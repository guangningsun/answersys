<template>
	<view class="u-page" style=" padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#8145e1"
			title="提示" 
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
				<image src="../../static/ic_error.png"  style="width: 380upx; height: 400upx; margin-top: 30upx;" mode="aspectFit"></image>
			</view>
			
			<u-button
			    text="返回"
			    size="normal"
				color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
				shape="circle"
				style="margin-top: 100upx;"
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
				answerResult:{}
			}
		},
		onLoad() {

		},
		methods: {
			onLeft(){
				uni.navigateTo({
					url:'../index/index'
				})
			},
			onRetry(){
				uni.navigateTo({
					url:'../index/index'
				})
			}
		}
	}
</script>

<style>

</style>
