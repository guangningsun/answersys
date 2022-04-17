<template>
	<view >
		<view class="padding-left-sm">
			<image class="bg-set" src="../../static/activity_bg.jpg"></image>
		</view>
		<view class="flex justify-center" style="padding-top: 750rpx; width:100%;" @click="onStart">
			<image id="animat" src="../../static/btn_start.png" style="width: 300upx; height: 100upx;" mode="aspectFit"></image>
		</view>
		
		
		<view
			class="text-gray text-center justify-center padding-sm"
			style="border-radius: 20upx; 
			position:fixed; bottom:0; 
			padding: 15upx; 
			padding-bottom: 250upx; 
			padding-top: 20upx;">
			<view class="flex" style="margin-top: 50rpx; margin-left: 15upx; margin-right: 15upx">
				<image src="../../static/btn_rule.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>
				<image @click="onRank" src="../../static/btn_rank.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>
				<image @click="onRecord" src="../../static/btn_receive_record.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>
				<image @click="onWarmup" src="../../static/btn_warmup.png" style="width: 150upx; height: 100upx; margin: 10rpx;" mode="aspectFit"></image>
			</view>
		</view>
		
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
					class="bg-orange text-df"
					open-type="getPhoneNumber"
					lang="zh_CN"
					@getphonenumber="getPhoneNumber">
					手机号登录
				</button>
				<view style="color: #FFFFFF; margin-top: 15upx;">{{ hint }}</view> 
			</view>
		</view>
		
		<!-- 申请手机号modal -->
		<view class="cu-modal bottom-modal" :class="modalName == 'PhoneModal' ? 'show' : ''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">手机号登录</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
				<view class="padding-xl">{{ hint }}</view>
				<view class="cu-bar bg-white">
					<view class="flex justify-end action">
						<button class="cu-btn text-gray" @tap="hideModal">拒绝</button>
						<button
							class="cu-btn line-olive margin-left-sm"
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
				
				openid: '',
				user_nickname: '',
				user_phone: '',
				// user_auth: '',
				user_info:null,
				
				apartmentId:'',
				
				shouldShowContent: false,
				showCenterIcon: true,
				
				hint:
					'登录后可以完整使用服务。首次使用，需要授权获取您的手机号进行登录绑定。'
				
			}
		},
		onLoad: function(options) {
			// console.log('======二维码解析参数========');
			// console.log(options.q);
			// var scene = decodeURIComponent(options.q); // 使用decodeURIComponent解析  获取当前二维码的网址
			// var arr1 = scene.split('/');
			// var apartId = arr1[arr1.length - 1];
			// this.apartmentId = apartId;

			// uni.setStorageSync(getApp().globalData.key_cat, this.apartmentId);
		},
		onShow() {
			this.user_phone = uni.getStorageSync(getApp().globalData.key_phone_num);
			this.openid = uni.getStorageSync(getApp().globalData.key_wx_openid);
		
			uni.login({
				provider: 'weixin',
				success: loginRes => {
					console.log('+++code：' + loginRes.code);
		
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
		},
		methods: {
			onStart(){
				uni.navigateTo({
					url:'../answering/answering'
				})
			},
			onRank(){
				uni.navigateTo({
					url:'../rank/rank'
				})
			},
			onRecord(){
				uni.navigateTo({
					url:'../receive_history/receive_history'
				})
			},
			onWarmup(){
				// uni.navigateTo({
				// 	url:'../receive_history/receive_history'
				// })
			},
			showPhoneModal(e) {
				this.modalName = e;
			},
			hideModal(e) {
				this.modalName = null;
			},
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
							title: '登录中.......'
						});
						this.requestUserInfo();
					}
				}
			},
			failCb(err) {
				console.log('api_login failed', err);
			},
			completeCb(rsp) {},
	/////
			successGetUserInfoCb(rsp) {
				uni.hideLoading();
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

						// if(!this.isEmpty(this.apartmentId)){
						// 	uni.hideLoading();
						// 	uni.navigateTo({
						// 		url:'../category/category'
						// 	})
						// }else{
							uni.hideLoading();
							this.shouldShowContent = true;
						// }
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

		// 0: 普通用户， 1:主管,  2:办公室主任   3: 管理员
		successPhoneCb(rsp) {
			console.log('api_phone success, rsp======');
			console.log(rsp);
			this.showCenterIcon = false;

			if (this.containsStr(rsp.errMsg, 'ok')) {
				uni.setStorageSync(getApp().globalData.key_phone_num,rsp.data.purePhoneNumber);
				// uni.setStorageSync(getApp().globalData.key_user_auth,rsp.data.auth);

				// let auth = rsp.data.auth;
				// console.log('phone cb auth: ' + auth);
				uni.hideLoading();
				this.requestUserInfo();
			}
		},
		failPhoneCb(err) {
			console.log('api_phone failed', err);
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
