<template>
	<view class="u-page" style=" padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#6141ea" 
			title="领取奖品" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="" style="margin-top: 30upx; margin-bottom: 30upx; padding: 20upx; border-radius: 12upx; background-color: #FFFFFF;">
			<view class="flex justify-start align-center">
				<image src="../../static/ic_finish.png"  style="width: 150upx; height: 150upx; margin-right: 10upx;" mode="aspectFit"></image>
				<view>
					<text class="title text-df text-black justify-center justify-start align-start">xxx商品</text>	
					<text class="title text-sm text-gray justify-center justify-start align-start">今日剩余10件</text>
				</view>
			</view>
			
			<!-- <view class="u-demo-block"
			style="margin-top: 30upx; margin-bottom: 30upx; padding: 15upx; padding-bottom: 30upx; border-radius: 12upx; border-style: solid; border-width: 1px; border-color:#eab28a; background-color: rgba(243, 237, 216, 0.3);">
				<text class="title text-bold text-xxl text-orange flex justify-center margin-top">{{answerResult.score}}分</text>
				<text class="title text-lg text-yellow flex justify-center margin-top align-center">{{answerResult.hint}}</text>
				<text class="title text-df text-green flex justify-center margin-top-xl align-center">今日剩余库存 {{answerResult.remain}} 件</text>
			</view> -->
			

		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				awardInfo:[]
			}
		},
		onLoad() {
		
			let params = {
				phone_number: uni.getStorageSync('key_phone_num'),
			};
			
			this.requestWithMethod(
				getApp().globalData.get_award_info,
				'POST',
				params,
				this.successCb,
				this.failCb,
				this.completeCb
			);
		},
		methods: {
			successCb(rsp) {
				console.log('get_award_info success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){

				}
			},
			failPhoneCb(err) {
				console.log('get_award_info failed', err);
			},
			completePhoneCb(rsp) {},
		}
	}
</script>

<style>

</style>
