<template>
	<view class="u-page" style="background-color: #FFFFFF; padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#6141ea" 
			title="信息确认" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
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
					<u--input
						v-model="userInfo.name"
						border="none"
					></u--input>
				</u-form-item>
				<u-form-item
					label="联系方式"
					prop="userInfo.tel"
					borderBottom
					labelWidth="100"
				>
					<u--input
						v-model="userInfo.tel"
						border="none"
					></u--input>
				</u-form-item>
				<u-form-item
					label="所属单位"
					prop="userInfo.company"
					borderBottom
					labelWidth="100"
				>
					<u--input
						v-model="userInfo.company"
						border="none"
					></u--input>
				</u-form-item>
				
				<u-form-item
					label="所属单位收货地址"
					prop="userInfo.company_address"
					borderBottom
					labelWidth="100"
				>
					<u--input
						v-model="userInfo.company_address"
						border="none"
					></u--input>
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
				color="#6141ea"
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
				userInfo:{},
				phoneNum:uni.getStorageSync('key_phone_num'),
				remark:''
			}
		},
		onLoad() {
		
			let params = {
				phone_number: uni.getStorageSync('key_phone_num'),
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
				if(rsp.data.error === 0){
					this.userInfo = rsp.data.msg.awardInfos
				}
			},
			failCb(err) {
				console.log('get_user_award_info failed', err);
			},
			completeCb(rsp) {},
			
			
			onConfirm(){
				if(getApp().isEmpty(this.remark)){
					uni.navigateTo({
						url:'../award_choose/award_choose'
					})
				} else {
					let params = {
						phone_number: uni.getStorageSync('key_phone_num'),
					};
					
					this.requestWithMethod(
						getApp().globalData.submit_user_info,
						'POST',
						params,
						this.successConfirmCb,
						this.failConfirmCb,
						this.completeConfirmCb
					);
				}
			},
			successConfirmCb(rsp) {
				console.log('submit_user_info success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){
					uni.navigateTo({
						url:'../award_choose/award_choose'
					})
				}
			},
			failConfirmCb(err) {
				console.log('submit_user_info failed', err);
			},
			completeConfirmCb(rsp) {},
		}
	}
</script>

<style>

</style>
