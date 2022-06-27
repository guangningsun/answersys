<template>
    <view class="u-page">

		<u-navbar
			bgColor="#8145e1"
			title="活动规则" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>

		<view class="u-demo-block"  
			style="margin-top: 30upx; 
			margin-left: 15upx; 
			margin-right: 15upx; 
			margin-bottom: 30upx; 
			border-radius: 12upx; 
			background-color: #FFFFFF;">
			<view v-show="!showServerRule" class="text-grey text-lg" style="padding-top: 30upx; padding-bottom: 30upx; padding-left: 20upx;padding-right: 20upx;">
				
				1.活动时间：{{activityTimeStr}}（具体时间以微信通知为准）；<br/>
				2.参与范围：经开区在库职工；<br/>
				3.每人只有一次答题机会，满分者有一次抽奖获得百事可乐一包的机会；<br/>
				4.请扫描本单位专属二维码参加活动，避免信息不匹配造成不能正常参加活动，或者奖品不能送达个人；<br/>
				5.普惠物品将送至职工所在单位；<br/>
				技术支持：孙照瑛  联系电话：15022746250 
				
			</view>
			
			<view class="padding:15upx">
				<span  
					v-show="showServerRule" 
					class="text-grey text-lg" 
					style="white-space: pre-wrap; padding-top: 30upx; padding-left: 20upx;padding-right: 20upx;"
					>
					{{ruleContent}}
				</span>
			</view>
		</view>
		
     
    </view>
</template>

<script>
export default {
    data() {
        return {
			activityTimeStr: '2022年7月1日-7月3日',
			showServerRule: false,
			ruleContent: `1.活动时间：2022年7月1日-7月3日（具体时间以微信通知为准）；\n2.参与范围：经开区在库职工；\n3.每人只有一次答题机会，满分者有一次抽奖获得百事可乐一包的机会；\n4.请扫描本单位专属二维码参加活动，避免信息不匹配造成不能正常参加活动，或者奖品不能送达个人；\n5.普惠物品将送至职工所在单位；\n技术支持：孙照瑛  联系电话：15022746250`
		}
    },
	onLoad() {
		uni.showLoading({
			title:'查询中...',
			mask:true
		})

		this.requestWithMethod(
			getApp().globalData.get_rule_info,
			'GET',
			'',
			this.successCb,
			this.failCb,
			this.completeCb,
			false
		);
	},
	
	methods: {
		successCb(rsp) {
			console.log('get_rule_info success, rsp======');
			console.log(rsp);
			uni.hideLoading()
			if(rsp.data.rule_content){
				this.showServerRule = true
				this.ruleContent = rsp.data.rule_content
			} else{
				this.showServerRule = false
			}
		},
		failCb(err) {
			uni.hideLoading()
			console.log('get_rule_info failed', err);
		},
		completeCb(rsp) {}
	}
};
</script>

<style lang="scss">

</style>
