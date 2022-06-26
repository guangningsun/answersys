<template>
	<view class="u-page" style="background-color: #FFFFFF; padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#5de992" 
			title="信息确认" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="flex justify-center">
			<image src="../../static/ic_idcard.svg"  style="width: 300upx; height: 300upx; margin-top: 10upx;" mode="aspectFit"></image>
		</view>
		
		<view class="u-demo-block" style="margin-top: 30upx; padding-bottom: 40upx;">
			<view style="margin-bottom: 40upx;">
				<u--text prefixIcon="phone" style="font-size: 18px;" text="手机号: "></u--text>
				<u--text style="font-size: 20px;" :text="phone"></u--text>
			</view>
			
			<view class="flex ">
				<image src="../../static/ic_idcard.png" mode="aspectFit" style="width: 25px; height: 25px; margin-right: 8px;"></image>
				<text style="font-size: 16px;">身份证号码</text>
			</view>
				
			<view class="u-demo-block__content" style="margin-top: 15px;">
				<u-input  v-model="idNum" placeholder="请填写身份证" border="surround" shape="circle"></u-input>
			</view>
			
		</view>
		
		<u-button
		    text="确认"
		    size="normal"
			color="linear-gradient(to right, rgb(13, 217, 128), rgb(105, 222, 162))"
			style="margin-top: 50px;"
			@click="onSubmit"
		></u-button>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				phone: uni.getStorageSync('key_phone_num'),
				idNum: ""
				// checked:false,
				// checkValue:[],
				// checkboxList1: [{
				// 		name: '协议',
				// 		disabled: false
				// 	}
				// ]
			}
		},
		methods: {
			checkboxChange(n) {
				console.log('change', n);
			},
			change(e) {
				console.log(e);
			},
			onSubmit(){
				let params = {
					phone_number: this.phone,
					id_card:this.idNum,
					open_id:uni.getStorageSync(getApp().globalData.key_wx_openid)
				};
				
				this.requestWithMethod(
					getApp().globalData.register_user,
					'POST',
					params,
					this.successCb,
					this.failCb,
					this.completeCb
				);
			},
			successCb(rsp) {
				console.log('register_user success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0 && rsp.data.is_update){
					
					uni.setStorageSync(getApp().globalData.key_is_update, rsp.data.is_update);
					uni.navigateTo({
						url:'../index/index'
					})
				}
			},
			failCb(err) {
				console.log('register_user failed', err);
			},
			completeCb(rsp) {},
		}
	}
</script>

<style>

</style>
