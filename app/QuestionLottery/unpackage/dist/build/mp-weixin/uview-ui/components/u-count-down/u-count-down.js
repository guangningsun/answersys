(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["uview-ui/components/u-count-down/u-count-down"],{"15cc":function(t,i,e){"use strict";var n=e("a41d"),a=e.n(n);a.a},"51ea":function(t,i,e){"use strict";var n;e.d(i,"b",(function(){return a})),e.d(i,"c",(function(){return r})),e.d(i,"a",(function(){return n}));var a=function(){var t=this,i=t.$createElement;t._self._c},r=[]},9034:function(t,i,e){"use strict";e.r(i);var n=e("f564"),a=e.n(n);for(var r in n)"default"!==r&&function(t){e.d(i,t,(function(){return n[t]}))}(r);i["default"]=a.a},"9d9b":function(t,i,e){"use strict";e.r(i);var n=e("51ea"),a=e("9034");for(var r in a)"default"!==r&&function(t){e.d(i,t,(function(){return a[t]}))}(r);e("15cc");var u,o=e("f0c5"),c=Object(o["a"])(a["default"],n["b"],n["c"],!1,null,"678a406b",null,!1,n["a"],u);i["default"]=c.exports},a41d:function(t,i,e){},f564:function(t,i,e){"use strict";(function(t){Object.defineProperty(i,"__esModule",{value:!0}),i.default=void 0;var n=r(e("083d")),a=e("d5ad");function r(t){return t&&t.__esModule?t:{default:t}}var u={name:"u-count-down",mixins:[t.$u.mpMixin,t.$u.mixin,n.default],data:function(){return{timer:null,timeData:(0,a.parseTimeData)(0),formattedTime:"0",runing:!1,endTime:0,remainTime:0}},watch:{time:function(t){this.reset()}},mounted:function(){this.init()},methods:{init:function(){this.reset()},start:function(){this.runing||(this.runing=!0,this.endTime=Date.now()+this.remainTime,this.toTick())},toTick:function(){this.millisecond?this.microTick():this.macroTick()},macroTick:function(){var t=this;this.clearTimeout(),this.timer=setTimeout((function(){var i=t.getRemainTime();(0,a.isSameSecond)(i,t.remainTime)&&0!==i||t.setRemainTime(i),0!==t.remainTime&&t.macroTick()}),30)},microTick:function(){var t=this;this.clearTimeout(),this.timer=setTimeout((function(){t.setRemainTime(t.getRemainTime()),0!==t.remainTime&&t.microTick()}),50)},getRemainTime:function(){return Math.max(this.endTime-Date.now(),0)},setRemainTime:function(t){this.remainTime=t;var i=(0,a.parseTimeData)(t);this.$emit("change",i),this.formattedTime=(0,a.parseFormat)(this.format,i),t<=0&&(this.pause(),this.$emit("finish"))},reset:function(){this.pause(),this.remainTime=this.time,this.setRemainTime(this.remainTime),this.autoStart&&this.start()},pause:function(){this.runing=!1,this.clearTimeout()},clearTimeout:function(t){function i(){return t.apply(this,arguments)}return i.toString=function(){return t.toString()},i}((function(){clearTimeout(this.timer),this.timer=null}))},beforeDestroy:function(){this.clearTimeout()}};i.default=u}).call(this,e("543d")["default"])}}]);
;(global["webpackJsonp"] = global["webpackJsonp"] || []).push([
    'uview-ui/components/u-count-down/u-count-down-create-component',
    {
        'uview-ui/components/u-count-down/u-count-down-create-component':(function(module, exports, __webpack_require__){
            __webpack_require__('543d')['createComponent'](__webpack_require__("9d9b"))
        })
    },
    [['uview-ui/components/u-count-down/u-count-down-create-component']]
]);
