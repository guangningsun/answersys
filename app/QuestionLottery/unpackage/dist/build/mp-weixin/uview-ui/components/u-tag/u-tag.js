(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["uview-ui/components/u-tag/u-tag"],{"221c":function(t,n,i){"use strict";var e=i("4b08"),o=i.n(e);o.a},"4b08":function(t,n,i){},"68a7":function(t,n,i){"use strict";i.r(n);var e=i("80d3"),o=i.n(e);for(var r in e)"default"!==r&&function(t){i.d(n,t,(function(){return e[t]}))}(r);n["default"]=o.a},"80d3":function(t,n,i){"use strict";(function(t){Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var e=o(i("f1b6"));function o(t){return t&&t.__esModule?t:{default:t}}var r={name:"u-tag",mixins:[t.$u.mpMixin,t.$u.mixin,e.default],data:function(){return{}},computed:{style:function(){var t={};return this.bgColor&&(t.backgroundColor=this.bgColor),this.color&&(t.color=this.color),this.borderColor&&(t.borderColor=this.borderColor),t},textColor:function(){var t={};return this.color&&(t.color=this.color),t},imgStyle:function(){var t="large"===this.size?"17px":"medium"===this.size?"15px":"13px";return{width:t,height:t}},closeSize:function(){var t="large"===this.size?15:"medium"===this.size?13:12;return t},iconSize:function(){var t="large"===this.size?21:"medium"===this.size?19:16;return t},elIconColor:function(){return this.iconColor?this.iconColor:this.plain?this.type:"#ffffff"}},methods:{closeHandler:function(){this.$emit("close",this.name)},clickHandler:function(){this.$emit("click",this.name)}}};n.default=r}).call(this,i("543d")["default"])},"9d3a":function(t,n,i){"use strict";i.r(n);var e=i("b392"),o=i("68a7");for(var r in o)"default"!==r&&function(t){i.d(n,t,(function(){return o[t]}))}(r);i("221c");var u,c=i("f0c5"),l=Object(c["a"])(o["default"],e["b"],e["c"],!1,null,"7f5c83cc",null,!1,e["a"],u);n["default"]=l.exports},b392:function(t,n,i){"use strict";i.d(n,"b",(function(){return o})),i.d(n,"c",(function(){return r})),i.d(n,"a",(function(){return e}));var e={uTransition:function(){return Promise.all([i.e("common/vendor"),i.e("uview-ui/components/u-transition/u-transition")]).then(i.bind(null,"cd03"))},uIcon:function(){return Promise.all([i.e("common/vendor"),i.e("uview-ui/components/u-icon/u-icon")]).then(i.bind(null,"cbcd"))}},o=function(){var t=this,n=t.$createElement,i=(t._self._c,t.__get_style([{marginRight:t.closable?"10px":0,marginTop:t.closable?"10px":0},t.style])),e=t.icon?t.$u.test.image(t.icon):null,o=t.icon&&e?t.__get_style([t.imgStyle]):null,r=t.__get_style([t.textColor]);t.$mp.data=Object.assign({},{$root:{s0:i,g0:e,s1:o,s2:r}})},r=[]}}]);
;(global["webpackJsonp"] = global["webpackJsonp"] || []).push([
    'uview-ui/components/u-tag/u-tag-create-component',
    {
        'uview-ui/components/u-tag/u-tag-create-component':(function(module, exports, __webpack_require__){
            __webpack_require__('543d')['createComponent'](__webpack_require__("9d3a"))
        })
    },
    [['uview-ui/components/u-tag/u-tag-create-component']]
]);