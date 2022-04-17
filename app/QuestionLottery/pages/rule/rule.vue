<template>
    <view class="u-page">
		<view class="">
			<u-navbar
				bgColor="#6141ea" 
				title="活动规则" 
				@rightClick="rightClick" 
				:autoBack="true"
				safeAreaInsetTop
				fixed
				placeholder
				titleStyle="color: #FFFFFF;">
			</u-navbar>
		</view>
		
        <view> test </view>
    </view>
</template>

<script>
export default {
    data() {
        return {};
    },
};
</script>

<style lang="scss">
.wrap {
    padding: 12px;
}

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
