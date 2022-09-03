<template>
	<view class="u-page" style="padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#8145e1"
			title="答题" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<view class="u-demo-block__content countdownBlock">
			<u-count-down
			    :time="15 * 60 * 1000"
			    format="HH:mm:ss"
			    autoStart
			    millisecond
			    @change="onChange"
				@finish="finish"
			>
				<view class="time">
					<view class="time__custom">
						<text class="time__custom__item">{{ timeData.hours>10?timeData.hours:'0'+timeData.hours}}</text>
					</view>
					<text class="time__doc">:</text>
					<view class="time__custom">
						<text class="time__custom__item">{{ timeData.minutes === 0 ? '00' : timeData.minutes }}</text>
					</view>
					<text class="time__doc">:</text>
					<view class="time__custom">
						<text class="time__custom__item">{{ timeData.seconds === 0 ? '00' : timeData.seconds }}</text>
					</view>
				</view>
			</u-count-down>
		</view>

		<view class="u-demo-block" v-for="(item, index) in questionListShow" :key="index"  style="margin-top: 30upx; margin-bottom: 30upx; padding: 15upx; border-radius: 12upx; background-color: #FFFFFF;">
			<view class="flex" style="margin-top: 5upx; margin-bottom: 5upx;">
				<u-tag :text="item.type === '多选'? '多选题' :'单选题'" :type="item.type === '多选'? 'warning' : 'success'" plain plainFill style="width: 60upx;"></u-tag>
				<text class="title text-bold text-lg text-black" style="margin-left: 30upx;"></text>
				<u--text type="info" :text="'第'+(item.id)+'题，共'+questionList.length+'题'" style="margin-left: 10upx;"></u--text>
			</view>
			<text class="title text-bold text-lg text-black">{{item.id}}. {{item.title}}</text>
			<view class="u-demo-block__content" style="margin-top: 20upx;">
				<view v-if=" item.type === '多选'" class="u-page__checkbox-item " >
					<u-checkbox-group
						v-model="answerRadioValue[item.id-1]"
						placement="column"
						@change="checkboxChange"
						:borderBottom="true"
						activeColor="#8145e1"
						iconPlacement="right"
					>
						<u-checkbox
							:customStyle="{ paddingBottom: '10px', paddingTop: '10px', paddingRight: '15px', paddingLeft:'15px'}"
							v-for="(questionItem, index2) in item.chooseItems"
							:key="index2"
							labelSize='18px'
							:label="questionItem.item_content"
							:name="questionItem.item_index"
						> 
						</u-checkbox>
					</u-checkbox-group>
				</view>
				
				<view v-if=" item.type === '单选'" class="u-page__radio-item " >
					<u-radio-group
						v-model="answerRadioValue[item.id-1]"
						placement="column"
						:borderBottom="true"
						activeColor="#8145e1"
						iconPlacement="right"
					>
						<u-radio
							:customStyle="{paddingBottom: '10px', paddingTop: '10px', paddingRight: '15px', paddingLeft:'15px'}"
							v-for="(questionItem, index3) in item.chooseItems"
							:key="index3"
							labelSize='18px'
							:label="questionItem.item_content"
							:name="questionItem.item_index"
						>
						</u-radio>
					</u-radio-group>
				</view>
			</view>
		</view>
		
		<u-button
			v-if="questionListShow[0].id === questionList.length"
		    text="提交"
		    size="normal"
			color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
			style="margin-top: 50px;"
			@click="onSubmit"
		></u-button>
		
		<u-button
			v-if="questionListShow[0].id < questionList.length"
		    text="下一题"
		    size="normal"
			color="linear-gradient(to right, rgb(124, 72, 212), rgb(154, 94, 219))"
			style="margin-top: 50px;"
			:disabled="answerRadioValue[questionListShow[0].id-1] === undefined || answerRadioValue[questionListShow[0].id-1] === '' "
			@click="onNext"
		></u-button>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				
				questionList:[],
				
				questionListShow:[],
				
				answerRadioValue:[],
				
				currentQuestionId:1,
				
				answerWithPid:[],
				
				timeData: {},
				
				isClickSubmit: false
			}
		},
		onLoad() {
			uni.showLoading({
				title:'正在加载...',
				mask:true
			})
			this.requestWithMethod(
				getApp().globalData.get_testpaperinfo,
				'GET',
				'',
				this.successCb,
				this.failCb,
				this.completeCb
			);
		},
		methods: {
			successCb(rsp) {
				console.log('get_testpaperinfo success, rsp======');
				console.log(rsp);
				uni.hideLoading()
				if(rsp.data.error === 0){
					this.questionList = rsp.data.msg.questionList
					this.questionListShow.length= 0
					this.questionListShow.push(this.questionList[0])
					console.log('questionListShow',this.questionListShow)
					this.currentQuestionId = this.questionListShow[0].pid
				}
				
			},
			failCb(err) {
				uni.hideLoading()
				console.log('get_testpaperinfo failed', err);
			},
			completeCb(rsp) {},
			
			// ==================
			
			successSubmitCb(rsp) {
				console.log('submit_paper success, rsp======');
				console.log(rsp);
				uni.hideLoading()
				if(rsp.data.error === 0){
					console.log('nnnn')
					uni.navigateTo({
						url: '../answer_finish/answer_finish'
					})
				}
				
			},
			failSubmitCb(err) {
				console.log('submit_paper failed', err);
				uni.hideLoading()
			},
			completeSubmitCb(rsp) {},
			
			// =================
			
			checkboxChange(ans) {
				console.log('change', ans);
				
				console.log('currentPid',this.currentQuestionId)
			},
			
			onSubmit(){
				console.log('get result')
				console.log(this.answerRadioValue)
				
				this.isClickSubmit = true
				
				uni.showLoading({
					title: '正在提交....',
					mask:true
				});
				
				if(this.answerWithPid.length < this.questionList.length){
					let item = this.questionListShow[0]
					
					let answerItem = {
						pid: this.currentQuestionId, 
						answer:this.answerRadioValue[item.id-1]
					}
					console.log('on onSubmit')
					console.log(answerItem)
					this.answerWithPid.push(answerItem)
					console.log(this.answerWithPid)
				}
				
				let params = {
					phone_number: uni.getStorageSync('key_phone_num'),
					answers: JSON.stringify(this.answerWithPid)
				}
				
				console.log('sub params')
				console.log(params)
				
				this.requestWithMethod(
					getApp().globalData.submit_paper,
					'POST',
					params,
					this.successSubmitCb,
					this.failSubmitCb,
					this.completeSubmitCb
				);
			},
			onNext(){
				console.log('on next')
				console.log(this.questionListShow)
				let item = this.questionListShow.pop()
				console.log(this.answerRadioValue)
				
				let answerItem = {
					pid: this.currentQuestionId, 
					answer:this.answerRadioValue[item.id-1]
				}
				console.log('on next000')
				console.log(answerItem)
				this.answerWithPid.push(answerItem)
				console.log(this.answerWithPid)
				
				this.questionListShow.length= 0
				this.questionListShow.push(this.questionList[item.id])
				this.currentQuestionId = this.questionListShow[0].pid
				
			},
			onChange(e) {
				this.timeData = e
			},
			finish() {
				// 时间结束，自动提交
				if (!this.isClickSubmit) {
					console.log('时间结束，自动提交')
					this.onSubmit()
				}
			}
		}
	}
</script>

<style lang="scss">
	.u-page {
		
	}
	.countdownBlock{
		margin-top: 10px
	}

	.time {
		@include flex;
		align-items: center;

		&__custom {
			margin-top: 4px;
			width: 22px;
			height: 22px;
			background-color: #fea747;
			border-radius: 4px;
			/* #ifndef APP-NVUE */
			display: flex;
			/* #endif */
			justify-content: center;
			align-items: center;

			&__item {
				color: #fff;
				font-size: 12px;
				text-align: center;
			}
		}

		&__doc {
			color: $u-primary;
			padding: 0px 4px;
		}

		&__item {
			color: #606266;
			font-size: 15px;
			margin-right: 4px;
		}
	}

	.u-view {
		padding: 40px 20px 0px 20px;

		&__title {
			font-size: 14px;
			color: rgb(143, 156, 162);
			margin-bottom: 10px;
		}
	}

	// 手动控制的btn样式
	.count-down {
		&__grid-item {
			width: 70px;
			height: 70px;
			@include flex;
			justify-content: center;
			align-items: center;

			&__circle {
				width: 32px;
				height: 32px;
				border-radius: 32px;
				background-color: $u-primary;
				/* #ifndef APP-NVUE */
				display: flex;
				/* #endif */
				justify-content: center;
				align-items: center;
				box-shadow: 1px 1px 4px rgba(155, 191, 255, .7);
			}

			&__grid-text {
				font-size: 14px;
				color: #909399;
				/* #ifndef APP-PLUS */
				box-sizing: border-box;
				/* #endif */
				margin-left: 6px;
			}
		}
	}
</style>
