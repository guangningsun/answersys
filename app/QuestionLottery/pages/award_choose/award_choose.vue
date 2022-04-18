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
		
		<view class=""  v-for="(item, index) in awardInfoList" :key="index" style="margin-top: 30upx; margin-bottom: 30upx; padding: 20upx; border-radius: 12upx; background-color: #FFFFFF;">
			<view class="flex justify-start align-center">
				<image :src="item.award_image"  style="width: 150upx; height: 150upx; margin-right: 10upx;" mode="aspectFit"></image>
				<view>
					<text class="title text-df text-black justify-center justify-start align-start">{{item.award_name}}</text>	
					<text class="title text-sm text-gray justify-center justify-start align-start margin-left-lg">今日剩余{{item.current_max}}件</text>
				</view>
				
			</view>
			<u-button
			    text="领取"
			    size="small"
				color="#ed945d"
				style="padding: 10upx; width: 80px;"
				@click="onClickReceive(item.id)"
			></u-button>
			
			<!-- <view class="u-demo-block"
			:disabled="item.current_max <= 0"
			style="margin-top: 30upx; margin-bottom: 30upx; padding: 15upx; padding-bottom: 30upx; border-radius: 12upx; border-style: solid; border-width: 1px; border-color:#eab28a; background-color: rgba(243, 237, 216, 0.3);">
				<text class="title text-bold text-xxl text-orange flex justify-center margin-top">{{answerResult.score}}分</text>
				<text class="title text-lg text-yellow flex justify-center margin-top align-center">{{answerResult.hint}}</text>
				<text class="title text-df text-green flex justify-center margin-top-xl align-center">今日剩余库存 {{answerResult.remain}} 件</text>
			</view> -->
			

		</view>
		
		<u-toast ref="uToast"></u-toast>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				awardInfoList:[]
			}
		},
		onLoad() {
		
			let params = {
				phone_number: uni.getStorageSync('key_phone_num'),
			};
			
			this.requestWithMethod(
				getApp().globalData.get_award_info,
				'GET',
				'',
				this.successCb,
				this.failCb,
				this.completeCb
			);
		},
		
		methods: {
			showToast(params) {
				this.$refs.uToast.show({
					...params,
					complete() {
						params.url && uni.navigateTo({
							url: params.url
						})
					}
				})
			},
			onClickReceive(id){
				console.log(id)
				
				let params = {
					phone_number: uni.getStorageSync('key_phone_num'),
					award_id:id
				};
				
				this.requestWithMethod(
					getApp().globalData.revice_award,
					'POST',
					params,
					this.successReviceAwardCb,
					this.failReviceAwardCb,
					this.completeReviceAwardCb
				);
			},
			
			
			successReviceAwardCb(rsp) {
				console.log('revice_award success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){
					let par = {
						type: 'success',
						message: '恭喜你！' + rsp.data.msg,
						url: '../index/index'
					}
					this.showToast(par)
					// uni.showToast({
					// 	title: rsp.data.msg,
					// 	icon: 'success',
					// 	duration:3000,
					// 	complete: () => {
					// 		uni.navigateTo({
					// 			url:'../index/index'
					// 		})
					// 	}
					// })
				}
			},
			failReviceAwardCb(err) {
				console.log('revice_award failed', err);
			},
			completeReviceAwardCb(rsp) {},
			
			
			successCb(rsp) {
				console.log('get_award_info success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){
					this.awardInfoList = rsp.data.msg.awardlist
				}
			},
			failCb(err) {
				console.log('get_award_info failed', err);
			},
			completeCb(rsp) {}
		}
	}
</script>

<style>

</style>
