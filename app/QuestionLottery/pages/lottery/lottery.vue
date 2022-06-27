<template>
	<view  class="u-page bg-gradual-blue2" 
	  style="background-image: url(../../static/lottery_bg.jpg); background-size:100% 100%; padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#8145e1"
			title="领取奖品" 
			:autoBack="false"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		<view style="margin-top: 120rpx; z-index: -1; padding-bottom: 600rpx;">
			<view style="font-size: 80upx;" class="text-wrapper text-orange text-bold text-center padding-bottom padding-top-sm">
				祝您好运
			</view>
			<LuckyWheel
				ref="myLucky"
				width="600rpx"
				height="600rpx"
				:blocks="blocks"
				:prizes="prizes"
				:buttons="buttons"
				:defaultStyle="defaultStyle"
				@start="startCallBack"
				@end="endCallBack"
			/>
			
			<view class="margin-top-xl">
				<u-button
				    text="返回"
				    size="normal"
					color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
					shape="circle"
					@click="goBackIndex"
				></u-button>
			</view>
		</view>
		
		<view class="cu-modal" :class="modalName=='prizeModal'?'show':''">
			<view class="cu-dialog" style="z-index: 10;">
				<view class="cu-bar bg-white justify-end">
					<view class="content">抽奖结果</view>
					<!-- <view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view> -->
				</view>
				<view v-show="!canLottery">
					<view class="bg-white text-wrapper text-lg text-orange text-bold text-center padding-bottom-sm padding-top-sm">
						已抽奖
					</view>
				</view>
				<view v-show="canLottery && prizeResult.id === -1">
					<view class="bg-white text-wrapper text-lg text-orange text-bold text-center padding-bottom-sm padding-top-sm">
						{{ prizeResult.name }}
					</view>
					<!-- <view class="bg-white text-wrapper text text-gray text text-center padding-bottom-sm padding-top-sm">
						下次继续努力
					</view> -->
				</view>
				<view v-show="canLottery && prizeResult.id !== -1">
					<view class="cu-item">
						<view class="flex cu-form-group">
							<view class="title text-orange">中奖物品</view>
							<view class="text-wrapper text-xxl text-red text-bold text-right padding-bottom-sm padding-top-sm">
								{{ prizeResult.name }}
							</view>
						</view>
						<view class="bg-white padding-top-lg padding-bottom-lg">
							<image :src=" prizeResult.img === null || prizeResult.img === undefined ? '../../static/default.png' : domain + '/media/'+ prizeResult.img "  style="width: 300upx; height: 300upx;" mode="aspectFit"></image>
						</view>
					</view>
				</view>
				
		
				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn lg bg-light-blue margin-left" @tap="onConfirm()">确认</button>
					</view>
					<!-- <view v-show="!canLottery" class="action">
						<button class="cu-btn lg bg-light-blue margin-left" @tap="onOK()">确认</button>
					</view> -->
				</view>
			</view>
		</view>
	</view>
</template>

<script>
import LuckyWheel from '@/components/@lucky-canvas/uni/lucky-wheel';
export default {
	components: { LuckyWheel },
	data() {
		return {
			domain: getApp().globalData.domain,
			modalName: null,
			canLottery: true,
			wheelVisible: true,
			prizeList: [
			  {
				id: 1,
				desc:'中奖了',
			  },
			  {
				id: 2,
				desc:'谢谢',
			  },
			  {
				id: 3,
				desc:'中奖了',
			  },
			  {
				id: 4,
				desc:'谢谢',
			  },
			],
			prizeResult: {},
			blocks: [{ padding: '13px', background: '#f4bc5c' }],
			prizes: [
				{ fonts: [{ text: '中奖了', top: '10%' }], background: '#ade4f1' },
				{ fonts: [{ text: '谢谢', top: '10%' }], background: '#e6fef3' },
				{ fonts: [{ text: '中奖了', top: '10%' }], background: '#ade4f1' },
				{ fonts: [{ text: '谢谢', top: '10%' }], background: '#e6fef3' }
			],
			buttons: [
				{ radius: '50px', background: '#75ceee' },
				{ radius: '45px', background: '#73c1ff' },
				{
					radius: '40px',
					background: '#3980f2',
					pointer: true,
					fonts: [{ text: '开始\n抽奖', top: '-20px', fontColor: '#fff' }]
				}
			]
		};
	},
	onLoad() {
		uni.showLoading({
			title:'正在加载...',
			mask:true
		})
		let params = {
			phone_number: uni.getStorageSync('key_phone_num'),
			apart_id: uni.getStorageSync('key_apart')
		};
		this.requestWithMethod(
			getApp().globalData.get_prize_info,
			'POST',
			params,
			this.successCb,
			this.failCb,
			this.completeCb
		);
	},
	methods: {
		showModal(e) {
			this.modalName = e;
		},
		hideModal(e) {
			this.modalName = null;
		},
		successCb(rsp) {
			console.log('get_prize_info success, rsp======');
			console.log(rsp);
			uni.hideLoading();
			if(rsp.data !== {}){
				this.prizeList = rsp.data.prize_info.prize_list
				this.prizeResult = rsp.data.prize_info.prize_result
				this.canLottery = rsp.data.prize_info.can_lottery === 0 ? false : true
				console.log('canLottery: ' + this.canLottery)
				
				this.prizes = []
				for (var i = 0; i < this.prizeList.length; i++) {
					let item = {}
					let fonts = []
					fonts.push({text:this.prizeList[i].desc, top: '10%'})
					item.fonts = fonts
					item.background = i % 2 === 0 ? '#e6fef3' : '#ade4f1'
					this.prizes.push(item)
				}
				console.log('mak res', this.prizes)
				console.log('mak res img', this.prizeResult)
			}
		},
		failCb(err) {
			console.log('get_answer_result failed', err);
			uni.hideLoading()
		},
		completeCb(rsp) {},
		// 点击抽奖按钮触发回调
		startCallBack() {
			// uni.setStorageSync(getApp().globalData.key_can_get_prize, true);
			
			// 先开始旋转
			this.$refs.myLucky.play();
			// 使用定时器来模拟请求接口
			setTimeout(() => {
				// 假设后端返回的中奖索引是0
				let index = this.prizeResult.id - 1;
				// 调用stop停止旋转并传递中奖索引
				this.$refs.myLucky.stop(index);
			}, 2000);
		},
		// 抽奖结束触发回调
		endCallBack(prize) {
			// 奖品详情
			console.log('makkk', prize);
			this.showModal('prizeModal')
		},
		onConfirm(){	
			this.hideModal()
			this.goBackIndex()
			// uni.navigateTo({
			// 	url: '../receive_info_check/receive_info_check'
			// })
		},
		onOK(){
			this.hideModal()
			this.goBackIndex()
		},
		goBackIndex(){
			uni.navigateTo({
				url:'../index/index'
			})
		},
		rightClick(){
			this.goBackIndex()
		}
	}
};
</script>

<style></style>
