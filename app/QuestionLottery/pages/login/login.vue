<template>
	<view class="u-page" style="background-color: #FFFFFF; height: 1600rpx">
		<u-navbar
			bgColor="#6141ea" 
			title="登录" 
			@rightClick="rightClick" 
			:autoBack="true"
			titleStyle="color: #FFFFFF;">
		</u-navbar>
		
		<image mode='aspectFit' style="width: 800rpx" src="../../static/login_bg.png" ></image>

		<view class="u-demo-block">
			<view class="flex">
				<u-icon label="验证码" size="18" name="../../static/ic_verify_code.png"></u-icon>
				
			</view>
				
				<view
					class="u-demo-block__content"
					style="margin-top: 15px;"
				>
					<!-- 注意：由于兼容性差异，如果需要使用前后插槽，nvue下需使用u--input，非nvue下需使用u-input -->
					<!-- #ifndef APP-NVUE -->
					<u-input placeholder="请填写短信验证码" border="surround" shape="circle">
					<!-- #endif -->
					<!-- #ifdef APP-NVUE -->
					<u--input placeholder="请填写短信验证码" border="surround" shape="circle">
					<!-- #endif -->
						<template slot="suffix">
							<u-code
								ref="uCode"
								@change="codeChange"
								seconds="20"
								changeText="X秒重新获取"
							></u-code>
							<u-button
								@tap="getCode"
								:text="tips"
								type="success"
								size="mini"
								shape="circle"
								color="#4600c3"
							></u-button>
						</template>
					<!-- #ifndef APP-NVUE -->
					</u-input>
					<!-- #endif -->
					<!-- #ifdef APP-NVUE -->
					</u--input>
					<!-- #endif -->
				</view>
			</view>

		</view>
	
		
		
		<!-- 顶部文字 -->
		<!-- <text class="title">用户名密码登录</text> -->
		<!-- <input class="input-box" :inputBorder="false" v-model="username" placeholder="请输入手机号/用户名"></input> -->
		<!-- <input type="password" class="input-box" :inputBorder="false" v-model="password" placeholder="请输入密码"></input> -->
		<!-- <button class="send-btn" :disabled="!canLogin" :type="canLogin?'primary':'default'" -->
			<!-- @click="pwdLogin">登录</button> -->
		<!-- 忘记密码 -->
		<!-- <view class="auth-box"> -->
			<!-- <text class="link" @click="toRetrievePwd">忘记密码</text> -->
			<!-- <text class="link" @click="toRegister">注册账号</text> -->
		<!-- </view> -->
		<!-- <uni-quick-login :agree="agree" ref="uniQuickLogin"></uni-quick-login> -->

</template>

<script>
  export default {
    data() {
      return {
        tips: '',
        value: ''
      }
    },
    watch: {
      value(newValue, oldValue) {
        // console.log('v-model', newValue);
      }
    },
    methods: {
      codeChange(text) {
        this.tips = text;
      },
      getCode() {
        if (this.$refs.uCode.canGetCode) {
          // 模拟向后端请求验证码
          uni.showLoading({
            title: '正在获取验证码'
          })
          setTimeout(() => {
            uni.hideLoading();
            // 这里此提示会被this.start()方法中的提示覆盖
            uni.$u.toast('验证码已发送');
            // 通知验证码组件内部开始倒计时
            this.$refs.uCode.start();
          }, 2000);
        } else {
          uni.$u.toast('倒计时结束后再发送');
        }
      },
      change(e) {
        console.log('change', e);
      }
    }
  }
</script>

<style lang="scss">
	.u-page {
		&__button-item {
			margin: 0 15px 15px 0;
		}
	}
	.u-demo-block {
		margin-left: 15px;
		margin-right: 15px;
	}
	.u-demo-block__title {
		font-size: 15px;
	}
	.u-demo-block__content {
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
		margin-top: 15px;
		margin-bottom: 15px;
	}
</style>
