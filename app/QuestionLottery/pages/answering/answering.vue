<template>
	<view class="u-page" style="padding-left: 20upx; padding-right: 20upx; height: 100%;">
		<u-navbar
			bgColor="#6141ea" 
			title="答题" 
			@rightClick="rightClick" 
			:autoBack="true"
			safeAreaInsetTop
			fixed
			placeholder
			titleStyle="color: #FFFFFF;">
		</u-navbar>

		<view class="u-demo-block" v-for="(item, index) in questionListShow" :key="index"  style="margin-top: 30upx; margin-bottom: 30upx; padding: 15upx; border-radius: 12upx; background-color: #FFFFFF;">
			<text class="title text-bold text-lg text-black">{{item.id}}. {{item.title}}</text>
			<view class="u-demo-block__content" style="margin-top: 20upx;">
				<view v-if=" item.type === '多选'" class="u-page__checkbox-item " >
					<u-checkbox-group
						v-model="answerRadioValue[item.id-1]"
						placement="column"
						@change="checkboxChange"
						activeColor="#6141ea"
					>
						<u-checkbox
							:customStyle="{marginBottom: '16px'}"
							v-for="(questionItem, index2) in item.chooseItems"
							:key="index2"
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
						activeColor="#6141ea"
					>
						<u-radio
							:customStyle="{marginBottom: '16px'}"
							v-for="(questionItem, index3) in item.chooseItems"
							:key="index3"
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
			color="#6141ea"
			style="margin-top: 50px;"
			@click="onSubmit"
		></u-button>
		
		<u-button
			v-if="questionListShow[0].id < questionList.length"
		    text="下一题"
		    size="normal"
			color="#6141ea"
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
				// questionList:[
				// 	{
				// 		id:1,
				// 		title:'问题问题标题',
				// 		type:'multi',
				// 		right_answer:['A','B','C'],
				// 		chooseItems:[
				// 			{
				// 				item_index:'A',
				// 				item_content:'选项A内容'
				// 			},
				// 			{
				// 				item_index:'B',
				// 				item_content:'选项B内容'
				// 			},
				// 			{
				// 				item_index:'C',
				// 				item_content:'选项C内容'
				// 			},
				// 			{
				// 				item_index:'D',
				// 				item_content:'选项D内容'
				// 			}
				// 		]
				// 	},
				// 	{
				// 		id:2,
				// 		title:'问题问题标题2222',
				// 		type:'single',
				// 		right_answer:['A'],
				// 		chooseItems:[
				// 			{
				// 				item_index:'A',
				// 				item_content:'选项A内容222'
				// 			},
				// 			{
				// 				item_index:'B',
				// 				item_content:'选项B内容222'
				// 			},
				// 			{
				// 				item_index:'C',
				// 				item_content:'选项C内容222'
				// 			},
				// 			{
				// 				item_index:'D',
				// 				item_content:'选项D内容222' 
				// 			}
				// 		]
				// 	},
				// ],

				
				questionList:[],
				
				questionListShow:[],
				
				answerRadioValue:[],
				
				currentQuestionId:1,
				
				answerWithPid:[]
			}
		},
		onLoad() {
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
				if(rsp.data.error === 0){
					this.questionList = rsp.data.msg.questionList
					this.questionListShow.length= 0
					this.questionListShow.push(this.questionList[0])
					console.log('questionListShow',this.questionListShow)
					this.currentQuestionId = this.questionListShow[0].pid
				}
				
			},
			failCb(err) {
				console.log('get_testpaperinfo failed', err);
			},
			completeCb(rsp) {},
			
			// ==================
			
			successSubmitCb(rsp) {
				console.log('submit_paper success, rsp======');
				console.log(rsp);
				if(rsp.data.error === 0){
					uni.navigateTo({
						url: '/pages/answer_finish/answer_finish'
					})
				}
				
			},
			failSubmitCb(err) {
				console.log('submit_paper failed', err);
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
				
				let item = this.questionListShow[0]
				
				let answerItem = {
					pid: this.currentQuestionId, 
					answer:this.answerRadioValue[item.id-1]
				}
				console.log('on onSubmit')
				console.log(answerItem)
				this.answerWithPid.push(answerItem)
				console.log(this.answerWithPid)
				
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
				
			}
		}
	}
</script>

<style>

</style>
