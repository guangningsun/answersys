<template>
	<view class="u-page" style="background-color: #FFFFFF; padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#5de992" 
			title="身份认证" 
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
		    
			
			<u-checkbox-group
				v-model="checkValue"
				shape="square"
				@change="change"
				activeColor="#5de992"
			>
				<u-checkbox
					:customStyle="{marginRight: '16px', marginTop:'20px', marginBottom:'20px'}"
					v-for="(item, index) in checkboxList1"
					:key="index"
					:label="item.name"
					:name="item.name"
				>
				</u-checkbox>
			</u-checkbox-group>
			
		</view>
		
		<u-button
		    text="提交"
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
				checked:false,
				checkValue:[],
				checkboxList1: [{
						name: '协议',
						disabled: false
					}
				]
			}
		},
		methods: {
			checkboxChange(n) {
				console.log('change', n);
			},
			change(e) {
				console.log(e);
			},
		}
	}
</script>

<style>

</style>
