(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["pages/award_choose/award_choose"],{"05e5":function(e,n,t){"use strict";t.d(n,"b",(function(){return a})),t.d(n,"c",(function(){return u})),t.d(n,"a",(function(){return o}));var o={uNavbar:function(){return Promise.all([t.e("common/vendor"),t.e("uview-ui/components/u-navbar/u-navbar")]).then(t.bind(null,"3ce4"))}},a=function(){var e=this,n=e.$createElement;e._self._c},u=[]},5242:function(e,n,t){"use strict";(function(e){t("a49a");o(t("66fd"));var n=o(t("853c"));function o(e){return e&&e.__esModule?e:{default:e}}wx.__webpack_require_UNI_MP_PLUGIN__=t,e(n.default)}).call(this,t("543d")["createPage"])},"853c":function(e,n,t){"use strict";t.r(n);var o=t("05e5"),a=t("eff5");for(var u in a)"default"!==u&&function(e){t.d(n,e,(function(){return a[e]}))}(u);var r,c=t("f0c5"),i=Object(c["a"])(a["default"],o["b"],o["c"],!1,null,null,null,!1,o["a"],r);n["default"]=i.exports},e027:function(e,n,t){"use strict";(function(e){Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var t={data:function(){return{awardInfo:[]}},onLoad:function(){var n={phone_number:e.getStorageSync("key_phone_num")};this.requestWithMethod(getApp().globalData.get_award_info,"POST",n,this.successCb,this.failCb,this.completeCb)},methods:{successCb:function(e){console.log("get_award_info success, rsp======"),console.log(e),e.data.error},failPhoneCb:function(e){console.log("get_award_info failed",e)},completePhoneCb:function(e){}}};n.default=t}).call(this,t("543d")["default"])},eff5:function(e,n,t){"use strict";t.r(n);var o=t("e027"),a=t.n(o);for(var u in o)"default"!==u&&function(e){t.d(n,e,(function(){return o[e]}))}(u);n["default"]=a.a}},[["5242","common/runtime","common/vendor"]]]);