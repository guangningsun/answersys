<template>
	<view class="u-page" style=" padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#8145e1"
			title="答题结束" 
			@rightClick="rightClick" 
			@leftClick="onLeft"
			:autoBack="false"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="" style="margin-top: 30upx; margin-bottom: 30upx; padding: 30upx; border-radius: 12upx; background-color: #FFFFFF;">
			<view class="flex justify-center">
				<image src="../../static/ic_finish.png"  style="width: 380upx; height: 400upx; margin-top: 30upx;" mode="aspectFit"></image>
			</view>
			
			<view class="u-demo-block"
			style="margin-top: 30upx; margin-bottom: 30upx; padding: 15upx; padding-bottom: 30upx; border-radius: 12upx; border-style: solid; border-width: 1px; border-color:#eab28a; background-color: rgba(243, 237, 216, 0.3);">
				<text class="title text-bold text-xxl text-orange flex justify-center margin-top">{{answerResult.score}}分</text>
				<text class="title text-lg text-yellow flex justify-center margin-top align-center">{{answerResult.hint}}</text>
				<!-- <text class="title text-df text-green flex justify-center margin-top-xl align-center">今日剩余库存 {{answerResult.remain}} 件</text> -->
			</view>
			
			<u-button
				v-if="answerResult.score === 100"
			    text="领取奖品"
			    size="normal"
				color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
				shape="circle"
				:disabled="answerResult.remain <= 0"
				style="margin-top: 50upx;"
				@click="onChooseItem"
			></u-button>
			
			<u-button
				v-if="answerResult.score < 100"
			    text="再来一次"
			    size="normal"
				color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
				shape="circle"
				style="margin-top: 50upx;"
				@click="onRetry"
			></u-button>
		</view>
		
		
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				full: "",
				fullNoRemain:"",
				noFull:"",
				answerResult:{
					score:'--',
					hint:'--',
					remain:'--'
				}
			}
		},
		onLoad() {

			uni.showLoading({
				title:'查询中...',
				mask:true
			})
			let params = {
				phone_number: uni.getStorageSync('key_phone_num'),
			};
			// let params = {
			// 	phone_number: '18620083263'
			// };
			
			this.requestWithMethod(
				getApp().globalData.get_answer_result,
				'POST',
				params,
				this.successCb,
				this.failCb,
				this.completeCb
			);
		},
		methods: {
			onLeft(){
				console.log('mmmmm')
				uni.navigateTo({
					url:'../index/index'
				})
			},
			onChooseItem(){
				uni.navigateTo({
					// url:'../award_choose/award_choose'
					url:'../lottery/lotteryV2'
				})
			},
			onRetry(){
				uni.navigateTo({
					url:'../answering/answering'
				})
			},
			successCb(rsp) {
				console.log('get_answer_result success, rsp======');
				console.log(rsp);
				uni.hideLoading()
				if(rsp.data.error === 0){
					this.answerResult = rsp.data.msg.answer_result
				}
			},
			failCb(err) {
				console.log('get_answer_result failed', err);
				uni.hideLoading()
			},
			completeCb(rsp) {},
		}
	}
</script>

<style>

</style>
