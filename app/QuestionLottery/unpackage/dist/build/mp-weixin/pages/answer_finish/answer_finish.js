(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["pages/answer_finish/answer_finish"],{"0ab5":function(n,e,t){"use strict";t.r(e);var u=t("c225"),o=t("485d");for(var r in o)"default"!==r&&function(n){t.d(e,n,(function(){return o[n]}))}(r);var a,c=t("f0c5"),s=Object(c["a"])(o["default"],u["b"],u["c"],!1,null,null,null,!1,u["a"],a);e["default"]=s.exports},"485d":function(n,e,t){"use strict";t.r(e);var u=t("4dbf"),o=t.n(u);for(var r in u)"default"!==r&&function(n){t.d(e,n,(function(){return u[n]}))}(r);e["default"]=o.a},"4dbf":function(n,e,t){"use strict";(function(n){Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var t={data:function(){return{full:"恭喜您获得满分！您有机会获选择会员日普惠商品一件",fullNoRemain:"恭喜您获得满分！活动火热，普惠商品已被领空，请明日在来",noFull:"非满分提示”您未全部答对！再来一次，祝您好运！",answerResult:{score:100,hint:"提示语提示语提示语提示语提示语提示语提示语提示语提示语",remain:10}}},onLoad:function(){var e={phone_number:n.getStorageSync("key_phone_num")};this.requestWithMethod(getApp().globalData.get_answer_result,"POST",e,this.successCb,this.failCb,this.completeCb)},methods:{onChooseItem:function(){},onRetry:function(){},successCb:function(n){console.log("get_answer_result success, rsp======"),console.log(n),0===n.data.error&&(this.answerResult=n.data.msg.answer_result)},failPhoneCb:function(n){console.log("get_answer_result failed",n)},completePhoneCb:function(n){}}};e.default=t}).call(this,t("543d")["default"])},b1e3:function(n,e,t){"use strict";(function(n){t("a49a");u(t("66fd"));var e=u(t("0ab5"));function u(n){return n&&n.__esModule?n:{default:n}}wx.__webpack_require_UNI_MP_PLUGIN__=t,n(e.default)}).call(this,t("543d")["createPage"])},c225:function(n,e,t){"use strict";t.d(e,"b",(function(){return o})),t.d(e,"c",(function(){return r})),t.d(e,"a",(function(){return u}));var u={uNavbar:function(){return Promise.all([t.e("common/vendor"),t.e("uview-ui/components/u-navbar/u-navbar")]).then(t.bind(null,"3ce4"))},uButton:function(){return Promise.all([t.e("common/vendor"),t.e("uview-ui/components/u-button/u-button")]).then(t.bind(null,"476d"))}},o=function(){var n=this,e=n.$createElement;n._self._c},r=[]}},[["b1e3","common/runtime","common/vendor"]]]);