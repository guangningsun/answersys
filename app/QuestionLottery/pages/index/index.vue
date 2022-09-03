<template>
	<view >
		<view class="padding-left-sm">
			<image class="bg-set" src="../../static/activity_bg.jpg"></image>
		</view>
		
		<view
			v-show="!isActivityStart"
			class="flex justify-center" 
			style="padding-top: 750rpx; width:100%; ">
			
			<view 
			style="font-size: 20px; 
				border-radius: 20upx; 
				color: #FFFFFF; 
				padding-left: 30upx; 
				padding-right: 30upx; 
				padding-bottom: 20upx; 
				padding-top: 20upx; 
				margin-left: 40upx;
				margin-right:40upx;
				background-color: rgba(51, 52, 52, 0.5)">{{startMsg}}</view> 
		</view>
		
		<view
			v-if="isActivityStart && shouldShowContent"
			class="flex text-gray justify-center align-center padding-sm"
			style="border-radius: 20upx; position:fixed; bottom:0;padding-left: 20upx; padding-bottom: 200upx; padding-top: 10upx;"
			>
			<view class="justify-center " style="margin-top: 150upx; margin-left: 15upx; margin-right: 15upx">
			  <image @click="onRule" src="../../static/btn_rule.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>			
			</view>
			<view v-show="isActivityStart" class="justify-center" style="padding-bottom: 250upx; "  @click="onStart">
			  <image id="animat" src="../../static/btn_start.png" style="width: 300upx; height: 100upx;" mode="aspectFit"></image>
			</view>
		</view>

		<!-- <view v-show="isActivityStart" class="justify-center align-center" style="padding-bottom: 120upx; padding-top: 1150rpx;"  @click="onStart">
			<image id="animat" src="../../static/btn_start.png" style="width: 300upx; height: 100upx;margin-top: 50upx;margin-left: 240upx;" mode="aspectFit"></image>
			
			<view class="flex justify-center " style="margin-top: 10rpx; margin-left: 15upx; margin-right: 15upx">
				<image @click="onRule" src="../../static/btn_rule.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>
				<image @click="onRank" src="../../static/btn_rank.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>
				<image @click="onRecord" src="../../static/btn_receive_record.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>
			</view>
		</view> -->
		
		
		<view v-show="!shouldShowContent && showCenterIcon">
			<view
				class="text-gray text-center justify-center padding-sm"
				style="border-radius: 20upx; 
				position:fixed; bottom:0; 
				padding: 15upx; 
				background-color: rgba(51, 52, 52, 0.5); 
				padding-bottom: 40upx; 
				padding-top: 20upx;">
				<button
					class="bg-gradual-orange text-df"
					open-type="getPhoneNumber"
					lang="zh_CN"
					@getphonenumber="getPhoneNumber">
					手机号登录
				</button>
				<view style="color: #FFFFFF; margin-top: 15upx;">{{ hint }}</view> 
			</view>
		</view>
		
		<!-- 申请手机号modal -->
		<view class="cu-modal" :class="modalName == 'PhoneModal' ? 'show' : ''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">手机号登录</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
				<view class="padding-xl">{{ hint }}</view>
				<view class="cu-bar bg-white padding-bottom">
					<view class="flex justify-end action" style="width: 100%;">
						<button class="cu-btn line-gray lg text-gray" style="padding: 0 80upx;" @tap="hideModal">拒绝</button>
						<button
							class="cu-btn lg bg-gradual-purple margin-left-sm"
							style="padding: 0 80upx;"
							open-type="getPhoneNumber"
							lang="zh_CN"
							@getphonenumber="getPhoneNumber"
						>
							同意
						</button>
					</view>
				</view>
			</view>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {

			return {
				modalName: null,
				canGetPrize: true,
				openid: '',
				user_nickname: '',
				user_phone: '',
				// user_auth: '',
				user_info:null,
				
				apartmentId:'',
				
				shouldShowContent: false,
				showCenterIcon: true,
				
				isActivityStart: false,
				
				isMember: false,
				
				memberMsg: '',
				
				startMsg:'',
				
				isLogin: false,
				
				hint:
					'登录后可以完整使用服务。首次使用，需要授权获取您的手机号进行登录绑定。'
				
			}
		},
		onLoad: function(options) {
			console.log('======二维码解析参数========');
			console.log(options.q);
			var scene = decodeURIComponent(options.q); // 使用decodeURIComponent解析  获取当前二维码的网址
			var arr1 = scene.split('/');
			var apartId = arr1[arr1.length - 1];
			this.apartmentId = apartId;
			
			

			uni.setStorageSync(getApp().globalData.key_apart, this.apartmentId);
		},
		onShow() {
			this.user_phone = uni.getStorageSync(getApp().globalData.key_phone_num);
			this.openid = uni.getStorageSync(getApp().globalData.key_wx_openid);
		
			uni.login({
				provider: 'weixin',
				success: loginRes => {
					console.log('+++code：' + loginRes.code);
		
					uni.showLoading({
						title:'正在查询中...'
					})
					this.requestWithMethod(
						getApp().globalData.api_login + loginRes.code,
						'POST',
						'',
						this.successCb,
						this.failCb,
						this.completeCb
					);
				}
			});
			uni.showLoading({
				title:'正在查询中...'
			})
			this.requestWithMethod(
				getApp().globalData.is_in_activity_time,
				'GET',
				'',
				this.successInActCb,
				this.failInActCb,
				this.completeInActCb
			)
		},
		methods: {
			showAlreadyLottery(){
				uni.showToast({
					icon:"none",
					title:'您已经抽奖，不能再次参与活动'
				})
			},
			onStart(){
				
				let apartId
				// #ifdef MP-WEIXIN
				    // 获取当前帐号信息
				    const accountInfo = wx.getAccountInfoSync();
				    console.log(accountInfo)
				    // env类型 develop:开发版、trial:体验版、release:正式版
				    const envWx = accountInfo.miniProgram.envVersion;
				    if(envWx === 'release'){
				        apartId = this.apartmentId
				    }else{
				        apartId = 1507
				    }
				// #endif
				console.log('mak testf', apartId)
				
				if(apartId === 'undefined'){
					uni.showToast({
						icon:"none",
						title:'请扫码参与活动'
					})
				} else if(!this.canGetPrize){
					this.showAlreadyLottery()

				} else {
					uni.showLoading({
						title:'正在查询中...'
					})
					let param = {
						phone_number: uni.getStorageSync(getApp().globalData.key_phone_num)
					}
					
					this.requestWithMethod(
						getApp().globalData.is_member,
						'POST',
						param,
						this.successIsMemberCb,
						this.failIsMemberCb,
						this.completeIsMemberCb
					);
				}
				
			},
			onRank(){
				uni.navigateTo({
					url:'../rank/rank'
				})
			},
			onRule(){
				uni.navigateTo({
					url:'../rule/rule'
				})
			},
			onRecord(){
				uni.navigateTo({
					url:'../receive_history/receive_history'
				})
			},
			onWarmup(){
				uni.navigateTo({
					url:'../warmup/warmup'
				})
			},
			showPhoneModal(e) {
				this.modalName = e;
			},
			hideModal(e) {
				this.modalName = null;
			},
			
			successIsMemberCb(rsp) {
				console.log('is_member success');
				console.log(rsp);
				uni.hideLoading()
				this.isMember = rsp.data.is_member
				this.memberMsg = rsp.data.msg
				this.canGetPrize = rsp.data.can_get_prize
				console.log('can_get_prize:' + this.canGetPrize)
				uni.setStorageSync(getApp().globalData.key_can_get_prize, this.canGetPrize);
				
				// if(!this.canGetPrize) {
				// 	this.showAlreadyLottery()
				// 	return
				// }
				
				if(this.isMember){
					uni.navigateTo({
						url:'../receive_info_check/receive_info_check'
					})
				}else{
					uni.showToast({
						title: this.memberMsg
					})
				}
			},
			failIsMemberCb(err) {
				console.log('is_member failed', err);
				uni.hideLoading()
			},
			completeIsMemberCb(rsp) {},
			
			////////////////////
			successInActCb(rsp) {
				console.log('is_in_activity_time success');
				console.log(rsp)
				console.log(rsp.statusCode + 'mmmk');
				uni.hideLoading()
				
				this.isActivityStart = rsp.data.is_start
				this.startMsg = rsp.data.msg				
				
				// this.isActivityStart = false
				// this.startMsg = '今日物品已经领空，请明日再来。由于参与人数较多，平台较拥堵，我们将要对服务进行优化，保证活动明天顺利开展。'
				
				// if (rsp.data.error === 0) {
				// 	this.isActivityStart = rsp.data.is_start
				// 	this.startMsg = rsp.data.msg
				// }
			},
			failInActCb(err) {
				console.log('is_in_activity_time failed', err);
				uni.hideLoading()
			},
			completeInActCb(rsp) {},
			//////////////////////////////
			successCb(rsp) {
				console.log('weixin_sns success');
				console.log(rsp);

				if (rsp.data.error === 0) {
					this.openid = rsp.data.openid;
					let is_login = rsp.data.is_login;
					// let user_auth = rsp.data.auth;
	
					// console.log(this.openid);
					
					// uni.setStorageSync(getApp().globalData.key_user_auth,user_auth);
	
					uni.setStorageSync(getApp().globalData.key_wx_openid,rsp.data.openid);
	
					////////
					console.log('is_login:' + is_login);
					if (is_login == 0) {
						this.showPhoneModal('PhoneModal');
					} else {
						// console.log('auth:' + user_auth);
						uni.showLoading({
							title: '登录中.......',
							mask:true
						});
						this.requestUserInfo();
					}
				}
			},
			failCb(err) {
				console.log('api_login failed', err);
				uni.hideLoading()
			},
			completeCb(rsp) {},
	/////
			successGetUserInfoCb(rsp) {
				uni.hideLoading();
				console.log(rsp)
				if (rsp.data.error === 0) {
					
					this.user_info = rsp.data.msg.user_info;
					console.log(this.user_info);
					
					let user_name = this.user_info[0].user_name;
					console.log('user_name====' + user_name);
					uni.setStorageSync(getApp().globalData.key_user_name, user_name);
					if(this.isEmpty(user_name)){
						uni.navigateTo({
							url:'./user_info'
						});
					}else{
						uni.setStorageSync(getApp().globalData.key_user_name,this.user_info[0].user_name);
						uni.setStorageSync(getApp().globalData.key_phone_num,this.user_info[0].phone_number);
						uni.hideLoading();
						this.shouldShowContent = true;
					}
				}
			},
			failGetUserInfoCb(err) {
				uni.hideLoading();
				console.log('get_user_info failed', err);
			},
			completeGetUserInfoCb(rsp) {},
			
			requestUserInfo() {
				let param
				this.requestWithMethod(
					getApp().globalData.get_user_info + this.openid,
					'GET',
					'',
					this.successGetUserInfoCb,
					this.failGetUserInfoCb,
					this.completeGetUserInfoCb
				);
			},
		// onGotUserInfo(e) {
		// 	console.log(e);
		// 	console.log(e.detail.userInfo.avatarUrl);
		// 	this.headImg = e.detail.userInfo.avatarUrl;
		// 	this.user_nickname = e.detail.userInfo.nickName;
		// 	uni.setStorageSync( getApp().globalData.key_user_head, e.detail.userInfo.avatarUrl);
		// 	uni.setStorageSync(getApp().globalData.key_user_nickname, e.detail.userInfo.nickName);
		// },

		///////////////

		successPhoneCb(rsp) {
			console.log('weixin_gusi success, rsp======');
			console.log(rsp);
			this.showCenterIcon = false;
			
			if (this.containsStr(rsp.errMsg, 'ok')) {
				uni.setStorageSync(getApp().globalData.key_phone_num,rsp.data.purePhoneNumber);
				uni.hideLoading();
				this.requestUserInfo();
			}
			
			if(rsp.data.is_exist === '1'){
				// 用户存在
			} else {
				if(!uni.getStorageSync('key_key_is_update')){
					// 用户不存在，进入信息登记页面
					uni.navigateTo({
						url:'../login/register'
					})
				}
			}
		},
		failPhoneCb(err) {
			console.log('weixin_gusi failed', err);
		},
		completePhoneCb(rsp) {},

		getPhoneNumber(e) {
			this.hideModal();

			var that = this;
			// 拒绝授权
			if (e.detail.errMsg == 'getPhoneNumber:fail user deny') {
				uni.showModal({
					title: '提示',
					showCancel: false,
					content: '未授权将无法登录',
					success: function(res) {}
				});
			} else {
				uni.showLoading({
					title: '跳转中'
				});

				let params = {
					encryptedData: e.detail.encryptedData,
					iv: e.detail.iv,
					openid: this.openid
				};
				this.requestWithMethod(
					getApp().globalData.api_getWXInfo,
					'POST',
					params,
					this.successPhoneCb,
					this.failPhoneCb,
					this.completePhoneCb
				);
			}
		}
		}
	}
</script>

<style>
	.bg-set {
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}
	.container {
		padding: 20px;
		font-size: 14px;
		line-height: 24px;
	}
	
	
	#animat{
			position:relative;
			animation:mymove 2s infinite;
			-webkit-animation:mymove 2s infinite; /*Safari and Chrome*/
			animation-direction:alternate;/*轮流反向播放动画。*/
			animation-timing-function: ease-in-out; /*动画的速度曲线*/
			/* Safari 和 Chrome */
			-webkit-animation:mymove 2s infinite;
			-webkit-animation-direction:alternate;/*轮流反向播放动画。*/
			-webkit-animation-timing-function: ease-in-out; /*动画的速度曲线*/
		}
		@keyframes mymove
		{
			0%{
			transform: scale(1);  /*开始为原始大小*/
			}
			25%{
				transform: scale(1.025); /*放大1.06倍*/
			}
			50%{
				transform: scale(1);
			}
			75%{
				transform: scale(1.025);
			}
	
		}
	
		@-webkit-keyframes mymove /*Safari and Chrome*/
		{
			0%{
			transform: scale(1);  /*开始为原始大小*/
			}
			25%{
				transform: scale(1.025); /*放大1.06倍*/
			}
			50%{
				transform: scale(1);
			}
			75%{
				transform: scale(1.025);
			}
		}
		
</style>
