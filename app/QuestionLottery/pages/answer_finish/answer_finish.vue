<template>
	<view class="u-page" style=" padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#6141ea" 
			title="答题结束" 
			@rightClick="rightClick" 
			:autoBack="true"
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
				<text class="title text-df text-green flex justify-center margin-top-xl align-center">今日剩余库存 {{answerResult.remain}} 件</text>
			</view>
			
			<u-button
				v-if="answerResult.score === 100"
			    text="开始选择"
			    size="normal"
				color="#6141ea"
				shape="circle"
				:disabled="answerResult.remain <= 0"
				style="margin-top: 50upx;"
				@click="onChooseItem"
			></u-button>
			
			<u-button
				v-if="answerResult.score < 100"
			    text="再来一次"
			    size="normal"
				color="#6141ea"
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
				full: "恭喜您获得满分！您有机会获选择会员日普惠商品一件",
				fullNoRemain:"恭喜您获得满分！活动火热，普惠商品已被领空，请明日在来",
				noFull:"非满分提示”您未全部答对！再来一次，祝您好运！",
				answerResult:{
					score:100,
					hint:"提示语提示语提示语提示语提示语提示语提示语提示语提示语",
					remain:10
				}
			}
		},
		onLoad() {

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
			onChooseItem(){
				
			},
			onRetry(){
				
			},
			successCb(rsp) {
				console.log('get_answer_result success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){
					this.answerResult = rsp.data.msg.answer_result
				}
			},
			failPhoneCb(err) {
				console.log('get_answer_result failed', err);
			},
			completePhoneCb(rsp) {},
		}
	}
</script>

<style>

</style>
