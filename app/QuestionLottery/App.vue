<script>
	export default {
		globalData: {
			
			domain_port: 'https://brilliantlife.com.cn:8020/',
			domain:'https://brilliantlife.com.cn:8020',
			image_prefix:'https://brilliantlife.com.cn:8020/media',
			
			// API 接口
			api_login: 'weixin_sns/',
			api_getWXInfo: 'weixin_gusi/',
			get_user_info:'get_user_info_by_wxid/',
			get_testpaperinfo:'get_testpaperinfo/',
			get_rankinfo:'get_rankinfo/',
			get_answer_result:'get_answer_result/',
			submit_paper:'submit_paper/',
			get_user_award_info:'get_user_award_info/',
			submit_user_info:'submit_user_info/',
			get_award_info:'get_award_info/',
			revice_award:'revice_award/',  //领取奖品，点击领取按钮触发
			register_user:'register_user/', 
			get_award_history:'get_award_history/',
			award_user_info_confirm:'award_user_info_confirm/', // 领取奖品前信息确认
			is_in_activity_time:'is_in_activity_time/',
			is_member:'is_member/',
			get_prize_info: 'get_prize_info/',
			get_rule_info: 'get_rule_info/',
			
			
			// key 值
			key_user_name:'key_user_name',
			key_user_auth:'key_user_auth',
			key_wx_openid:'key_wx_openid',
			key_user_head:'key_user_head',
			key_user_nickname:'key_user_nickname',
			key_phone_num:'key_phone_num' ,
			key_is_update:'key_is_update',
			key_apart:'key_apart',
			key_can_get_prize:'key_can_get_prize',
		},
			
		onLaunch: function() {
			console.warn('当前组件仅支持 uni_modules 目录结构 ，请升级 HBuilderX 到 3.1.0 版本以上！')
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style lang="scss">
	@import "uview-ui/index.scss";
	/*每个页面公共css */
	@import '@/uni_modules/uni-scss/index.scss';
	/* #ifndef APP-NVUE */
	@import '@/static/customicons.css';
	@import "colorui/main.css";
	@import "colorui/icon.css";
	// 设置整个项目的背景色
	page {
		background-color: #f5f5f5;
	}

	/* #endif */
	.example-info {
		font-size: 14px;
		color: #333;
		padding: 10px;
	}
	.nav-list {
		display: flex;
		flex-wrap: wrap;
		padding: 0px 40upx 0px;
		justify-content: space-between;
	}
	
	.nav-li {
		padding: 30upx;
		border-radius: 12upx;
		width: 45%;
		margin: 0 2.5% 40upx;
		background-image: url(https://cdn.nlark.com/yuque/0/2019/png/280374/1552996358352-assets/web-upload/cc3b1807-c684-4b83-8f80-80e5b8a6b975.png);
		background-size: cover;
		background-position: center;
		position: relative;
		z-index: 1;
	}
	
	.nav-li::after {
		content: "";
		position: absolute;
		z-index: -1;
		background-color: inherit;
		width: 100%;
		height: 100%;
		left: 0;
		bottom: -10%;
		border-radius: 10upx;
		opacity: 0.2;
		transform: scale(0.9, 0.9);
	}
	
	.nav-li.cur {
		color: #fff;
		background: rgb(94, 185, 94);
		box-shadow: 4upx 4upx 6upx rgba(94, 185, 94, 0.4);
	}
	
	.nav-title {
		font-size: 32upx;
		font-weight: 300;
	}
	
	.nav-title::first-letter {
		font-size: 40upx;
		margin-right: 4upx;
	}
	
	.nav-name {
		font-size: 28upx;
		text-transform: Capitalize;
		margin-top: 20upx;
		position: relative;
	}
	
	.nav-name::before {
		content: "";
		position: absolute;
		display: block;
		width: 40upx;
		height: 6upx;
		background: #fff;
		bottom: 0;
		right: 0;
		opacity: 0.5;
	}
	
	.nav-name::after {
		content: "";
		position: absolute;
		display: block;
		width: 100upx;
		height: 1px;
		background: #fff;
		bottom: 0;
		right: 40upx;
		opacity: 0.3;
	}
	
	.nav-name::first-letter {
		font-weight: bold;
		font-size: 36upx;
		margin-right: 1px;
	}
	
	.nav-li text {
		position: absolute;
		right: 30upx;
		top: 30upx;
		font-size: 52upx;
		width: 60upx;
		height: 60upx;
		text-align: center;
		line-height: 60upx;
	}
	
	.text-light {
		font-weight: 300;
	}
	
	@keyframes show {
		0% {
			transform: translateY(-50px);
		}
	
		60% {
			transform: translateY(40upx);
		}
	
		100% {
			transform: translateY(0px);
		}
	}
	
	@-webkit-keyframes show {
		0% {
			transform: translateY(-50px);
		}
	
		60% {
			transform: translateY(40upx);
		}
	
		100% {
			transform: translateY(0px);
		}
	}	
</style>
