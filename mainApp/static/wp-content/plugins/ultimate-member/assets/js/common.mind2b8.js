"object"!=typeof window.UM&&(window.UM={}),"object"!=typeof UM.common&&(UM.common={}),UM.common={tipsy:{init:function(){"function"==typeof jQuery.fn.tipsy&&(jQuery(".um-tip-n").tipsy({gravity:"n",opacity:1,live:"a.live",offset:3}),jQuery(".um-tip-w").tipsy({gravity:"w",opacity:1,live:"a.live",offset:3}),jQuery(".um-tip-e").tipsy({gravity:"e",opacity:1,live:"a.live",offset:3}),jQuery(".um-tip-s").tipsy({gravity:"s",opacity:1,live:"a.live",offset:3}))},hide:function(){"function"==typeof jQuery.fn.tipsy&&(jQuery(".um-tip-n").tipsy("hide"),jQuery(".um-tip-w").tipsy("hide"),jQuery(".um-tip-e").tipsy("hide"),jQuery(".um-tip-s").tipsy("hide"),jQuery(".um .tipsy").remove())}},datetimePicker:{init:function(){jQuery(".um-datepicker:not(.picker__input)").each(function(){e=void 0!==(elem=jQuery(this)).attr("data-disabled_weekdays")&&""!=elem.attr("data-disabled_weekdays")&&JSON.parse(elem.attr("data-disabled_weekdays"));var e,t=null,i=(void 0!==elem.attr("data-years")&&(t=elem.attr("data-years")),elem.attr("data-date_min")),a=elem.attr("data-date_max"),n=[],o=[],i=(void 0!==i&&(n=i.split(",")),void 0!==a&&(o=a.split(",")),n.length?new Date(n):null),a=n.length?new Date(o):null,o=(i&&"Invalid Date"==i.toString()&&3==n.length&&(n=n[1]+"/"+n[2]+"/"+n[0],i=new Date(Date.parse(n))),a&&"Invalid Date"==a.toString()&&3==o.length&&(n=o[1]+"/"+o[2]+"/"+o[0],a=new Date(Date.parse(n))),{disable:e,format:elem.attr("data-format"),formatSubmit:"yyyy/mm/dd",hiddenName:!0,onOpen:function(){elem.blur(),elem.parents("body").hasClass("wp-admin")&&elem.siblings(".picker").find(".picker__button--close").addClass("button")},onClose:function(){elem.blur()}});null!==t&&(o.selectYears=t),null!==i&&(o.min=i),null!==a&&(o.max=a),elem.pickadate(o)}),jQuery(".um-timepicker:not(.picker__input)").each(function(){(elem=jQuery(this)).pickatime({format:elem.attr("data-format"),interval:parseInt(elem.attr("data-intervals")),formatSubmit:"HH:i",hiddenName:!0,onOpen:function(){elem.blur()},onClose:function(){elem.blur()}})})}},select:{isSelected:function(e,t){return e===t?' selected="selected"':""}},form:{vanillaSerialize:function(e){var t,i,e=document.querySelector("#"+e),a={};for([t,i]of new FormData(e))void 0!==a[t]?(Array.isArray(a[t])||(a[t]=[a[t]]),a[t].push(i)):a[t]=i;return a}}},jQuery(document).on("ajaxStart",function(){UM.common.tipsy.hide()}),jQuery(document).on("ajaxSuccess",function(){UM.common.tipsy.init()}),jQuery(document).ready(function(){UM.common.tipsy.init(),UM.common.datetimePicker.init()});