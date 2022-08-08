<template>
	<view class="u-page" style="background-color: #FFFFFF; padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#8145e1"
			title="信息确认" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="bg-light-yellow2 text-purple padding-sm">{{hint}}</view>
		
		<view class="flex justify-center">
			<image src="../../static/ic_comfirm.png"  style="width: 300upx; height: 300upx; margin-top: 10upx;" mode="aspectFit"></image>
		</view>
		
		<view class="u-demo-block"  style="margin-top: 30upx; margin-bottom: 30upx; padding: 15upx; border-radius: 12upx; background-color: #FFFFFF;">
			<u--form
				labelPosition="left">
				<u-form-item
					label="姓名"
					prop="userInfo.name"
					labelWidth="100"
					borderBottom>
					<u--text
						:text="userInfo.name"
					></u--text>
				</u-form-item>
				<u-form-item
					label="联系方式"
					prop="userInfo.tel"
					borderBottom
					labelWidth="100"
				>
					<u--text
						:text="userInfo.tel"
					></u--text>
				</u-form-item>
				<u-form-item
					label="所属单位"
					prop="userInfo.company"
					borderBottom
					labelWidth="100"
				>
					<u--text
						:text="userInfo.company"
					></u--text>
				</u-form-item>
				<!-- <u-form-item
					label="新增单位联系人"
					prop="userInfo.company_connect"
					borderBottom
					labelWidth="100"
				>
					<u--text
						:text="userInfo.company_connect"
					></u--text>
				</u-form-item>
				<u-form-item
					label="联系人电话"
					prop="userInfo.company_phone"
					borderBottom
					labelWidth="100"
				>
					<u--text
						:text="userInfo.company_phone"
					></u--text>
				</u-form-item> -->
				<u-form-item
					label="所属单位收货地址"
					prop="userInfo.company_address"
					borderBottom
					labelWidth="100"
				>
					<u--text
						:text="userInfo.company_address"
					></u--text>
				</u-form-item>
				
				<u-form-item
					label="备注"
					prop="remark"
					borderBottom
				>
					<u--textarea
						placeholder="若有需要修改的地方请填写"
						v-model="remark"
						count
					></u--textarea>
				</u-form-item>
			</u--form>
			
			<u-button
			    text="确认"
			    size="normal"
				color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
				style="margin-top: 50px; margin-bottom: 50px;"
				@click="onConfirm"
			></u-button>
			
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				userInfo:{
					name:'--',
					tel:'--',
					company:'--',
					company_address:'--',
					company_connect: '--',
					company_phone: '--'
				},
				hint: '请确认信息',
				noInfoHint: '请联系更新',
				phoneNum:uni.getStorageSync('key_phone_num'),
				remark:'',
			}
		},
		onLoad() {
		
			uni.showLoading({
				title:'查询中...',
				mask:true
			})
		
			let params = {
				phone_number: uni.getStorageSync('key_phone_num')
			};
			
			this.requestWithMethod(
				getApp().globalData.get_user_award_info,
				'POST',
				params,
				this.successCb,
				this.failCb,
				this.completeCb
			);
		},
		methods: {
			successCb(rsp) {
				console.log('get_user_award_info success, rsp======');
				console.log(rsp);
				uni.hideLoading();
				if(rsp.data.error === 0){
					this.userInfo = rsp.data.msg.awardInfos
					this.hint = rsp.data.msg.hint
					this.noInfoHint = rsp.data.msg.noInfoHint
					
					if(this.userInfo === undefined || this.userInfo === {} || this.userInfo === ''){
						// if(true){
						uni.showModal({
							content: this.noInfoHint,
							title: '提示',
							confirmText: "确认", // 确认按钮的文字  
							showCancel: true, // 是否显示取消按钮，默认为 true
							confirmColor: '#39B54A',
							success: (res) => {
							if(res.confirm) {  
								uni.navigateTo({
									url:'../index/index'
								})
							} else {  
								console.log('cancel') //点击取消之后执行的代码
								}  
							}
						})
					}
				}
			},
			failCb(err) {
				console.log('get_user_award_info failed', err);
				uni.hideLoading()
			},
			completeCb(rsp) {},
			
			
			onConfirm(){
				
				if(this.userInfo.tel === '--' || this.isEmpty(this.userInfo.tel)){
					uni.showToast({
						icon:"none",
						title:'请填写正确的手机号'
					})
					return
				}
				
				uni.showLoading({
					title:'查询中...',
					mask:true
				})
				let params = {
					phone_number: uni.getStorageSync('key_phone_num'),
					remark: this.remark,
					apart_id: uni.getStorageSync('key_apart')
				};
				
				this.requestWithMethod(
					getApp().globalData.submit_user_info,
					'POST',
					params,
					this.successConfirmCb,
					this.failConfirmCb,
					this.completeConfirmCb
				);

			},
			successConfirmCb(rsp) {
				console.log('submit_user_info success, rsp======');
				console.log(rsp);
				uni.hideLoading();
				if(rsp.data.error === 0){
					uni.navigateTo({
						url:'../answering/answering'
					})
				}
			},
			failConfirmCb(err) {
				uni.hideLoading();
				console.log('submit_user_info failed', err);
			},
			completeConfirmCb(rsp) {},
		}
	}
</script>

<style>

</style>
