<template>
	<view class="u-page" style=" padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#5de992" 
			title="领取奖品" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="u-demo-bloc"  v-for="(item, index) in awardInfoList" :key="index" style="margin-top: 30upx; margin-bottom: 30upx; padding: 20upx; border-radius: 12upx; background-color: #FFFFFF;">
			<view class="flex justify-start align-center">
				<!-- <image :src="item.award_image"  style="width: 200upx; height: 200upx;" mode="aspectFit"></image> -->
				<image :src=" item.award_image === null ? '../../static/default.png' : domain + item.award_image "  style="width: 200upx; height: 200upx;" mode="aspectFit"></image>
				<view class="margin-left-xl">
					<view class="margin-top-sm">
						<text class="title text-df text-black justify-center justify-start align-start">{{item.award_name}}</text>
					</view>
					<view class="margin-top-sm">
						<text class="title text-sm text-gray justify-center justify-start align-start ">今日剩余{{item.current_max}}件</text>
					</view>
				</view>

				<view class="flex justify-end align-end" style="margin-left: 60upx; margin-right: 10upx;">
					<u-button
					    text="领取"
					    size="small"
						color="linear-gradient(to right, rgb(13, 217, 128), rgb(105, 222, 162))"
						style="padding: 10upx; width: 60px; margin-right: 10upx;"
						@click="onClickReceive(item.id)"
					></u-button>
				</view>
				
			</view>
				
		</view>
		
		<u-toast ref="uToast"></u-toast>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				domain: getApp().globalData.domain,
				awardInfoList:[]
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
				uni.showLoading({
					title:'领取中...',
					mask:true
				})
				
				let params = {
					phone_number: uni.getStorageSync('key_phone_num'),
					award_id:id,
					apart_id: uni.getStorageSync('key_apart')
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
				uni.hideLoading()
				if(rsp.data.error === 0){
					let par = {
						message: rsp.data.msg,
						url: '../index/index'
					}
					this.showToast(par)
				}
				// if(rsp.data.error === 0 &&(rsp.data.msg.indexOf("已登记") != -1 || rsp.data.msg.indexOf("成功") != -1) ){
				// 	let par = {
				// 		type: 'success',
				// 		message: rsp.data.msg,
				// 		url: '../index/index'
				// 	}
				// 	this.showToast(par)
				// } else if(rsp.data.error === 0 && rsp.data.msg.indexOf("失败") != -1){
				// 	let par = {
				// 		type: 'fail',
				// 		message: rsp.data.msg,
				// 	}
				// 	this.showToast(par)
				// }
				
			},
			failReviceAwardCb(err) {
				uni.hideLoading()
				console.log('revice_award failed', err);
			},
			completeReviceAwardCb(rsp) {},
			
			
			successCb(rsp) {
				console.log('get_award_info success, rsp======');
				console.log(rsp);
				uni.hideLoading()
				if(rsp.data.error === 0){
					this.awardInfoList = rsp.data.msg.awardlist
				}
			},
			failCb(err) {
				uni.hideLoading()
				console.log('get_award_info failed', err);
			},
			completeCb(rsp) {}
		}
	}
</script>

<style>

</style>
