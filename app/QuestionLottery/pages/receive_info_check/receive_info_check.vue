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
			<image src="../../static/ic_idcard.svg"  style="width: 300upx; height: 300upx; margin-top: 10upx;" mode="aspectFit"></image>
		</view>
		
		<view class="u-demo-block" style="margin-top: 30upx;">
			<view class="flex align-center">
				<image src="../../static/ic_idcard.png" mode="aspectFit" style="width: 25px; height: 25px; margin-right: 8px;"></image>
				<text style="font-size: 16px;">身份证号码</text>
			</view>
				
			<view class="u-demo-block__content" style="margin-top: 15px;">
				<u-input placeholder="请填写身份证" border="surround" shape="circle"></u-input>
			</view>
			
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
