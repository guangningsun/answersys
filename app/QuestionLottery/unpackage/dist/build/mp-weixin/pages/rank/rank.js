(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["pages/rank/rank"],{"16e6":function(n,t,a){"use strict";a.d(t,"b",(function(){return o})),a.d(t,"c",(function(){return r})),a.d(t,"a",(function(){return e}));var e={uNavbar:function(){return Promise.all([a.e("common/vendor"),a.e("uview-ui/components/u-navbar/u-navbar")]).then(a.bind(null,"3ce4"))}},o=function(){var n=this,t=n.$createElement;n._self._c},r=[]},"338f":function(n,t,a){},3485:function(n,t,a){"use strict";var e=a("338f"),o=a.n(e);o.a},3985:function(n,t,a){"use strict";(function(n){Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a={data:function(){return{avatarSrc:["../../static/ic_head_1.png","../../static/ic_head_2.png","../../static/ic_head_3.png","../../static/ic_head_4.png"],rankList:[]}},onLoad:function(){n.showLoading({title:"查询中..."}),this.requestWithMethod(getApp().globalData.get_rankinfo,"GET","",this.successCb,this.failCb,this.completeCb)},methods:{getRandomAvatar:function(){var n=Math.round(Math.random()*avatarSrc.length-1);return avatarSrc[n]},successCb:function(t){console.log("get_rankinfo success, rsp======"),console.log(t),n.hideLoading(),0===t.data.error&&(this.rankList=t.data.msg.rankList)},failPhoneCb:function(t){console.log("get_rankinfo failed",t),n.hideLoading()},completePhoneCb:function(n){}}};t.default=a}).call(this,a("543d")["default"])},4846:function(n,t,a){"use strict";a.r(t);var e=a("16e6"),o=a("85a4");for(var r in o)"default"!==r&&function(n){a.d(t,n,(function(){return o[n]}))}(r);a("3485");var i,c=a("f0c5"),u=Object(c["a"])(o["default"],e["b"],e["c"],!1,null,null,null,!1,e["a"],i);t["default"]=u.exports},"4fda":function(n,t,a){"use strict";(function(n){a("a49a");e(a("66fd"));var t=e(a("4846"));function e(n){return n&&n.__esModule?n:{default:n}}wx.__webpack_require_UNI_MP_PLUGIN__=a,n(t.default)}).call(this,a("543d")["createPage"])},"85a4":function(n,t,a){"use strict";a.r(t);var e=a("3985"),o=a.n(e);for(var r in e)"default"!==r&&function(n){a.d(t,n,(function(){return e[n]}))}(r);t["default"]=o.a}},[["4fda","common/runtime","common/vendor"]]]);