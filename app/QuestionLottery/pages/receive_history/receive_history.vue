<template>
	<view class="u-page" style=" padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#5de992" 
			title="领取记录" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view v-if="historyList.length === 0" class="">
			<u-empty
				mode="history"
				icon="http://cdn.uviewui.com/uview/empty/history.png"
			>
			</u-empty>
		</view>
		
		<view v-if="historyList" class=""  v-for="(item, index) in historyList" :key="index" style="margin-top: 20upx; margin-bottom: 20upx; border-radius: 12upx; background-color: #FFFFFF;">
			<view class="flex justify-start align-center">
				<image :src="item.award_image === null ? '../../static/default.png' : domain + item.award_image"  style="width: 200upx; height: 200upx;" mode="aspectFit"></image>
				<view class="margin-left-xl">
					<view class="margin-top-sm">
						<text class=" title text-df text-bold text-black justify-center justify-start align-start">{{item.award_name}}</text>	
					</view>
					<view class="margin-top-sm">
						<text class="title text-sm text-gray justify-center justify-start align-start ">{{item.revice_time}}</text>
					</view>
				</view>
			</view>
		</view>
		
		<!-- <u-toast ref="uToast"></u-toast> -->
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				domain: getApp().globalData.domain,
				historyList:[
					// {
					// 	id: 1,
					// 	award_name: 'xx11x',
					// 	date:'2022-04-20',  
					// 	img:'https://cdn.uviewui.com/uview/album/1.jpg',
					// },
					// {
					// 	id: 2,
					// 	award_name: 'xx33x',
					// 	date:'2022-04-20',  
					// 	img:'https://cdn.uviewui.com/uview/album/2.jpg',
					// },
					// {
					// 	id: 3,
					// 	award_name: 'xx22x',
					// 	date:'2022-04-20',  
					// 	img:'https://cdn.uviewui.com/uview/album/1.jpg',
					// }
				]
			}
		},
		onLoad() {
		
			uni.showLoading({
				title:'查询中...'
			})
			let params = {
				phone_number: uni.getStorageSync('key_phone_num'),
			};
			
			this.requestWithMethod(
				getApp().globalData.get_award_history,
				'POST',
				params,
				this.successCb,
				this.failCb,
				this.completeCb
			);
		},
		
		methods: {			
			successCb(rsp) {
				uni.hideLoading()
				console.log('get_award_history success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){
					this.historyList = rsp.data.msg.awardlist
				}
			},
			failCb(err) {
				console.log('get_award_history failed', err);
				uni.hideLoading()
			},
			completeCb(rsp) {}
		}
	}
</script>

<style>

</style>
