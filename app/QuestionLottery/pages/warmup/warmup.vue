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
				
			questionList:[
				{
					chooseItems:[
						{
							item_content:'A.企业',
							item_index: "A",
						},
						{
							item_content: "B.用人单位",
							item_index: "B"
						},{
							item_content: "C.劳动者",
							item_index: "C"
						},{
							item_content: "D.用人单位和劳动者",
							item_index: "D"
						},
					],
					id: 1,
					pid: 12,
					right_answer:["B","C"],
					title: "《劳动合同法》的立法宗旨是：完善劳动合同制度，明确劳动合同双方当事人的权利和义务，保护（）的合法权益，构建和发展和谐稳定的劳动关系。",
					type: "多选"
				},
				{
					chooseItems:[
						{
							item_content: "A.人民民主",
							item_index: "A"
						},
						{
							item_content: "B.全面小康",
							item_index: "B"
						},{
							item_content: "C.美好生活",
							item_index: "C"
						}
					],
					id: 2,
					pid: 13,
					right_answer:[ "A", "B", "C"],
					title: "2021年11月11日，中国共产党第十九届中央委员会第六次全体会议通过了《中共中央关于党的百年奋斗重大成就和历史经验的决议》。决议指出，一百年来，党领导人民经过波澜壮阔的伟大斗争，中国人民彻底摆脱了被欺负、被压迫、被奴役的命运，成为国家、社会和自己命运的主人，（_______）不断发展，十四亿多人口实现（_______），中国人民对（_______）的向往不断变为现实。",
					type: "多选"
				},
				{
					chooseItems:[
						{
							item_content: "A.第一个百年奋斗目标",
							item_index: "A"
						},
						{
							item_content: "B.迈出新步伐",
							item_index: "B"
						},{
							item_content: "C.取得新成效",
							item_index: "C"
						},{
							item_content: "D.良好开局",
							item_index: "D"
						}
					],
					id: 3,
					pid: 14,
					right_answer:[ "A", "B", "C","D"],
					title: "2021年12月8日至10日，中央经济工作会议在北京举行。会议认为，今年是党和国家历史上具有里程碑意义的一年。我们隆重庆祝中国共产党成立一百周年，实现（_____________），开启向第二个百年奋斗目标进军新征程，沉着应对百年变局和世纪疫情，构建新发展格局（____________），高质量发展（___________），实现了“十四五”（__________）。",
					type: "多选"
				},
				{
					chooseItems:[
						{
							item_content: "A.政治原则",
							item_index: "A"
						},
						{
							item_content: "B.根本保证",
							item_index: "B"
						}
					],
					id: 4,
					pid: 15,
					right_answer:[ "A", "B"],
					title: "坚持党对工会工作的领导，是习近平总书记关于工人阶级和工会工作的重要论述的关键，是做好工会工作的（________）和（________）",
					type: "多选"
				},
				{
					chooseItems:[
						{
							item_content: "A.开放",
							item_index: "A"
						},
						{
							item_content: "B.开拓",
							item_index: "B"
						},
						{
							item_content: "C.求新",
							item_index: "C"
						},
						{
							item_content: "D求实",
							item_index: "D"
						}
					],
					id: 5,
					pid: 16,
					right_answer:[ "A", "B","C","D"],
					title: "1996年4月，开发区工委、管委会确定“泰达精神”内涵。在2021年初工作会上，经开区党委书记、管委会主任尤天成同志讲：要将“（_____）（_____），励精图大业；（_____）（_____），众志建新城”的泰达精神融入每一名泰达人的血液，接续不畏难的勇气，不怕苦的意志，不服输的志气，激励全体泰达人不忘初心、砥砺前行。",
					type: "多选"
				}
				],
				
				questionListShow:[],
				
				answerRadioValue:[],
				
				currentQuestionId:1,
				
				answerWithPid:[]
			}
		},
		onLoad() {
			this.questionListShow.length= 0
			this.questionListShow.push(this.questionList[0])
			console.log('questionListShow',this.questionListShow)
			this.currentQuestionId = this.questionListShow[0].pid
		},
		methods: {
			// showToast(params) {
			// 	this.$refs.uToast.show({
			// 		...params,
			// 		complete() {
			// 			params.url && uni.navigateTo({
			// 				url: params.url
			// 			})
			// 		}
			// 	})
			// },
			
			checkboxChange(ans) {
				console.log('change', ans);
				
				console.log('currentPid',this.currentQuestionId)
			},
			
			onSubmit(){
				
				
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
				
				console.log('finish warm up')
				let par = {
					message: '完成热身',
					url: '../index/index'
				}
				uni.showToast({
					title:"完成热身",
				})
				setTimeout(() => {
					uni.navigateTo({
						url:'../index/index'
					})
				}, 1000)
				
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
