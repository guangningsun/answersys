<template>
	<view class="u-page" style="padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#6141ea" 
			title="成绩排行" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="u-demo-block" v-for="(item, index) in rankList" :key="index"  style="margin-top: 30upx; margin-bottom: 30upx; padding: 20upx; border-radius: 12upx; background-color: #FFFFFF;">
			<view class="u-demo-block__content" >
				<view v-if="index === 0" class="flex align-center">
					<image src="../../static/ic_place1.png" mode="aspectFit" style="width: 25px; height: 25px; margin-right: 8px;"></image>
					<!-- <u-avatar :src="this.getRandomAvatar" style="margin-right: 20upx;"></u-avatar> -->
					<text class="title text-bold text-lg text-black" style="padding-right: 20upx;">{{item.id}}</text>
					<text class="title text-lg text-black" style="padding-right: 35upx;">{{item.tel}}</text>
					<text class="title text-lg text-black justify-end" style="color: #007AFF;">分数:{{item.score}}</text>
				</view>
				<view v-if="index === 1" class="flex align-center">
					<image src="../../static/ic_place2.png" mode="aspectFit" style="width: 25px; height: 25px; margin-right: 8px;"></image>
					<!-- <u-avatar :src="this.getRandomAvatar" style="margin-right: 20upx;"></u-avatar> -->
					<text class="title text-bold text-lg text-black" style="padding-right: 20upx;">{{item.id}}</text>
					<text class="title text-lg text-black" style="padding-right: 35upx;">{{item.tel}}</text>
					<text class="title text-lg text-black justify-end" style="color: #007AFF;">分数:{{item.score}}</text>
				</view>
				<view v-if="index === 2" class="flex align-center">
					<image src="../../static/ic_place3.png" mode="aspectFit" style="width: 25px; height: 25px; margin-right: 8px;"></image>
					<!-- <u-avatar :src="this.getRandomAvatar" style="margin-right: 20upx;"></u-avatar> -->
					<text class="title text-bold text-lg text-black" style="padding-right: 20upx;">{{item.id}}</text>
					<text class="title text-lg text-black" style="padding-right: 35upx;">{{item.tel}}</text>
					<text class="title text-lg text-black justify-end" style="color: #007AFF;">分数:{{item.score}}</text>
				</view>
				<view v-if="index > 2" class="flex align-center">
					<image src="../../static/ic_place.png" mode="aspectFit" style="width: 25px; height: 25px; margin-right: 8px;"></image>
					<!-- <u-avatar :src="this.getRandomAvatar" style="margin-right: 20upx;"></u-avatar> -->
					<text class="title text-bold text-lg text-black" style="padding-right: 20upx;">{{item.id}}</text>
					<text class="title text-lg text-black" style="padding-right: 35upx;">{{item.tel}}</text>
					<text class="title text-lg text-black justify-end" style="color: #007AFF;">分数:{{item.score}}</text>
				</view>
			</view>
		</view>

		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				avatarSrc:[
					'../../static/ic_head_1.png',
					'../../static/ic_head_2.png',
					'../../static/ic_head_3.png',
					'../../static/ic_head_4.png'
					],
				// rankList:[
				// 	{
				// 		nick:'昵称AAA',
				// 		tel:'184****4356',
				// 		score:'100',
				// 		img:'/头像url'
				// 	},
				// 	{
				// 		nick:'昵称ABB',
				// 		tel:'177****9999',
				// 		score:'100',
				// 		img:'/头像url'
				// 	},
				// 	{
				// 		nick:'昵称CC',
				// 		tel:'133****4366',
				// 		score:'100',
				// 		img:'/头像url'
				// 	},
				// 	{
				// 		nick:'昵11称AAA',
				// 		tel:'134****4356',
				// 		score:'90',
				// 		img:'/头像url'
				// 	},
				// ]
				rankList:[]
			}
		},
		onLoad() {
			this.requestWithMethod(
				getApp().globalData.get_rankinfo,
				'GET',
				'',
				this.successCb,
				this.failCb,
				this.completeCb
			);
		},
		methods: {
			getRandomAvatar(){
				let index = Math.round(Math.random()*avatarSrc.length-1)
				return avatarSrc[index]
			},
			successCb(rsp) {
				console.log('get_rankinfo success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){
					this.rankList = rsp.data.msg.rankList
				}
				
			},
			failPhoneCb(err) {
				console.log('get_rankinfo failed', err);
			},
			completePhoneCb(rsp) {}
		}
	}
</script>

<style>

.demo-layout {
    height: 25px;
    border-radius: 4px;
}

.bg-purple {
    background: #ced7e1;
}

.bg-purple-light {
    background: #e5e9f2;
}

.bg-purple-dark {
    background: #99a9bf;
}
</style>
