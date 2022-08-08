<template>
	<view class="u-page" style=" padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#8145e1"
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
						<text class="title text-sm text-gray justify-center justify-start align-start ">今日剩余{{item.award_num}}件</text>
					</view>
				</view>

				<view class="flex justify-end align-end" style="margin-left: 60upx; margin-right: 10upx;">
					<u-button
					    text="领取"
					    size="small"
						color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
						style="padding: 10upx; width: 60px; margin-right: 10upx;"
						@click="onClickReceive(item)"
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
		onShow() {
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
		onLoad() {
			
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
			onClickReceive(item){
				console.log('itemId: ', item.id)
				
				let num = parseInt(item.award_num)
				
				if (num <= 0){
					uni.showToast({
						icon:"none",
						title:'奖品剩余数量不足'
					})
				}else{
					uni.showLoading({
						title:'领取中...',
						mask:true
					})
					
					let apartId
					// #ifdef MP-WEIXIN
					    // 获取当前帐号信息
					    const accountInfo = wx.getAccountInfoSync();
					    console.log(accountInfo)
					    // env类型 develop:开发版、trial:体验版、release:正式版
					    const envWx = accountInfo.miniProgram.envVersion;
					    if(envWx === 'release'){
					        apartId = uni.getStorageSync('key_apart')
					    }else{
					        apartId = 1507
					    }
					// #endif
					console.log('mak test2', apartId)
					
					let params = {
						phone_number: uni.getStorageSync('key_phone_num'),
						award_id:item.id,
						apart_id: apartId
					};
					
					this.requestWithMethod(
						getApp().globalData.revice_award,
						'POST',
						params,
						this.successReviceAwardCb,
						this.failReviceAwardCb,
						this.completeReviceAwardCb
					);
				}
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
