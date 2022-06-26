<template>
	<view class="u-page" style="padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#5de992" 
			title="答题分析" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="u-demo-block" style="margin-top: 30upx; margin-bottom: 30supx; padding: 15upx; border-radius: 12upx; background-color: #f5fff0;">
			<view class="flex">
				<text class="title text-bold text-lg text-black">1、你比较喜欢下面哪个颜色？</text>
				<u-tag text="正确" type="success" icon="checkmark" plain plainFill></u-tag>
			</view>
			<view class="u-demo-block__content" style="margin-top: 20upx;">
				<view class="u-page__radio-item">
					<u-radio-group
						v-model="radiovalue5" 
						placement="column"
						activeColor="#5de992"
					>
						<u-radio
							:customStyle="{marginBottom: '8px'}"
							v-for="(item, index) in checkboxList5"
							:key="index"
							:label="item.name"
							:name="item.name"
						>
						</u-radio>
					</u-radio-group>
					<u-line></u-line>
					<view style="margin-top: 10upx;">您的答案: A B C</view>
					<view>正确答案: A B C</view>
				</view>
			</view>
		</view>
		
		<view class="u-demo-block" style="margin-top: 30upx; margin-bottom: 30supx; padding: 15upx; border-radius: 12upx; background-color: #fce4e4;">
			<view class="flex">
				<text class="title text-bold text-lg text-black">1、你比较喜欢下面哪个颜色？</text>
				<u-tag text="错误" type="error" icon="close" plain plainFill></u-tag>
			</view>
			<view class="u-demo-block__content" style="margin-top: 20upx;">
				<view class="u-page__radio-item">
					<u-radio-group
						v-model="radiovalue5" 
						placement="column"
						activeColor="#5de992"
					>
						<u-radio
							:customStyle="{marginBottom: '8px'}"
							v-for="(item, index) in checkboxList5"
							:key="index"
							:label="item.name"
							:name="item.name"
						>
						</u-radio>
					</u-radio-group>
					<u-line></u-line>
					<view style="margin-top: 10upx;">您的答案: A B C</view>
					<view>正确答案: A B C</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				radiovalue5: '绿色',
				
				//自定义颜色数据
				checkboxList5: [{
						name: '红色',
						disabled: false
					},
					{
						name: '黄色',
						disabled: false
					},
					{
						name: '绿色',
						disabled: false
					},
					{
						name: '蓝色',
						disabled: false
					}
				],
				// u-checkbox-group的v-model绑定的值如果设置为某个checkbox的name，就会被默认选中
				checkboxValue5: ['绿色'],
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
