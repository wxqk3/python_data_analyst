# -*- coding:utf8 -*-
from lxml import etree
import requests

html='''
<html lang="cn" xmlns:og="http://ogp.me/ns#" class=" js flexbox no-touch csstransitions"><!--<![endif]--><head><style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><script type="text/javascript" async="" src="//munchkin.marketo.net/155/munchkin.js"></script><script async="" src="//amplify.outbrain.com/cp/obtp.js" type="text/javascript"></script><script type="text/javascript" async="" src="https://pixel.mathtag.com/event/js?mt_id=1135071&amp;mt_adid=181986&amp;v1=&amp;v2=&amp;v3=&amp;s3=&amp;s1=https%3A%2F%2Fwww.appannie.com%2Fapps%2Fios%2Fapp%2Fidle-heroes%2Freviews%2F%3Forder_by%3Ddate%26order_type%3Ddesc%26date%3D2019-04-29~2019-05-29%26translate_selected%3Dfalse%26granularity%3Dweekly%26stack%26percent%3Dfalse%26series%3Drating_star_1%2Crating_star_2%2Crating_star_3%2Crating_star_4%2Crating_star_5&amp;s2=%E6%94%BE%E7%BD%AE%E5%A5%87%E5%85%B5%20-%E5%85%A8%E7%90%83%E5%90%8C%E6%9C%8D%E6%94%BE%E7%BD%AE%E7%B1%BB%E6%B8%B8%E6%88%8F%20-%20iOS%20Store%20App%20Store%20%E8%AF%84%E8%AE%BA%20%7C%20App%20Annie"></script><script async="" src="//px.airpr.com/airpr.js"></script><script src="https://connect.facebook.net/signals/plugins/inferredEvents.js?v=2.8.47" async=""></script><script src="https://connect.facebook.net/signals/config/680989378664200?v=2.8.47&amp;r=stable" async=""></script><script async="" src="https://connect.facebook.net/en_US/fbevents.js"></script><script type="text/javascript" async="" src="https://cdn.walkme.com/users/440e9852f2724fafb2d968494f028e77/walkme_440e9852f2724fafb2d968494f028e77_https.js"></script><script type="text/javascript" async="" src="https://stats.g.doubleclick.net/dc.js"></script><script type="text/javascript" async="" src="//www.googleadservices.com/pagead/conversion_async.js"></script><script type="text/javascript" async="" src="//www.googleadservices.com/pagead/conversion_async.js"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://sjs.bizographics.com/insight.min.js"></script><script type="text/javascript" async="" src="https://cdn.heapanalytics.com/js/heap-3646280627.js"></script><script type="text/javascript" src="https://bam.nr-data.net/1/8c32ed8b53?a=2163096&amp;v=1123.df1c7f8&amp;to=ZwdbZkpZXENVWxZbDF5Nf0dWW0ZZW1ZNRQZSA1dTVEFGWVdLTEUGUkxLV05RV0caSgdEClUVSgh/XVxVRlEBYAZGC1xFblFXRxpfB0Y%3D&amp;rst=2159&amp;ref=https://www.appannie.com/apps/ios/app/idle-heroes/reviews/&amp;qt=4&amp;ap=866&amp;be=1323&amp;fe=1695&amp;dc=1680&amp;af=err,xhr,stn,ins,spa&amp;perf=%7B%22timing%22:%7B%22of%22:1559256388869,%22n%22:0,%22f%22:0,%22dn%22:2,%22dne%22:66,%22c%22:66,%22s%22:130,%22ce%22:269,%22rq%22:269,%22rp%22:1302,%22rpe%22:1580,%22dl%22:1320,%22di%22:1681,%22ds%22:1681,%22de%22:1693,%22dc%22:1694,%22l%22:1694,%22le%22:1699%7D,%22navigation%22:%7B%7D%7D&amp;jsonp=NREUM.setToken"></script><script async="" src="//www.googletagmanager.com/gtm.js?id=GTM-D44H&amp;l=dataLayer_D44H"></script><script src="https://js-agent.newrelic.com/nr-spa-1123.min.js"></script><script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={xpid:"VwcPUFJXGwEBUlJSDgc="};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{s.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(23),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,s){try{p?p-=1:o(s||new UncaughtException(t,e,n),!0)}catch(f){try{i("ierr",[f,c.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t,e){var n=e?null:c.now();i("err",[t,n])}var i=t("handle"),a=t(24),s=t("ee"),c=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError",p=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(13),t(12),"addEventListener"in window&&t(6),c.xhrWrappable&&t(14),d=!0)}s.on("fn-start",function(t,e,n){d&&(p+=1)}),s.on("fn-err",function(t,e,n){d&&!n[l]&&(f(n,l,function(){return!0}),this.thrown=!0,o(n))}),s.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),s.on("internal-error",function(t){i("ierr",[t,c.now(),!0])})},{}],3:[function(t,e,n){t("loader").features.ins=!0},{}],4:[function(t,e,n){function r(){M++,j=y.hash,this[u]=x.now()}function o(){M--,y.hash!==j&&i(0,!0);var t=x.now();this[h]=~~this[h]+t-this[u],this[d]=t}function i(t,e){E.emit("newURL",[""+y,e])}function a(t,e){t.on(e,function(){this[e]=x.now()})}var s="-start",c="-end",f="-body",u="fn"+s,d="fn"+c,l="cb"+s,p="cb"+c,h="jsTime",m="fetch",v="addEventListener",w=window,y=w.location,x=t("loader");if(w[v]&&x.xhrWrappable){var g=t(10),b=t(11),E=t(8),R=t(6),O=t(13),C=t(7),P=t(14),T=t(9),L=t("ee"),S=L.get("tracer");t(16),x.features.spa=!0;var j,M=0;L.on(u,r),L.on(l,r),L.on(d,o),L.on(p,o),L.buffer([u,d,"xhr-done","xhr-resolved"]),R.buffer([u]),O.buffer(["setTimeout"+c,"clearTimeout"+s,u]),P.buffer([u,"new-xhr","send-xhr"+s]),C.buffer([m+s,m+"-done",m+f+s,m+f+c]),E.buffer(["newURL"]),g.buffer([u]),b.buffer(["propagate",l,p,"executor-err","resolve"+s]),S.buffer([u,"no-"+u]),T.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"]),a(P,"send-xhr"+s),a(L,"xhr-resolved"),a(L,"xhr-done"),a(C,m+s),a(C,m+"-done"),a(T,"new-jsonp"),a(T,"jsonp-end"),a(T,"cb-start"),E.on("pushState-end",i),E.on("replaceState-end",i),w[v]("hashchange",i,!0),w[v]("load",i,!0),w[v]("popstate",function(){i(0,M>1)},!0)}},{}],5:[function(t,e,n){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(13),s=t(12),c="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",l="resource",p="-start",h="-end",m="fn"+p,v="fn"+h,w="bstTimer",y="pushState",x=t("loader");x.features.stn=!0,t(8);var g=NREUM.o.EV;o.on(m,function(t,e){var n=t[0];n instanceof g&&(this.bstStart=x.now())}),o.on(v,function(t,e){var n=t[0];n instanceof g&&i("bst",[n,e,this.bstStart,x.now()])}),a.on(m,function(t,e,n){this.bstStart=x.now(),this.bstType=n}),a.on(v,function(t,e){i(w,[e,this.bstStart,x.now(),this.bstType])}),s.on(m,function(){this.bstStart=x.now()}),s.on(v,function(t,e){i(w,[e,this.bstStart,x.now(),"requestAnimationFrame"])}),o.on(y+p,function(t){this.time=x.now(),this.startPath=location.pathname+location.hash}),o.on(y+h,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+c]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["c"+c]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["webkitC"+c]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],6:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),s=t(26)(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=c(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?s(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],7:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=r.apply(this,arguments);return o.emit(n+"start",arguments,t),t.then(function(e){return o.emit(n+"end",[null,e],t),e},function(e){throw o.emit(n+"end",[e],t),e})})}var o=t("ee").get("fetch"),i=t(23);e.exports=o;var a=window,s="fetch-",c=s+"body-",f=["arrayBuffer","blob","json","text","formData"],u=a.Request,d=a.Response,l=a.fetch,p="prototype";u&&d&&l&&(i(f,function(t,e){r(u[p],e,c),r(d[p],e,c)}),r(a,"fetch",s),o.on(s+"end",function(t,e){var n=this;if(e){var r=e.headers.get("content-length");null!==r&&(n.rxSize=r),o.emit(s+"done",[null,e],n)}else o.emit(s+"done",[t],n)}))},{}],8:[function(t,e,n){var r=t("ee").get("history"),o=t(26)(r);e.exports=r,o.inPlace(window.history,["pushState","replaceState"],"-")},{}],9:[function(t,e,n){function r(t){function e(){c.emit("jsonp-end",[],l),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}function n(){c.emit("jsonp-error",[],l),c.emit("jsonp-end",[],l),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}var r=t&&"string"==typeof t.nodeName&&"script"===t.nodeName.toLowerCase();if(r){var o="function"==typeof t.addEventListener;if(o){var a=i(t.src);if(a){var u=s(a),d="function"==typeof u.parent[u.key];if(d){var l={};f.inPlace(u.parent,[u.key],"cb-",l),t.addEventListener("load",e,!1),t.addEventListener("error",n,!1),c.emit("new-jsonp",[t.src],l)}}}}}function o(){return"addEventListener"in window}function i(t){var e=t.match(u);return e?e[1]:null}function a(t,e){var n=t.match(l),r=n[1],o=n[3];return o?a(o,e[r]):e[r]}function s(t){var e=t.match(d);return e&&e.length>=3?{key:e[2],parent:a(e[1],window)}:{key:t,parent:window}}var c=t("ee").get("jsonp"),f=t(26)(c);if(e.exports=c,o()){var u=/[?&](?:callback|cb)=([^&#]+)/,d=/(.*)\.([^.]+)/,l=/^(\w+)(\.|$)(.*)$/,p=["appendChild","insertBefore","replaceChild"];f.inPlace(HTMLElement.prototype,p,"dom-"),f.inPlace(HTMLHeadElement.prototype,p,"dom-"),f.inPlace(HTMLBodyElement.prototype,p,"dom-"),c.on("dom-start",function(t){r(t[0])})}},{}],10:[function(t,e,n){var r=t("ee").get("mutation"),o=t(26)(r),i=NREUM.o.MO;e.exports=r,i&&(window.MutationObserver=function(t){return this instanceof i?new i(o(t,"fn-")):i.apply(this,arguments)},MutationObserver.prototype=i.prototype)},{}],11:[function(t,e,n){function r(t){var e=a.context(),n=s(t,"executor-",e),r=new f(n);return a.context(r).getCtx=function(){return e},a.emit("new-promise",[r,e],e),r}function o(t,e){return e}var i=t(26),a=t("ee").get("promise"),s=i(a),c=t(23),f=NREUM.o.PR;e.exports=a,f&&(window.Promise=r,["all","race"].forEach(function(t){var e=f[t];f[t]=function(n){function r(t){return function(){a.emit("propagate",[null,!o],i),o=o||!t}}var o=!1;c(n,function(e,n){Promise.resolve(n).then(r("all"===t),r(!1))});var i=e.apply(f,arguments),s=f.resolve(i);return s}}),["resolve","reject"].forEach(function(t){var e=f[t];f[t]=function(t){var n=e.apply(f,arguments);return t!==n&&a.emit("propagate",[t,!0],n),n}}),f.prototype["catch"]=function(t){return this.then(null,t)},f.prototype=Object.create(f.prototype,{constructor:{value:r}}),c(Object.getOwnPropertyNames(f),function(t,e){try{r[e]=f[e]}catch(n){}}),a.on("executor-start",function(t){t[0]=s(t[0],"resolve-",this),t[1]=s(t[1],"resolve-",this)}),a.on("executor-err",function(t,e,n){t[1](n)}),s.inPlace(f.prototype,["then"],"then-",o),a.on("then-start",function(t,e){this.promise=e,t[0]=s(t[0],"cb-",this),t[1]=s(t[1],"cb-",this)}),a.on("then-end",function(t,e,n){this.nextPromise=n;var r=this.promise;a.emit("propagate",[r,!0],n)}),a.on("cb-end",function(t,e,n){a.emit("propagate",[n,!0],this.nextPromise)}),a.on("propagate",function(t,e,n){this.getCtx&&!e||(this.getCtx=function(){if(t instanceof Promise)var e=a.context(t);return e&&e.getCtx?e.getCtx():this})}),r.toString=function(){return""+f})},{}],12:[function(t,e,n){var r=t("ee").get("raf"),o=t(26)(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],13:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t(26)(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],14:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",s)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,y,"fn-",s)}function i(t){x.push(t),h&&(b?b.then(a):v?v(a):(E=-E,R.data=E))}function a(){for(var t=0;t<x.length;t++)r([],x[t]);x.length&&(x=[])}function s(t,e){return e}function c(t,e){for(var n in t)e[n]=t[n];return e}t(6);var f=t("ee"),u=f.get("xhr"),d=t(26)(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,v=l.SI,w="readystatechange",y=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],x=[];e.exports=u;var g=window.XMLHttpRequest=function(t){var e=new p(t);try{u.emit("new-xhr",[e],e),e.addEventListener(w,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(c(p,g),g.prototype=p.prototype,d.inPlace(g.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),h){var b=m&&m.resolve();if(!v&&!m){var E=1,R=document.createTextNode(E);new h(a).observe(R,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===w||a()})},{}],15:[function(t,e,n){function r(){var t=window.NREUM,e=t.info.accountID||null,n=t.info.agentID||null,r=t.info.trustKey||null,i="btoa"in window&&"function"==typeof window.btoa;if(!e||!n||!i)return null;var a={v:[0,1],d:{ty:"Browser",ac:e,ap:n,id:o.generateCatId(),tr:o.generateCatId(),ti:Date.now()}};return r&&e!==r&&(a.d.tk=r),btoa(JSON.stringify(a))}var o=t(21);e.exports={generateTraceHeader:r}},{}],16:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<p;r++)t.removeEventListener(l[r],this.listener,!1);e.aborted||(n.duration=s.now()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==e.status&&(e.status=0):a(this,t),n.cbTime=this.cbTime,d.emit("xhr-done",[t],t),c("xhr",[e,n,this.startTime]))}}function o(t,e){var n=t.responseType;if("json"===n&&null!==e)return e;var r="arraybuffer"===n||"blob"===n||"json"===n?t.response:t.responseText;return v(r)}function i(t,e){var n=f(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}function a(t,e){t.params.status=e.status;var n=o(e,t.lastSize);if(n&&(t.metrics.rxSize=n),t.sameOrigin){var r=e.getResponseHeader("X-NewRelic-App-Data");r&&(t.params.cat=r.split(", ").pop())}t.loadCaptureCalled=!0}var s=t("loader");if(s.xhrWrappable){var c=t("handle"),f=t(17),u=t(15).generateTraceHeader,d=t("ee"),l=["load","error","abort","timeout"],p=l.length,h=t("id"),m=t(20),v=t(19),w=window.XMLHttpRequest;s.features.xhr=!0,t(14),d.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,e.loadCaptureCalled=!1,t.addEventListener("load",function(n){a(e,t)},!1),m&&(m>34||m<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),d.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),d.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid);var n=!1;if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(n=!!NREUM.init.distributed_tracing.enabled),n&&this.sameOrigin){var r=u();r&&e.setRequestHeader("newrelic",r)}}),d.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=v(r);i&&(n.txSize=i)}this.startTime=s.now(),this.listener=function(t){try{"abort"!==t.type||o.loadCaptureCalled||(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{d.emit("internal-error",[n])}catch(r){}}};for(var a=0;a<p;a++)e.addEventListener(l[a],this.listener,!1)}),d.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),d.on("xhr-load-added",function(t,e){var n=""+h(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),d.on("xhr-load-removed",function(t,e){var n=""+h(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),d.on("addEventListener-end",function(t,e){e instanceof w&&"load"===t[0]&&d.emit("xhr-load-added",[t[1],t[2]],e)}),d.on("removeEventListener-end",function(t,e){e instanceof w&&"load"===t[0]&&d.emit("xhr-load-removed",[t[1],t[2]],e)}),d.on("fn-start",function(t,e,n){e instanceof w&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=s.now()))}),d.on("fn-end",function(t,e){this.xhrCbStart&&d.emit("xhr-cb-time",[s.now()-this.xhrCbStart,this.onload,e],e)})}},{}],17:[function(t,e,n){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!e.protocol||":"===e.protocol||e.protocol===n.protocol,a=e.hostname===document.domain&&e.port===n.port;return r.sameOrigin=i&&(!e.hostname||a),r}},{}],18:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[f.now()].concat(s(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(23),s=t(24),c=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,e){u[e]=o(l+e,!0,"api")}),u.addPageAction=o(l+"addPageAction",!0),u.setCurrentRouteName=o(l+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(p+"tracer",[f.now(),t,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[f.now(),r,o],n),o)try{return e.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],n),t}finally{c.emit("fn-end",[f.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){h[e]=o(p+e)}),newrelic.noticeError=function(t,e){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now(),!1,e])}},{}],19:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],20:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],21:[function(t,e,n){function r(){function t(){return e?15&e[n++]:16*Math.random()|0}var e=null,n=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&(e=r.getRandomValues(new Uint8Array(31)));for(var o,i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",a="",s=0;s<i.length;s++)o=i[s],"x"===o?a+=t().toString(16):"y"===o?(o=3&t()|8,a+=o.toString(16)):a+=o;return a}function o(){function t(){return e?15&e[n++]:16*Math.random()|0}var e=null,n=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&Uint8Array&&(e=r.getRandomValues(new Uint8Array(31)));for(var o=[],i=0;i<16;i++)o.push(t().toString(16));return o.join("")}e.exports={generateUuid:r,generateCatId:o}},{}],22:[function(t,e,n){function r(t,e){if(!o)return!1;if(t!==o)return!1;if(!e)return!0;if(!i)return!1;for(var n=i.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var s=navigator.userAgent,c=s.match(a);c&&s.indexOf("Chrome")===-1&&s.indexOf("Chromium")===-1&&(o="Safari",i=c[1])}e.exports={agent:o,version:i,match:r}},{}],23:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],24:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],25:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],26:[function(t,e,n){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(24),a="nr@original",s=Object.prototype.hasOwnProperty,c=!1;e.exports=function(t,e){function n(t,e,n,o){function nrWrapper(){var r,a,s,c;try{a=this,r=i(arguments),s="function"==typeof n?n(r,a):n||{}}catch(f){l([f,"",[r,a,o],s])}u(e+"start",[r,a,o],s);try{return c=t.apply(a,r)}catch(d){throw u(e+"err",[r,a,d],s),d}finally{u(e+"end",[r,a,c],s)}}return r(t)?t:(e||(e=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,e,o,i){o||(o="");var a,s,c,f="-"===o.charAt(0);for(c=0;c<e.length;c++)s=e[c],a=t[s],r(a)||(t[s]=n(a,f?s+o:o,i,s))}function u(n,r,o){if(!c||e){var i=c;c=!0;try{t.emit(n,r,o,e)}catch(a){l([a,n,r,o])}c=i}}function d(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){l([r])}for(var o in t)s.call(t,o)&&(e[o]=t[o]);return e}function l(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=o),n.inPlace=f,n.flag=a,n}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?c(t,s,i):i()}function n(n,r,o,i){if(!l.aborted||i){t&&t(n,r,o);for(var a=e(o),s=m(n),c=s.length,f=0;f<c;f++)s[f].apply(a,r);var d=u[x[n]];return d&&d.push([g,n,r,a]),a}}function p(t,e){y[t]=m(t).concat(e)}function h(t,e){var n=y[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function m(t){return y[t]||[]}function v(t){return d[t]=d[t]||o(n)}function w(t,e){f(t,function(t,n){e=e||"feature",x[n]=e,e in u||(u[e]=[])})}var y={},x={},g={on:p,addEventListener:p,removeEventListener:h,emit:n,get:v,listeners:m,context:e,buffer:w,abort:a,aborted:!1};return g}function i(){return new r}function a(){(u.api||u.feature)&&(l.aborted=!0,u=l.backlog={})}var s="nr@context",c=t("gos"),f=t(23),u={},d={},l=e.exports=o();l.backlog=u},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!E++){var t=b.info=NREUM.info,e=p.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return u.abort();f(x,function(e,n){t[e]||(t[e]=n)}),c("mark",["onload",a()+b.offset],null,"api");var n=p.createElement("script");n.src="https://"+t.agent,e.parentNode.insertBefore(n,e)}}function o(){"complete"===p.readyState&&i()}function i(){c("mark",["domContent",a()+b.offset],null,"api")}function a(){return R.exists&&performance.now?Math.round(performance.now()):(s=Math.max((new Date).getTime(),s))-b.offset}var s=(new Date).getTime(),c=t("handle"),f=t(23),u=t("ee"),d=t(22),l=window,p=l.document,h="addEventListener",m="attachEvent",v=l.XMLHttpRequest,w=v&&v.prototype;NREUM.o={ST:setTimeout,SI:l.setImmediate,CT:clearTimeout,XHR:v,REQ:l.Request,EV:l.Event,PR:l.Promise,MO:l.MutationObserver};var y=""+location,x={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-spa-1123.min.js"},g=v&&w&&w[h]&&!/CriOS/.test(navigator.userAgent),b=e.exports={offset:s,now:a,origin:y,features:{},xhrWrappable:g,userAgent:d};t(18),p[h]?(p[h]("DOMContentLoaded",i,!1),l[h]("load",r,!1)):(p[m]("onreadystatechange",o),l[m]("onload",r)),c("mark",["firstbyte",s],null,"api");var E=0,R=t(25)},{}]},{},["loader",2,16,5,3,4]);</script><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","queueTime":4,"licenseKey":"8c32ed8b53","agent":"","transactionName":"ZwdbZkpZXENVWxZbDF5Nf0dWW0ZZW1ZNRQZSA1dTVEFGWVdLTEUGUkxLV05RV0caSgdEClUVSgh/XVxVRlEBYAZGC1xFblFXRxpfB0Y=","applicationID":"2163096","errorBeacon":"bam.nr-data.net","applicationTime":866}</script>
<meta name="robots" content="noarchive">
<meta name="viewport" content="width=980">
<title>放置奇兵 -全球同服放置类游戏 - iOS Store App Store 评论 | App Annie</title>
<meta name="description" content="
查看iOS Store上放置奇兵 -全球同服放置类游戏的评论。您可以根据 App 版本、所在国家、评分和时间段的不同对所有评论进行分类。
">
<meta name="keywords" content="app annie connect store stats intelligence rankings reviews statistics market data ios apple google android">
<meta name="google-site-verification" content="ivCYuhXzy549wGxwC7WBt3xK68o8CBxXAmt0tWt-ork">

<meta name="apple-itunes-app" content="app-id=660004961">
<meta name="google-play-app" content="app-id=com.appannie.app">



    
        <meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@appannie">
<meta name="twitter:creator" content="@appannie">

    <meta name="twitter:title" content="放置奇兵 -全球同服放置类游戏">
    <meta property="og:title" content="放置奇兵 -全球同服放置类游戏">



    <meta name="twitter:image:src" content="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a">
    <meta property="og:image" content="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a">


    


<link rel="alternate" type="application/rss+xml" title="App Annie - App Tracking &amp; Analytics" href="http://feeds.feedburner.com/askannie">
<link rel="apple-touch-icon-precomposed" href="https://static-s.aa-cdn.net/media/pictures/favicon-60.v-0c92e327.png">
<link rel="icon" type="image/png" href="https://static-s.aa-cdn.net/media/pictures/favicon.v-edfeee35.png">
<link rel="preload" href="https://static-s.aa-cdn.net/media/css/fonts/ProximaNova/ProximaNova-Regular.v-67525874.woff" as="font" type="font/woff2" crossorigin="">
<link rel="preload" href="https://static-s.aa-cdn.net/media/css/fonts/ProximaNova/ProximaNova-Bold.v-acdec6aa.woff" as="font" type="font/woff2" crossorigin="">
<link rel="preload" href="https://static-s.aa-cdn.net/media/css/fonts/fontawesome_4.3.0/fontawesome-webfont.woff2?v=4.3.0" as="font" type="font/woff2" crossorigin="">

<script>
AA_MEDIA_URL = 'https://static-s.aa-cdn.net/media/';
AA_CMS_CONTENT_URL = 'https://static-c.aa-cdn.net/wp-content/';
AA_BLOG_CONTENT_URL = 'https://static-s.aa-cdn.net/media/blog-content/';
</script>
<script>
/* quick $ step 1/3 */
(function() {
var fns = __aa_fns = [];
$ = jQuery = function(fn) {
  if (fn.call && fn.apply) { fns.push(fn); return;
  } else if (fn === document) {
    return { ready: function(fn) {
        if (fn.call && fn.apply) { fns.push(fn); }
    } };
  }
  throw 'dont use $ other than ready';
};
$.extend = function(obj) {
  var i=1,srcs=arguments,l=srcs.length,src,key;
  for(;i<l;++i) { src=srcs[i];
    for (key in src) { obj[key] = src[key]; }
  }
  return obj;
};

window.__lang = 'zh-cn';
})();
</script>



<link type="text/css" rel="stylesheet" href="https://static-s.aa-cdn.net/media/css/c/base.min.v-73e7c19c.css">

    
        <link type="text/css" rel="stylesheet" href="https://static-s.aa-cdn.net/media/css/c/prod.min.v-729ab107.css">
    




<!-- TradeDoubler site verification 2289284 -->
<script type="text/javascript" async="" src="//munchkin.marketo.net/munchkin.js"></script><script src="https://googleads.g.doubleclick.net/pagead/viewthroughconversion/975177143/?random=1559256391782&amp;cv=9&amp;fst=1559256391782&amp;num=1&amp;guid=ON&amp;resp=GooglemKTybQhCsO&amp;u_h=800&amp;u_w=1280&amp;u_ah=730&amp;u_aw=1280&amp;u_cd=24&amp;u_his=74&amp;u_tz=-300&amp;u_java=true&amp;u_nplug=1&amp;u_nmime=3&amp;gtm=2wg5m0&amp;sendb=1&amp;frm=0&amp;url=https%3A%2F%2Fwww.appannie.com%2Fapps%2Fios%2Fapp%2Fidle-heroes%2Freviews%2F%3Forder_by%3Ddate%26order_type%3Ddesc%26date%3D2019-04-29~2019-05-29%26translate_selected%3Dfalse%26granularity%3Dweekly%26stack%26percent%3Dfalse%26series%3Drating_star_1%2Crating_star_2%2Crating_star_3%2Crating_star_4%2Crating_star_5&amp;ref=https%3A%2F%2Fwww.appannie.com%2Fapps%2Fios%2Fapp%2Fidle-heroes%2Fapp-ranking%2F%3Fdevice%3Diphone%26type%3Dranks%26date%3D2019-05-29&amp;tiba=%E6%94%BE%E7%BD%AE%E5%A5%87%E5%85%B5%20-%E5%85%A8%E7%90%83%E5%90%8C%E6%9C%8D%E6%94%BE%E7%BD%AE%E7%B1%BB%E6%B8%B8%E6%88%8F%20-%20iOS%20Store%20App%20Store%20%E8%AF%84%E8%AE%BA%20%7C%20App%20Annie&amp;async=1&amp;rfmt=3&amp;fmt=4"></script><script src="https://googleads.g.doubleclick.net/pagead/viewthroughconversion/861559337/?random=1559256391786&amp;cv=9&amp;fst=1559256391786&amp;num=1&amp;guid=ON&amp;resp=GooglemKTybQhCsO&amp;u_h=800&amp;u_w=1280&amp;u_ah=730&amp;u_aw=1280&amp;u_cd=24&amp;u_his=74&amp;u_tz=-300&amp;u_java=true&amp;u_nplug=1&amp;u_nmime=3&amp;gtm=2wg5m0&amp;sendb=1&amp;frm=0&amp;url=https%3A%2F%2Fwww.appannie.com%2Fapps%2Fios%2Fapp%2Fidle-heroes%2Freviews%2F%3Forder_by%3Ddate%26order_type%3Ddesc%26date%3D2019-04-29~2019-05-29%26translate_selected%3Dfalse%26granularity%3Dweekly%26stack%26percent%3Dfalse%26series%3Drating_star_1%2Crating_star_2%2Crating_star_3%2Crating_star_4%2Crating_star_5&amp;ref=https%3A%2F%2Fwww.appannie.com%2Fapps%2Fios%2Fapp%2Fidle-heroes%2Fapp-ranking%2F%3Fdevice%3Diphone%26type%3Dranks%26date%3D2019-05-29&amp;tiba=%E6%94%BE%E7%BD%AE%E5%A5%87%E5%85%B5%20-%E5%85%A8%E7%90%83%E5%90%8C%E6%9C%8D%E6%94%BE%E7%BD%AE%E7%B1%BB%E6%B8%B8%E6%88%8F%20-%20iOS%20Store%20App%20Store%20%E8%AF%84%E8%AE%BA%20%7C%20App%20Annie&amp;async=1&amp;rfmt=3&amp;fmt=4"></script><script async="" src="https://cdn.walkme.com/users/440e9852f2724fafb2d968494f028e77/settings.txt" id="mt_script"></script><script async="" src="https://cdn.walkme.com/player/resources/wmjQuery171.js" id="mt_script"></script><script async="" src="https://cdn.walkme.com/users/440e9852f2724fafb2d968494f028e77/scripts/prelib-plugin-wmloader-d297afa6-bc2d-4263-a045-902394c47619.js" id="mt_script"></script><script async="" src="https://cdn.walkme.com/player/lib/walkme_lib_20190512-103449-0f686237.js" id="mt_script"></script><style type="text/css" media="print">.usabilla_live_button_container { display: none; }</style><script async="" src="https://cdn.walkme.com/users/440e9852f2724fafb2d968494f028e77/data_216ab230dac4466bb58e50ce1a781b2e_zh-cn.js" id="mt_script"></script><script charset="utf-8" src="https://cdn.walkme.com/player/lib/20190512-103449-0f686237/9.30996c83.walkme_lib.js"></script><script charset="utf-8" src="https://cdn.walkme.com/player/lib/20190512-103449-0f686237/webComponentDrawableCreator.5809ba0b.walkme_lib.js"></script><style type="text/css" class="walkme-to-remove" id="walkme-custom-css">.custom-launcher-19842:active {
}.custom-launcher-19842:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: #189be3;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-19842 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 36px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #168dce;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-19843:active {
}.custom-launcher-19843:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: #189be3;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-19843 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 24px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #168dce;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-19844:active {
}.custom-launcher-19844:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: #189be3;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-19844 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 20px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #168dce;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-45302 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #ffffff;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-45302:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: #ffffff;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-45302:active {
}.custom-launcher-47005 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #168dce;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-47005:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: #189be3;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-47005:active {
}.custom-launcher-47006 {
	font-weight: bold;
	font-style: normal;
	text-decoration: none;
	font-size: 16px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #168dce;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-47006:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: #189be3;
	font-weight: bold;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-47006:active {
}.custom-launcher-47486 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: #3f88d4;
	background-color: #ffffff;
	border-color: #3f88d4;
	border-radius: 0px;
	border-width: 1px;
	border-style: solid;
	padding-top: 3px;
	padding-right: 0px;
	padding-bottom: 3px;
	padding-left: 0px;
}.custom-launcher-47486:hover {
	color: #ffffff;
	background-color: #3f88d4;
	border-color: #3f88d4;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-47486:active {
	color: #ffffff;
	background-color: #4596e9;
	border-color: #4596e9;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-50153 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "Arial";
	color: #000000;
	background-color: #ffffff;
	border-color: #ffffff;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-50153:hover {
	color: #000000;
	background-color: #ffffff;
	border-color: #ffffff;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-50153:active {
}.custom-launcher-76965 {
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #102235;
	border-color: #102205;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-76965:hover {
	color: #ffffff;
	background-color: #12253a;
	border-color: #122506;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-76965:active {
}.custom-launcher-85177 {
	font-weight: normal;
	font-style: normal;
	line-height: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #102235;
	border-color: #102235;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-85177:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: transparent;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-85177:active {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: transparent;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-165805 {
	font-weight: normal;
	font-style: normal;
	line-height: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #168dce;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-165805:hover {
	color: #ffffff;
	background-color: #1cb8ff;
	border-color: #189be3;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-165805:active {
}.custom-launcher-171215 {
	font-weight: normal;
	font-style: normal;
	line-height: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: transparent;
	background-color: transparent;
	border-color: transparent;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 11px;
	padding-bottom: 7px;
	padding-left: 11px;
}.custom-launcher-171215:hover {
	color: transparent;
	background-color: transparent;
	border-color: transparent;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-171215:active {
}.custom-launcher-171331 {
	font-weight: normal;
	font-style: normal;
	line-height: normal;
	text-decoration: none;
	font-size: 12px;
	font-family: "walkme-opensans";
	color: #fff;
	background-color: #19a7f8;
	border-color: #168dce;
	border-radius: 2px;
	border-width: 1px;
	border-style: solid;
	padding-top: 7px;
	padding-right: 7px;
	padding-bottom: 7px;
	padding-left: 7px;
}.custom-launcher-171331:hover {
	color: transparent;
	background-color: transparent;
	border-color: #189be3;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}.custom-launcher-171331:active {
	color: transparent;
	background-color: transparent;
	border-color: #189be3;
	font-weight: normal;
	font-style: normal;
	text-decoration: none;
}/* Theme 4 Menu ---- START */
#walkme-menu {
  height: auto !important;
}
#walkme-menu .walkme-main {
  width: 410px !important;
  height: 510px !important;
  box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.3) !important;
  border: 1px solid #dcdcdc !important;
}
#walkme-menu .walkme-main,
#walkme-menu .walkme-jspContainer,
#walkme-menu .walkme-deployable .walkme-deployable-icon,
#walkme-menu .walkme-category > .walkme-deployable-row,
#walkme-menu .walkme-category > .walkme-deployable-row:hover,
#walkme-menu .walkme-activatable:hover {
  background-color: #ffffff !important;
}
/* X */
#walkme-menu .walkme-minimize.walkme-menu-click-close {
  top: 8px !important;
  right: 35px !important;
  color: #444444 !important;
  opacity: 0.3 !important;
}
/* Language Dropdown */
#walkme-menu #walkme-languages {
  margin-top: 21px !important;
  font-family: "walkme-lato-regular",Arial !important;
  font-weight: 100 !important;
  color: #444444 !important;
  opacity: 0.4 !important;
}
#walkme-menu .walkme-languages-arrow,
#walkme-menu #walkme-current-language {
  color: #444444 !important;
  opacity: 1.0 !important;
}
/* Title */

#walkme-menu #walkme-title {
  display:block;
  background-image: url(http://appannie.com/media/pictures/header-footer-images/learn.v-06fccb4a.svg) !important;
  background-repeat: no-repeat !important;
    background-size: 22px 22px !important;
  padding: 0px 0px 0px 32px !important;
  vertical-align: middle !important;
  margin: 20px 0px 0px 20px !important;
  font-size: 18px !important;
  color: #444444 !important;
  overflow: visible !important;
}
/* Tabs */
#walkme-menu #walkme-tabs-wrapper {
  display: block !important;
  width: 410px !important;
  top: 55px !important;
  margin: 0px auto !important;
  padding: 0px !important;
  overflow: hidden !important;
}
#walkme-menu.walkme-no-tabs #walkme-tabs-wrapper {
  top: 39px !important;
}
#walkme-menu #walkme-tabs {
  height: 38px !important;
  border-bottom: none !important;
}
#walkme-menu #walkme-tabs .walkme-tab-button {
  width: calc(50% - 30px) !important;
  height: 38px !important;
  margin: 0px 20px 0px 10px !important;
  padding: 1px 6px !important;
  background-color: #ffffff !important;
  border: 1px solid #dcdcdc !important;
  border-radius: 3px !important;
}
#walkme-menu #walkme-tabs .walkme-tab-button.walkme-first-tab {
  margin: 0px 10px 0px 20px !important;
}
#walkme-menu #walkme-tabs .walkme-tab-button .walkme-tab-button-image {
  display: none !important;
}
#walkme-menu #walkme-tabs .walkme-tab-button .walkme-tab-button-text {
  padding-top: 8px !important;
  font-size: 15px !important;
  color: #3F88D4 !important;
}
/* Selected Tab */
#walkme-menu #walkme-tabs .walkme-tab-button.walkme-tab-button-selected {
  background-color: #3F88D4 !important;
  border-color: #3F88D4 !important;
}
#walkme-menu #walkme-tabs .walkme-tab-button.walkme-tab-button-selected .walkme-tab-button-text {
  color: #ffffff !important;
}
/* Search Box */
#walkme-menu .walkme-search-box-container {
  width: 370px !important;
  margin: 20px 20px 0px 20px !important;
}
#walkme-menu .walkme-search-box-container .walkme-search-box {
  width: 303px !important;
  height: 39px !important;
  margin: 0px !important;
  padding-left: 10px !important;
  border: 1px solid #dcdcdc !important;
  border-radius: 3px !important;
    font-size: 14px !important;
    font-weight: 100 !important;
    color: #444444 !important;
    opacity: 0.6 !important;
}
#walkme-menu .walkme-search-box-container .walkme-search-box-button {
  width: 45px !important;
  height: 40px !important;
  background: #3F88D4 !important;
  border-radius: 3px !important;
}
#walkme-menu .walkme-search-box-container .walkme-search-box-button .walkme-search-box-button-image {
  display: block !important;
  margin: 12px 0px 0px 14px !important;
  font-family: 'walkme-widget-font' !important;
  color: #ffffff !important;
}
#walkme-menu .walkme-search-results-list-inner .walkme-message.walkme-no-results {
  margin-top: 20px !important;
}
#walkme-menu .walkme-search-results-list-inner .walkme-message.walkme-no-results .walkme-text {
  font-weight: normal !important;
  color: #444444 !important;
}
/* Menu Content */
#walkme-menu .walkme-deployables-list,
#walkme-menu .walkme-search-results-list {
  width: 370px !important;
  margin: 20px 20px 0px !important;
  background: transparent !important;
  border: 1px solid #dcdcdc !important;
  border-radius: 2px !important;
}
#walkme-menu .walkme-jspContainer {
  height: 371px !important;
}
#walkme-menu .walkme-jspContainer .walkme-jspPane {
  width: 370px !important;
}
#walkme-menu .walkme-deployable {
  height: auto !important;
  background: transparent !important;
  background-color: transparent !important;
  border-bottom: 1px solid #dcdcdc !important;
}
#walkme-menu .walkme-deployable.walkme-tab {
  border-bottom: none !important;
}
#walkme-menu .walkme-deployable .walkme-name,
#walkme-menu .walkme-deployable.walkme-category.walkme-opened .walkme-activatable .walkme-text .walkme-name,
#walkme-menu .walkme-deployable.walkme-category > .walkme-deployable-row > .walkme-text > .walkme-name {
  font-size: 14px !important;
  font-weight: 100 !important;
  padding: 5px 0px 5px 10px !important;
  color: #444444 !important;
}
#walkme-menu .walkme-deployable .walkme-description {
  font-weight: 100 !important;
  color: #444444 !important;
  opacity: 0.6 !important;
}
#walkme-menu .walkme-deployable .walkme-name, 
#walkme-menu .walkme-activatable .walkme-name:hover,
#walkme-menu .walkme-deployable.walkme-category.walkme-opened .walkme-activatable .walkme-text .walkme-name:hover,
#walkme-menu .walkme-deployable.walkme-category > .walkme-deployable-row > .walkme-text > .walkme-name:hover {
  font-size: 14px !important;
  font-weight: 100 !important;
  padding-left: 10px !important;
  padding: 5px 0px 5px 10px !important;
  color: #3F88D4 !important;
}
#walkme-menu .walkme-activatable,
#walkme-menu .walkme-category > .walkme-deployable-row > .walkme-text {
  margin: 0px !important;
}
#walkme-menu .walkme-deployable.walkme-category.walkme-opened {
  padding-bottom: 6px !important;
}
#walkme-menu .walkme-deployable.walkme-category.walkme-opened .walkme-activatable {
  border-bottom: none !important;
}
#walkme-menu .walkme-deployable.walkme-category.walkme-opened .walkme-activatable .walkme-deployable-row {
  padding: 6px 0px 2px !important;
}
#walkme-menu .walkme-deployable.walkme-category.walkme-opened .walkme-activatable .walkme-deployable-row .walkme-text {
  padding-top: 0px !important;
}
#walkme-menu .walkme-message > div:nth-child(1),
#walkme-menu .walkme-deployable.walkme-activatable .walkme-deployable-icon::before, 
#walkme-menu .walkme-deployable.walkme-category > .walkme-deployable-row > .walkme-deployable-icon,
#walkme-menu .walkme-deployable.walkme-category > .walkme-deployable-row:hover > .walkme-deployable-icon {
  color: #3F88D4 !important;
}
#walkme-menu .walkme-deployable .walkme-description, 
.walkme-menu .walkme-activatable .walkme-description {
  padding-bottom: 4px !important;
  padding-left: 10px !important;
}
#walkme-menu .walkme-deployable .walkme-description:empty, 
.walkme-menu .walkme-activatable .walkme-description:empty,
#walkme-menu .walkme-category .walkme-deployable .walkme-description, 
.walkme-menu .walkme-category .walkme-activatable .walkme-description {
  padding-bottom: 0px !important;
}
/* Onboarding Content */
#walkme-menu .walkme-deployable.walkme-task .walkme-deployable-row .walkme-text .walkme-deployable-name {
  padding-left: 0px !important;
}
#walkme-menu .walkme-deployable.walkme-task.walkme-completed .walkme-deployable-row .walkme-text .walkme-deployable-name {
  font-style: italic !important;
  color: #444444 !important;
  opacity: 0.6 !important;
}
#walkme-menu #walkme-progress-bar {
  width: 370px !important;
  margin: 24px 20px !important;
  border: 1px solid #dcdcdc !important;
  border-radius: 3px !important;
}
#walkme-menu #walkme-progress-bar .walkme-progress-bar-inner {
  background-color: #3F88D4 !important;
}
#walkme-menu #walkme-progress-bar .walkme-progress-bar-inner .walkme-progress-bar-text {
  color: #444444 !important;
}
/* Scroll Bar */
#walkme-menu .walkme-jspVerticalBar {
  width: 8px !important;
  background: transparent !important;
}
#walkme-menu .walkme-jspVerticalBar .walkme-jspTrack {
  background: transparent !important;
  border-left: none !important;
}
#walkme-menu .walkme-jspVerticalBar .walkme-jspTrack .walkme-jspDrag {
  width: 6px !important;
  background-color: rgba(0, 0, 0, 0.25) !important;
  border-radius: 4px !important;
  border: none !important;
}
/* Footer */
#walkme-menu #walkme-footer {
  width: 410px !important;
}
#walkme-menu #walkme-footer .walkme-powered-by {
  display: none !important;
  font-weight: 300 !important;
  color: rgba(0, 0, 0, 0.25) !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
}
#walkme-menu .walkme-powered-by-logo {
  display: none !important;
}

#walkme-menu #walkme-footer .walkme-open-ticket {
  padding-left: 13px !important;
  color: #3F88D4 !important;
}
/* Icons */
#walkme-menu .walkme-minimize,
#walkme-menu .walkme-message .walkme-icon,
#walkme-menu .walkme-deployable .walkme-deployable-row .walkme-deployable-icon {
  font-family: 'walkme-widget-font' !important;
}
/* Theme 4 Menu ---- END */

div.walkme-menu.walkme-penguin.walkme-override .walkme-category-482050 .walkme-activatable, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-category-482050 .walkme-activatable {
 display: block !important;
}
  
div.walkme-menu.walkme-penguin.walkme-override .walkme-category-482050.walkme-opened .walkme-activatable, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-category-482050.walkme-opened .walkme-activatable,
div.walkme-menu.walkme-penguin.walkme-override .walkme-category-482050 .walkme-activatable.walkme-invisible, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-category-482050 .walkme-activatable.walkme-invisible {
 display: none !important;
}
  
div.walkme-menu.walkme-penguin.walkme-override .walkme-deployable.walkme-category-482050.walkme-override .walkme-activatable, 
div.walkme-menu.walkme-penguin.walkme-override .walkme-activatable.walkme-category-482050.walkme-override .walkme-activatable, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-deployable.walkme-category-482050.walkme-override .walkme-activatable, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-activatable.walkme-category-482050.walkme-override .walkme-activatable {
 border-bottom: none !important;
}
  
div.walkme-menu.walkme-penguin.walkme-override .walkme-deployable.walkme-category-482050.walkme-override .walkme-activatable .walkme-deployable-icon, 
div.walkme-menu.walkme-penguin.walkme-override .walkme-activatable.walkme-category-482050.walkme-override .walkme-activatable .walkme-deployable-icon, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-deployable.walkme-category-482050.walkme-override .walkme-activatable .walkme-deployable-icon, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-activatable.walkme-category-482050.walkme-override .walkme-activatable .walkme-deployable-icon {
 height: 20px !important;
    padding-top: 4px !important;
    margin-left: 12px !important;
    width: 26px !important;
}
  
div.walkme-menu.walkme-penguin.walkme-override .walkme-deployable.walkme-category-482050.walkme-override .walkme-activatable .walkme-text, 
div.walkme-menu.walkme-penguin.walkme-override .walkme-activatable.walkme-category-482050.walkme-override .walkme-activatable .walkme-text, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-deployable.walkme-category-482050.walkme-override .walkme-activatable .walkme-text, 
div.walkme-menu.walkme-penguin .walkme-override .walkme-activatable.walkme-category-482050.walkme-override .walkme-activatable .walkme-text {
 padding: 0 !important;
}
  
div.walkme-menu.walkme-penguin .walkme-category-482050 > .walkme-deployable-row > .walkme-deployable-icon:before, 
div.walkme-menu.walkme-penguin * .walkme-category-482050 > .walkme-deployable-row > .walkme-deployable-icon:before {
 content: "\e60a";
}
  
div.walkme-menu.walkme-penguin .walkme-category-482050.walkme-opened > .walkme-deployable-row > .walkme-deployable-icon:before, 
div.walkme-menu.walkme-penguin * .walkme-category-482050.walkme-opened > .walkme-deployable-row > .walkme-deployable-icon:before {
 content:"\e609";
}


#walkme-player[class*='walkme-language'] .walkme-title, .walkme-player.walkme-colorado *.walkme-position-major-top.walkme-direction-ltr .walkme-title {
    top: 8px !important;
    left: 50px !important;
  
  }

/* Monochrome balloon with Next and Back Button Default */

.wm-design-template-125 .walkme-custom-side-border {
  display: none !important;
}

.wm-design-template-125.walkme-custom-balloon-outer-div {
  min-width: 240px !important;
  max-width: 380px !important;
  -webkit-border-radius: 3px !important;
  -moz-border-radius: 3px !important;
  border-radius: 3px !important;
  background-color: #3B7AE4 !important;
}

.wm-design-template-125.walkme-custom-balloon-outer-div.walkme-custom-popup-step {
  min-width: 360px !important;
  max-width: 420px !important;
}

.wm-design-template-125 .walkme-custom-balloon-top-div {
  -webkit-border-radius: 3px !important;
  -moz-border-radius: 3px !important;
  border-radius: 3px !important;
  background-color: #3B7AE4 !important;
}

.wm-design-template-125 .walkme-custom-balloon-mid-div,
.wm-design-template-125 .walkme-custom-balloon-inner-div {
  -webkit-border-radius: 3px !important;
  -moz-border-radius: 3px !important;
  border-radius: 3px !important;
  background-color: #3B7AE4 !important;
}

.wm-design-template-125 .walkme-custom-balloon-mid-div {
  -webkit-box-shadow: 0 2px 7px 0 rgba(51,55,57,0.3) !important;
  -moz-box-shadow: 0 2px 7px 0 rgba(51,55,57,0.3) !important;
  box-shadow: 0 2px 7px 0 rgba(51,55,57,0.3) !important;
}

.wm-design-template-125 .walkme-custom-balloon-inner-div {
  border: none !important;
  background-color: #3B7AE4 !important;
}

.wm-design-template-125 .walkme-custom-balloon-close-button {
  padding: 0 !important;
  margin: 1px 7px 0 0 !important;
  font-size: 16px !important;
  font-weight: bold !important;
  color: #fff !important;
}

.wm-design-template-125 .walkme-custom-balloon-close-button:hover {
  color: #ccc !important;
}

.wm-design-template-125 .walkme-custom-balloon-title {
  margin-bottom: 6px !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #fff !important;
}

.wm-design-template-125 .walkme-custom-balloon-content {
  margin-bottom: 5px !important;
  font-weight: normal !important;
  color: #fff !important;
}

.wm-design-template-125 .walkme-custom-balloon-separator {
  display: none !important;
}

.wm-design-template-125 .walkme-custom-balloon-bottom-div {
  position: relative !important;
  height: 44px !important;
  margin-top: 10px !important;
  background-color: #3B7AE4 !important;
}

.wm-design-template-125.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  height: 28px !important;
}

/* buttons */

.wm-design-template-125 .walkme-custom-balloon-top-div-bottom {
  position: relative !important;
  z-index: 100 !important;
}

.wm-design-template-125 .walkme-custom-balloon-buttons-wrapper {
  padding: 0 8px 0 16px !important;
  margin: 0 !important;
}

.wm-design-template-125 .walkme-custom-balloon-button {
  height: 32px !important;
}

.wm-design-template-125 .walkme-custom-balloon-back-button {
  float: left !important;
  margin: 6px 0 !important;
  color: #fff !important;
  background-color: #3B7AE4 !important;
}

.wm-design-template-125 .walkme-custom-balloon-back-button:hover {
  color: #ececec !important;
}

.wm-design-template-125 .walkme-custom-balloon-next-button,
.wm-design-template-125 .walkme-custom-balloon-done-button,
.wm-design-template-125 .walkme-custom-balloon-start-button {
  margin: 6px 0 !important;
  color: #fff !important;
  background-color: #3B7AE4 !important;
}

.wm-design-template-125 .walkme-custom-balloon-next-button:hover,
.wm-design-template-125 .walkme-custom-balloon-done-button:hover,
.wm-design-template-125 .walkme-custom-balloon-start-button:hover {
  color: #ececec !important;
}

.wm-design-template-125 .walkme-custom-balloon-button-text {
  font-size: 10px !important;
  font-weight: bold !important;
  text-transform: uppercase !important;
}

/* powered by walkme */

.wm-design-template-125 .walkme-custom-powered-by-div {
  float: left !important;
  font-size: 10px !important;
  margin: 7px 0 !important;
}

.wm-design-template-125 .walkme-custom-powered-by {
  color: #fff !important;
}

.wm-design-template-125 .walkme-custom-powered-by:hover,
.wm-design-template-125 .walkme-custom-powered-by:active {
  color: #ccc !important;
}

/* step count */

.wm-design-template-125 .walkme-custom-balloon-subtext {
  position: absolute !important;
  width: 100% !important;
  padding: 0 !important;
  margin: 14px 0 0 0 !important;
  text-align: center !important;
  font-size: 10px !important;
  color: #fff !important;
}

.wm-design-template-125.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-subtext {
  margin-top: 6px !important;
}

/* arrows - need to be set up with border-width: 1px on Customize */

/* arrows - top arrow */

.wm-design-template-125.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 0 7px 6px 7px !important;
  border-color: transparent transparent #3B7AE4 !important;
  margin-top: 4px !important;
}

.wm-design-template-125.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 0 6px 5px 6px !important;
  border-color: transparent transparent #3B7AE4 !important;
  margin-top: 4px !important;
}

/* arrows - right arrow */

.wm-design-template-125.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 7px 0 7px 6px !important;
  border-color: transparent transparent transparent #3B7AE4 !important;
  margin-left: 1px !important;
}

.wm-design-template-125.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 6px 0 6px 6px !important;
  border-color: transparent transparent transparent #3B7AE4 !important;
  margin-left: 1px !important;
}

/* arrows - bottom arrow */

.wm-design-template-125.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 6px 7px 0 7px !important;
  border-color: #3B7AE4 transparent transparent transparent !important;
  margin-top: 1px !important;
}

.wm-design-template-125.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 5px 6px 0 6px !important;
  border-color: #3B7AE4 transparent transparent transparent !important;
  margin-top: 1px !important;
}

/* arrows - left arrow */

.wm-design-template-125.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 7px 6px 7px 0 !important;
  border-color: transparent #3B7AE4 transparent transparent !important;
  margin-left: 4px !important;
}

.wm-design-template-125.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 6px 5px 6px 0 !important;
  border-color: transparent #3B7AE4 transparent transparent !important;
  margin-left: 4px !important;
} /* Blue balloon with Next and Back Button Default */

.wm-design-template-126 .walkme-custom-side-border {
  display: none !important;
}

.wm-design-template-126.walkme-custom-balloon-outer-div {
  min-width: 240px !important;
  max-width: 380px !important;
}

.wm-design-template-126.walkme-custom-balloon-outer-div.walkme-custom-popup-step {
  min-width: 360px !important;
  max-width: 420px !important;
}

.wm-design-template-126 .walkme-custom-balloon-top-div {
  -webkit-border-radius: 1px !important;
  -moz-border-radius: 1px !important;
  border-radius: 1px !important;
  background-color: #fff !important;
}

.wm-design-template-126 .walkme-custom-balloon-mid-div,
.wm-design-template-126 .walkme-custom-balloon-inner-div {
  -webkit-border-radius: 1px !important;
  -moz-border-radius: 1px !important;
  border-radius: 1px !important;
  background-color: #fff !important;
}

.wm-design-template-126 .walkme-custom-balloon-mid-div {
  -webkit-box-shadow: 2px 2px 8px 0 rgba(137,138,148,0.32) !important;
  -moz-box-shadow: 2px 2px 8px 0 rgba(137,138,148,0.32) !important;
  box-shadow: 2px 2px 8px 0 rgba(137,138,148,0.32) !important;
}

.wm-design-template-126 .walkme-custom-balloon-inner-div {
  border: 1px solid #DCE1E6 !important;
}

.wm-design-template-126 .walkme-custom-balloon-close-button {
  padding: 0 !important;
  margin: 4px 8px 0 0 !important;
  font-size: 13px !important;
  color: #ccc !important;
}

.wm-design-template-126 .walkme-custom-balloon-close-button:hover {
  color: #9D9D9D !important;
}

.wm-design-template-126 .walkme-custom-balloon-title {
  margin-bottom: 6px !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  color: #1B2432 !important;
  text-transform: uppercase !important;
}

.wm-design-template-126 .walkme-custom-balloon-content {
  margin-bottom: 5px !important;
  font-size: 13px !important;
  font-weight: normal !important;
  color: #6A6A6A !important;
}

.wm-design-template-126 .walkme-custom-balloon-separator {
  background-color: #DCEBD0 !important;
}

.wm-design-template-126 .walkme-custom-balloon-bottom-div {
  position: relative !important;
  height: 44px !important;
  background-color: #fff !important;
}

.wm-design-template-126.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  height: 28px !important;
}

/* buttons */

.wm-design-template-126 .walkme-custom-balloon-buttons-wrapper {
  padding: 0 8px 0 16px !important;
  margin: 0 !important;
}

.wm-design-template-126 .walkme-custom-balloon-button {
  height: 32px !important;
}

.wm-design-template-126 .walkme-custom-balloon-back-button {
  margin: 6px 0 !important;
  color: #484B4F !important;
}

.wm-design-template-126 .walkme-custom-balloon-back-button:hover {
  color: #2D2F31 !important;
}

.wm-design-template-126 .walkme-custom-balloon-cancel-button {
  margin-right: 10px !important;
  color: #CCCCCC !important;
}

.wm-design-template-126 .walkme-custom-balloon-cancel-button:hover {
  color: #9D9D9D !important;
}

.wm-design-template-126 .walkme-custom-balloon-next-button,
.wm-design-template-126 .walkme-custom-balloon-start-button,
.wm-design-template-126 .walkme-custom-balloon-done-button {
  margin: 6px 0 6px 6px !important;
  background-color: #fff !important;
  color: #3397D1 !important;
}

.wm-design-template-126 .walkme-custom-balloon-next-button:hover,
.wm-design-template-126 .walkme-custom-balloon-start-button:hover,
.wm-design-template-126 .walkme-custom-balloon-done-button:hover {
  color: #1777AE !important;
}

.wm-design-template-126 .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
}

/* powered by walkme */

.wm-design-template-126 .walkme-custom-powered-by-div {
  float: left !important;
  font-size: 10px !important;
  margin: 7px 0 !important;
}

.wm-design-template-126 .walkme-custom-powered-by {
  color: #9d9d9d !important;
}

.wm-design-template-126 .walkme-custom-powered-by:hover,
.wm-design-template-126 .walkme-custom-powered-by:active {
  color: #8F8F8F !important;
}

/* step count */

.wm-design-template-126 .walkme-custom-balloon-subtext {
  margin-top: 16px !important;
  margin-left: 16px !important;
  color: #8F8F8F !important;
}

.wm-design-template-126.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-subtext {
  float: right !important;
  margin-top: 8px !important;
  margin-right: 16px !important;
  margin-left: 0 !important;
}

/* arrows - need to be set up with border-width: 1px on Customize */

/* arrows - top arrow */

.wm-design-template-126.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 0 6px 6px 6px !important;
  border-color: transparent transparent #dce1e7 !important;
  margin-top: 5px !important;
}

.wm-design-template-126.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 0 5px 5px 5px !important;
  border-color: transparent transparent #ffffff !important;
  margin-top: 5px !important;
}

/* arrows - right arrow */

.wm-design-template-126.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 6px 0 6px 6px !important;
  border-color: transparent transparent transparent #dce1e7 !important;
}

.wm-design-template-126.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 5px 0 5px 5px !important;
  border-color: transparent transparent transparent #ffffff !important;
}

/* arrows - bottom arrow */

.wm-design-template-126.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 6px 6px 0 6px !important;
  border-color: #dce1e7 transparent transparent transparent !important;
}

.wm-design-template-126.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 5px 5px 0 5px !important;
  border-color: #ffffff transparent transparent transparent !important;
}

/* arrows - left arrow */

.wm-design-template-126.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 6px 6px 6px 0 !important;
  border-color: transparent #dce1e7 transparent transparent !important;
  margin-left: 5px !important;
}

.wm-design-template-126.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 5px 5px 5px 0 !important;
  border-color: transparent #ffffff transparent transparent !important;
  margin-left: 5px !important;
} /* Dark balloon with Next and Back Button Default */

.wm-design-template-1506 .walkme-custom-side-border {
  display: none !important;
}

.wm-design-template-1506.walkme-custom-balloon-outer-div {
  min-width: 240px !important;
  max-width: 380px !important;
  -webkit-border-radius: 3px !important;
  -moz-border-radius: 3px !important;
  border-radius: 3px !important;
  background-color: #1F2532 !important;
}

.wm-design-template-1506.walkme-custom-balloon-outer-div.walkme-custom-popup-step {
  min-width: 360px !important;
  max-width: 420px !important;
}

.wm-design-template-1506 .walkme-custom-balloon-top-div {
  -webkit-border-radius: 3px !important;
  -moz-border-radius: 3px !important;
  border-radius: 3px !important;
  background-color: #1F2532 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-mid-div,
.wm-design-template-1506 .walkme-custom-balloon-inner-div {
  -webkit-border-radius: 3px !important;
  -moz-border-radius: 3px !important;
  border-radius: 3px !important;
}

.wm-design-template-1506 .walkme-custom-balloon-mid-div {
  background-color: #1F2532 !important;
  -webkit-box-shadow: 0 2px 4px 0 #A3A3A3 !important;
  -moz-box-shadow: 0 2px 4px 0 #A3A3A3 !important;
  box-shadow: 0 2px 4px 0 #A3A3A3 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-inner-div {
  border-width: 0 !important;
  background-color: #1F2532 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-close-button {
  padding: 0 !important;
  margin: 3px 7px 0 0 !important;
  color: #fff !important;
  font-weight: bold !important;
  font-size: 16px !important;
}

.wm-design-template-1506 .walkme-custom-balloon-title {
  margin-bottom: 6px !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  color: #1DE9B6 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-content {
  margin-bottom: 5px !important;
  font-weight: normal !important;
  color: #fff !important;
}

.wm-design-template-1506 .walkme-custom-balloon-separator {
  display: none !important;
}

.wm-design-template-1506 .walkme-custom-balloon-bottom-div {
  position: relative !important;
  height: 44px !important;
  margin-top: 15px !important;
  background-color: #1F2532 !important;
}

.wm-design-template-1506.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  height: 36px !important;
}

/* buttons */

.wm-design-template-1506 .walkme-custom-balloon-top-div-bottom {
  position: relative !important;
  z-index: 100 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-buttons-wrapper {
  padding: 0 16px 0 16px !important;
  margin: 0 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-button {
  height: 22px !important;
}

.wm-design-template-1506 .walkme-custom-balloon-back-button {
  float: left !important;
  margin: 6px 0 !important;
  color: #1DE9B6 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-back-button:hover {
  color: #14CBA8 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-next-button,
.wm-design-template-1506 .walkme-custom-balloon-done-button,
.wm-design-template-1506 .walkme-custom-balloon-start-button {
  width: 44px !important;
  margin: 6px 0 !important;
  padding-bottom: 2px !important;
  border: 1px solid #1DE9B6 !important;
  -webkit-border-radius: 3px !important;
  -moz-border-radius: 3px !important;
  border-radius: 3px !important;
  background-color: #1F2532 !important;
  color: #1DE9B6 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-next-button:hover,
.wm-design-template-1506 .walkme-custom-balloon-done-button:hover,
.wm-design-template-1506 .walkme-custom-balloon-start-button:hover {
  border-color: #14CBA8 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-next-button:hover .walkme-custom-balloon-button-text,
.wm-design-template-1506 .walkme-custom-balloon-done-button:hover .walkme-custom-balloon-button-text,
.wm-design-template-1506 .walkme-custom-balloon-start-button:hover .walkme-custom-balloon-button-text {
  color: #14CBA8 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 600 !important;
}

.wm-design-template-1506 .walkme-custom-balloon-cancel-button {
  margin-right: 10px !important;
}

.wm-design-template-1506 .walkme-custom-balloon-cancel-button .walkme-custom-balloon-button-text {
  color: #fff !important;
}

.wm-design-template-1506 .walkme-custom-balloon-cancel-button:hover .walkme-custom-balloon-button-text {
  color: #9a9a9a !important;
}

/* powered by walkme */

.wm-design-template-1506 .walkme-custom-powered-by-div {
  float: left !important;
  font-size: 11px !important;
  margin: 7px 0 !important;
}

.wm-design-template-1506 .walkme-custom-powered-by {
  color: #9A9A9A !important;
}

.wm-design-template-1506 .walkme-custom-powered-by:hover,
.wm-design-template-1506 .walkme-custom-powered-by:active {
  color: #9A9A9A !important;
}

/* step count */

.wm-design-template-1506 .walkme-custom-balloon-subtext {
  position: absolute !important;
  width: 100% !important;
  padding: 0 !important;
  margin: 10px 0 0 0 !important;
  font-size: 10px !important;
  text-align: center !important;
  color: #1DE9B6 !important;
}

.wm-design-template-1506.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-subtext {
  margin-top: 7px !important;
}

/* arrows - need to be set up with border-width: 1px on Customize */

/* arrows - top arrow */

.wm-design-template-1506.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 0 7px 6px 7px !important;
  border-color: transparent transparent #1F2532 !important;
  margin-top: 4px !important;
}

.wm-design-template-1506.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 0 6px 5px 6px !important;
  border-color: transparent transparent #1F2532 !important;
  margin-top: 4px !important;
}

/* arrows - right arrow */

.wm-design-template-1506.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 7px 0 7px 6px !important;
  border-color: transparent transparent transparent #1F2532 !important;
  margin-left: 1px !important;
}

.wm-design-template-1506.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 6px 0 6px 6px !important;
  border-color: transparent transparent transparent #1F2532 !important;
  margin-left: 1px !important;
}

/* arrows - bottom arrow */

.wm-design-template-1506.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 6px 7px 0 7px !important;
  border-color: #1F2532 transparent transparent transparent !important;
  margin-top: 1px !important;
}

.wm-design-template-1506.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 5px 6px 0 6px !important;
  border-color: #1F2532 transparent transparent transparent !important;
  margin-top: 1px !important;
}

/* arrows - left arrow */

.wm-design-template-1506.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-style: solid !important;
  border-width: 7px 6px 7px 0 !important;
  border-color: transparent #1F2532 transparent transparent !important;
  margin-left: 4px !important;
}

.wm-design-template-1506.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-style: solid !important;
  border-width: 6px 5px 6px 0 !important;
  border-color: transparent #1F2532 transparent transparent !important;
  margin-left: 4px !important;
} /* Custom Balloons -- START */

.wm-design-template-1507 .walkme-custom-balloon-mid-div {
  box-shadow: none !important;
  border-radius: 0 !important;
}

.wm-design-template-1507 .walkme-custom-balloon-inner-div {
  background-color: #333333 !important;
  border: none !important;
  border-radius: 0 !important;
}

.wm-design-template-1507 .walkme-custom-balloon-top-div {
  background-color: #333333 !important;
  border-radius: 0 !important;
}

.wm-design-template-1507 .walkme-custom-balloon-content-wrapper {
  min-height: 53px !important;
}

/* X */

.wm-design-template-1507 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  color: rgba(255, 255, 255, 0.5) !important;
}

.wm-design-template-1507 .walkme-click-and-hover.walkme-custom-balloon-close-button:hover,
.wm-design-template-1507 .walkme-click-and-hover.walkme-custom-balloon-close-button:active {
  color: #ffffff !important;
}

/* Text */

.wm-design-template-1507 .walkme-custom-balloon-title,
.wm-design-template-1507 .walkme-custom-balloon-content {
  color: #ffffff !important;
}

.wm-design-template-1507 .walkme-custom-balloon-title {
  padding: 8px 2px 0 !important;
  margin-left: 13px !important;
  margin-right: 13px !important;
}

.wm-design-template-1507 .walkme-custom-balloon-content {
  margin: 2px 15px 0 !important;
}

/* Footer */

.wm-design-template-1507 .walkme-custom-balloon-separator {
  margin: 2px 0 0 !important;
  background-color: transparent !important;
}

.wm-design-template-1507 .walkme-custom-balloon-bottom-div {
  background-color: #333333 !important;
}

.wm-design-template-1507 .walkme-custom-balloon-subtext {
  color: rgba(255, 255, 255, 0.5) !important;
}

/* Buttons */

.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  background-color: #ffffff !important;
}

.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: rgba(255, 255, 255, 0.9) !important;
}

.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  color: #333333 !important;
}

.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text:hover {
  color: rgba(255, 255, 255, 0.9) !important;
}

.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-done-button,
.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-next-button {
  margin: 6px 0 6px 6px !important;
  float: right !important;
}

.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-done-button .walkme-custom-balloon-button-text,
.wm-design-template-1507 .walkme-custom-balloon-button.walkme-custom-balloon-next-button .walkme-custom-balloon-button-text {
  text-transform: uppercase !important;
}

/* Side Border */

.wm-design-template-1507 .walkme-custom-side-border {
  display: none !important;
}

/* Alternate Styles */

.wm-design-template-1507.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-separator {
  margin: 4px 0 0 !important;
}

.wm-design-template-1507.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-content-wrapper {
  min-height: 30px !important;
}

/* Arrows */

/* Left Arrow Color */

.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner,
.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #333333 transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner,
.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #333333 !important;
}

/* Top Arrow Color */

.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner,
.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent #333333 !important;
}

/* Bottom Arrow inner fill color */

.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner,
.wm-design-template-1507.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #333333 transparent transparent !important;
}

/* Custom Global Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-1508.walkme-custom-balloon-outer-div {
  min-width: 330px !important;
}

.wm-design-template-1508.walkme-custom-balloon-outer-div.walkme-custom-popup-step {
  min-width: 430px !important;
}

.wm-design-template-1508 .walkme-custom-balloon-separator,
.wm-design-template-1508 .walkme-custom-balloon-bottom-div,
.wm-design-template-1508 .walkme-custom-balloon-inner-div,
.wm-design-template-1508 .walkme-custom-balloon-top-div {
  background-color: #3393d1 !important;
}

.wm-design-template-1508 .walkme-custom-balloon-inner-div {
  border: 2px solid #3393d1 !important;
}

.wm-design-template-1508 .walkme-custom-balloon-inner-div,
.wm-design-template-1508 .walkme-custom-balloon-mid-div {
  overflow: visible !important;
}

.wm-design-template-1508 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 13px 0 rgba(0, 0, 0, 0.4) !important;
}

.wm-design-template-1508 .walkme-custom-side-border {
  display: none !important;
}

/* X */

.wm-design-template-1508 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  right: -12px !important;
  top: -12px !important;
  margin: 6px 4px 0 !important;
  padding: 0 5px !important;
  background: #ffffff !important;
  -webkit-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  -moz-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  border: 2px solid #3393d1 !important;
  border-radius: 100% !important;
  font-size: 12px !important;
  color: #3393d1 !important;
}

.wm-design-template-1508 .walkme-click-and-hover.walkme-custom-balloon-close-button:hover {
  right: -12px !important;
  top: -12px !important;
  margin: 6px 4px 0 !important;
  padding: 0 5px !important;
  background: #3393d1 !important;
  -webkit-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  -moz-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  border: 2px solid #3393d1 !important;
  border-radius: 100% !important;
  transition: background 200ms ease 0s !important;
  font-size: 12px !important;
  color: #ffffff !important;
}

/* Title */

.wm-design-template-1508 .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 16px 18px 0 18px !important;
  font-weight: 100 !important;
  line-height: 1.7 !important;
  color: #ffffff !important;
}

/* Content */

.wm-design-template-1508 .walkme-custom-balloon-content {
  padding: 2px !important;
  margin: 13px 18px !important;
  font-weight: 300 !important;
  line-height: 1.7 !important;
  font-size: 13px !important;
  color: #ffffff !important;
}

.wm-design-template-1508 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-1508 .walkme-custom-balloon-subtext {
  position: absolute !important;
  width: 100% !important;
  padding: 0 !important;
  margin: 6px 0 0 0 !important;
  text-align: center !important;
  font-size: 10px !important;
  color: #FFF !important;
}

.wm-design-template-1508 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-1508 .walkme-custom-powered-by-div {
  margin-right: 8px !important;
}

.wm-design-template-1508 .walkme-custom-powered-by-div a.walkme-custom-powered-by {
  color: #ffffff !important;
}

.wm-design-template-1508 .walkme-custom-balloon-top-div-bottom {
  position: relative !important;
  z-index: 100 !important;
}

/* Buttons */

/* Next button styles */

.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button.walkme-custom-balloon-back-button:hover {
  width: 89px !important;
  height: 25px !important;
  margin: 0px 20px 20px 20px !important;
  padding: 1px 5px 2px 5px !important;
  background: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 15px !important;
  transition: background 200ms ease 0s !important;
}

.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover,
.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button.walkme-custom-balloon-back-button {
  width: 89px !important;
  height: 25px !important;
  margin: 0px 20px 20px 20px !important;
  padding: 1px 5px 2px 5px !important;
  background: #3393d1 !important;
  border: 2px solid #ffffff !important;
  border-radius: 15px !important;
  transition: background 200ms ease 0s !important;
}

.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button.walkme-custom-balloon-back-button {
  float: left !important;
}

.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-normal-button span.walkme-custom-balloon-button-text,
.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button.walkme-custom-balloon-back-button:hover span.walkme-custom-balloon-button-text {
  font-size: 12px !important;
  color: #3393d1 !important;
}

.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover span.walkme-custom-balloon-button-text,
.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button.walkme-custom-balloon-back-button span.walkme-custom-balloon-button-text {
  font-size: 12px !important;
  color: #ffffff !important;
}

.wm-design-template-1508 .walkme-custom-balloon-button.walkme-custom-balloon-weak-button.walkme-custom-balloon-cancel-button {
  margin-top: 3px !important;
  color: #fff !important;
}

/* Arrow syles for balloons */

/* arrow at the top of the Balloon inner fill color */

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #3393d1 !important;
}

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent #3393d1 !important;
}

/* arrow at the bottom of the Balloon outer fill color */

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #3393d1 transparent !important;
}

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #3393d1 transparent transparent !important;
}

/* arrow at the right of the Balloon outer fill color */

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #3393d1 !important;
}

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #3393d1 !important;
}

/* arrow at the left of the Balloon outer fill color */

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #3393d1 transparent transparent  !important;
}

.wm-design-template-1508.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #3393d1 transparent transparent  !important;
}

/* Alternative Balloon Styles */

/* No Title */

.wm-design-template-1508.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 6px !important;
}

/* No Content */

.wm-design-template-1508.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  padding-bottom: 10px !important;
}

/* Theme 3 Balloon Styles -- END */ /* Custom Balloons -- START */

.wm-design-template-1509.walkme-custom-balloon-outer-div,
.wm-design-template-1509 .walkme-custom-balloon-mid-div,
.wm-design-template-1509 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div,
.wm-design-template-1509 .walkme-custom-balloon-mid-div,
.wm-design-template-1509 .walkme-custom-balloon-inner-div,
.wm-design-template-1509 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-1509 .walkme-custom-balloon-mid-div,
.wm-design-template-1509 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-1509 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-1509 .walkme-custom-balloon-inner-div,
.wm-design-template-1509 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-1509 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-1509 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-1509 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-1509 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-1509 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-1509 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-1509 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-1509 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-1509 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-1509 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-1509.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-1509.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-1509 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-1509 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-1509.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-1509.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-1509.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-1509.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-1509.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* white basic SO */

.wm-design-template-7722.wm-outer-div {
  width: auto !important;
  max-width: 500px !important;
  padding: 200px 85px 40px 85px !important;
  -webkit-border-radius: 2px !important;
  -moz-border-radius: 2px !important;
  border-radius: 2px !important;
  background: #fff url('https://cdn.walkme.com/player/resources/images/templates/illustration-telescope.png') no-repeat center 40px !important;
  -webkit-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
}

.wm-design-template-7722 .wm-title {
  margin-bottom: 11px !important;
  color: #1B2432 !important;
  font-size: 18px !important;
  font-weight: normal !important;
  text-align: center !important;
  text-transform: uppercase !important;
}

.wm-design-template-7722 .wm-title b,
.wm-design-template-7722 .wm-title u,
.wm-design-template-7722 .wm-title i,
.wm-design-template-7722 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
  text-transform: inherit !important;
}

.wm-design-template-7722 .wm-title b {
  font-weight: bold !important;
}

.wm-design-template-7722 .wm-close-button {
  right: 8px !important;
  top: 3px !important;
  color: #D8D8D8 !important;
}

.wm-design-template-7722 .wm-close-button:hover {
  color: #AFAFAF !important;
}

.wm-design-template-7722 .wm-template-text {
  font-size: 14px !important;
  font-weight: normal !important;
  color: #5F5F5F !important;
  text-align: center !important;
}

.wm-design-template-7722 .wm-template-text b,
.wm-design-template-7722 .wm-template-text u,
.wm-design-template-7722 .wm-template-text i,
.wm-design-template-7722 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-7722 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-7722 .buttons-wrapper {
  display: table !important;
  margin: 80px auto 0 auto !important;
}

.wm-design-template-7722 .wm-blue-btn {
  float: left !important;
  padding: 0 !important;
  margin: 0 !important;
  background: #fff !important;
  color: #DA7A60 !important;
  font-size: 14px !important;
  font-weight: normal !important;
  text-transform: uppercase !important;
}

.wm-design-template-7722 .wm-blue-btn:hover {
  color: #9C4F3A !important;
}

.wm-design-template-7722 .wm-close-link {
  float: right !important;
  margin: 0 !important;
  margin-left: 60px !important;
  background: #fff !important;
  font-size: 14px !important;
  font-weight: normal !important;
  color: #5F5F5F !important;
  text-decoration: none !important;
  text-transform: uppercase !important;
}

.wm-design-template-7722 .wm-close-link:hover {
  color: #5F5F5F !important;
}  /* Sunset Gradient Gallery Shoutout -- START */

.wm-design-template-8339.wm-outer-div {
  width: auto !important;
  min-width: 400px !important;
  max-width: 500px !important;
  padding: 0 !important;
  background: #fbcf71 !important;
  background: -moz-linear-gradient(45deg, #fbcf71 0%, #f35b69 87%) !important;
  background: -webkit-linear-gradient(45deg, #fbcf71 0%,#f35b69 87%)!important;
  background: linear-gradient(45deg, #fbcf71 0%,#f35b69 87%)!important;
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fbcf71', endColorstr='#f35b69',GradientType=1 )!important;
}

/* X */

.wm-design-template-8339 .wm-close-button.walkme-x-button {
  -webkit-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  -moz-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  background: #fff !important;
  border-radius: 100% !important;
  padding: 3px 7px 5px 7px !important;
  font-size: 12px !important;
  margin: -15px -22px 0px !important;
  color: #f5766b !important;
  border: 2px solid #f5766b !important;
  transition: background 200ms ease 0s !important;
}

.wm-design-template-8339 .wm-close-button.walkme-x-button:hover {
  background: #f5766b !important;
  border-radius: 100% !important;
  padding: 3px 7px 5px 7px !important;
  font-size: 12px !important;
  margin: -15px -22px 0px !important;
  color: #fff !important;
  border: 2px solid #fff !important;
  transition: background 200ms ease 0s !important;
}

/* Title */

.wm-design-template-8339 .wm-title.wm-template-main-text {
  margin: 74px 40px 74px !important;
  text-align: center !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-8339 .wm-title b,
.wm-design-template-8339 .wm-title u,
.wm-design-template-8339 .wm-title i,
.wm-design-template-8339 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-8339 .wm-title b {
  font-weight: bold !important;
}

/* Content */

.wm-design-template-8339 .wm-content {
  background: #fff !important;
  padding-bottom: 50px !important;
}

.wm-design-template-8339 .wm-content .wm-template-text {
  padding-top: 30px !important;
  padding-bottom: 10px !important;
  text-align: center !important;
  padding-left: 35px !important;
  padding-right: 35px !important;
}

.wm-design-template-8339 .wm-content .wm-template-text,
.wm-design-template-8339 .wm-content .wm-template-text * {
  text-align: center !important;
  font-size: 13px !important;
  font-weight: 100 !important;
  line-height: normal !important;
  color: #333 !important;
  background-color: #fff !important;
}

.wm-design-template-8339 .wm-template-text b,
.wm-design-template-8339 .wm-template-text u,
.wm-design-template-8339 .wm-template-text i,
.wm-design-template-8339 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-8339 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-8339 .buttons-wrapper .wm-blue-btn.wm-template-main-bg {
  min-width: 146px !important;
  float: none !important;
  padding: 6px 18px !important;
  background-color: #f5766b  !important;
  border: 2px solid #f5766b !important;
  border-radius: 18px !important;
  text-align: center !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #fff !important;
  margin-top: 20px !important;
  max-width: 450px !important;
}

.wm-design-template-8339 .buttons-wrapper {
  display: table !important;
  margin: -4px auto -30px auto !important;
  text-align: center !important;
  background-color: #fff !important;
}

.wm-design-template-8339 .buttons-wrapper .wm-blue-btn {
  float: none !important;
  padding: 9px 20px !important;
  -webkit-border-radius: 2px !important;
  -moz-border-radius: 2px !important;
  border-radius: 2px !important;
  margin: 0 !important;
  border: 1px solid #333 !important;
  background-color: #A952F6 !important;
  color: #333 !important;
  font-size: 14px !important;
  font-weight: normal !important;
}

.wm-design-template-8339 .buttons-wrapper .wm-blue-btn:hover {
  background-color: #fff !important;
  border: 2px solid #f5766b !important;
  color: #f5766b !important;
}

.wm-design-template-8339 .buttons-wrapper .wm-close-link {
  float: none !important;
  display: block !important;
  margin: 15px 0px 0px 0px !important;
  min-width: 35px !important;
  float: none !important;
  display: block !important;
  background-color: transparent !important;
  border: none !important;
  text-align: center !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  text-decoration: none !important;
  color: #a1a1a2 !important;
  text-decoration: underline !important;
}

.wm-design-template-8339 .buttons-wrapper .wm-close-link:hover {
  opacity: .7 !important;
  transition: background 200ms ease 0s !important;
} /* WalkMe ShoutOut Error Banner Design --- START */

.wm-design-template-8343.wm-outer-div {
  width: 100% !important;
  margin: 0px !important;
  padding: 10px 0px 0px 0px !important;
  background-color: #B00707 !important;
  background-image: url("https://s3-us-west-1.amazonaws.com/walkme.external/CSSAutoGen/error_icon.png") !important;
  background-repeat: no-repeat !important;
  background-position: 20px 52.5% !important;
  min-height: 50px !important;
}

.wm-design-template-8343.wm-outer-div.wm-position-top,
.wm-design-template-8343.wm-outer-div.wm-position-center,
.wm-design-template-8343.wm-outer-div.wm-position-bottom {
  left: 0px !important;
}

/* Title Styles */

.wm-design-template-8343 .wm-title.wm-template-main-text {
  display: none !important;
}

/* Body Text Styles */

.wm-design-template-8343 .wm-template-text {
  margin: 10px 0px 0px 60px !important;
  color: #fff !important;
  width: 65% !important;
  display: inline-block !important;
  float: left !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

.wm-design-template-8343 .wm-template-text b,
.wm-design-template-8343 .wm-template-text u,
.wm-design-template-8343 .wm-template-text i,
.wm-design-template-8343 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-8343 .wm-template-text b {
  font-weight: bold !important;
}

/* Button Styles */

.wm-design-template-8343 .buttons-wrapper {
  float: right !important;
  display: inline-block !important;
  margin: 6px 30px 0px 0px !important;
}

.wm-design-template-8343 .wm-blue-btn {
  background-color: #B00707 !important;
  color: #fff !important;
  padding: 5px 10px 5px !important;
  border: 1px solid #fff !important;
}

.wm-design-template-8343 .wm-blue-btn:hover {
  background-color: #fff !important;
  color: #B00707 !important;
  padding: 5px 10px 5px !important;
  border: 1px solid #B00707 !important;
}

/* X Button Styles */

.wm-design-template-8343 .wm-close-button {
  font-size: 0px !important;
  right: 27px !important;
}

.wm-design-template-8343 .wm-close-button:before {
  content: "" !important;
  position: absolute !important;
  background: url("https://s3-us-west-1.amazonaws.com/walkme.external/CSSAutoGen/x_btn_white.png") no-repeat center !important;
  width: 22px !important;
  height: 22px !important;
  margin: 0px 0px 0px 0px !important;
}

.wm-design-template-8343 .buttons-wrapper .wm-close-link {
  display: none !important;
}

/* Media Querie */

@media only screen and (max-width : 768px) {
  .wm-design-template-8343 .wm-template-text {
    margin: 10px 0px 0px 60px !important;
    color: #fff !important;
    width: 60% !important;
    display: inline-block !important;
    float: left !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
  }
}

@media only screen and (max-width : 621px) {
  .wm-design-template-8343 .wm-template-text {
    margin: 10px 0px 0px 60px !important;
    color: #fff !important;
    width: 45% !important;
    display: inline-block !important;
    float: left !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
  }
}

@media only screen and (max-width : 440px) {
  .wm-design-template-8343 .wm-template-text {
    margin: 10px 0px 0px 60px !important;
    color: #fff !important;
    width: 40% !important;
    display: inline-block !important;
    float: left !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
  }
}

@media only screen and (max-width : 321px) {
  .wm-design-template-8343 .wm-template-text {
    margin: 10px 0px 0px 60px !important;
    color: #fff !important;
    width: 35% !important;
    display: inline-block !important;
    float: left !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
  }
}

/* WalkMe ShoutOut Error Banner Design --- END */ /* white basic SO */

.wm-design-template-8363.wm-outer-div {
  width: auto !important;
  max-width: 500px !important;
  padding: 46px 60px 30px 58px !important;
  -webkit-border-radius: 5px !important;
  -moz-border-radius: 5px !important;
  border-radius: 5px !important;
  background-color: #fff !important;
  -webkit-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
}

.wm-design-template-8363 .wm-title {
  margin-bottom: 9px !important;
  color: #39C2FF !important;
  font-size: 18px !important;
  font-weight: normal !important;
  text-align: center !important;
}

.wm-design-template-8363 .wm-title b,
.wm-design-template-8363 .wm-title u,
.wm-design-template-8363 .wm-title i,
.wm-design-template-8363 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-8363 .wm-title b {
  font-weight: bold !important;
}

.wm-design-template-8363 .wm-close-button {
  right: 8px !important;
  top: 3px !important;
  color: #D8D8D8 !important;
}

.wm-design-template-8363 .wm-close-button:hover {
  color: #AFAFAF !important;
}

.wm-design-template-8363 .wm-template-text {
  font-size: 14px !important;
  font-weight: normal !important;
  color: #919191 !important;
  text-align: center !important;
}

.wm-design-template-8363 .wm-template-text b,
.wm-design-template-8363 .wm-template-text u,
.wm-design-template-8363 .wm-template-text i,
.wm-design-template-8363 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-8363 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-8363 .buttons-wrapper {
  display: table !important;
  margin: 32px auto 0 auto !important;
}

.wm-design-template-8363 .wm-blue-btn {
  float: right !important;
  padding: 10px 30px !important;
  margin: 0 !important;
  -webkit-border-radius: 26px !important;
  -moz-border-radius: 26px !important;
  border-radius: 26px !important;
  background-color: #39C2FF !important;
  color: #fff !important;
  font-size: 14px !important;
  font-weight: 500 !important;
}

.wm-design-template-8363 .wm-blue-btn:hover {
  background-color: #1E9AD1 !important;
}

.wm-design-template-8363 .wm-close-link {
  float: left !important;
  padding: 10px 30px !important;
  margin: 0 !important;
  margin-right: 40px !important;
  font-size: 14px !important;
  font-weight: normal !important;
  color: #AFAFAF !important;
  text-decoration: none !important;
}

.wm-design-template-8363 .wm-close-link:hover {
  color: #929292 !important;
} /* SFDC Gradient Gallery Shoutout -- START */

.wm-design-template-9802.wm-outer-div {
  width: auto !important;
  min-width: 400px !important;
  max-width: 500px !important;
  padding: 0 !important;
  background: #2e96f2 !important;
  /* Old browsers */
  background: -moz-linear-gradient(45deg, #2e96f2 0%, #2989d8 49%, #1e5799 98%) !important;
  /* FF3.6-15 */
  background: -webkit-linear-gradient(45deg, #2e96f2 0%,#2989d8 49%,#1e5799 98%) !important;
  /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(45deg, #2e96f2 0%,#2989d8 49%,#1e5799 98%) !important;
  /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
}

/* X */

.wm-design-template-9802 .wm-close-button.walkme-x-button {
  -webkit-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  -moz-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  background: #fff !important;
  border-radius: 100% !important;
  padding: 3px 7px 5px 7px !important;
  font-size: 12px !important;
  margin: -15px -22px 0px !important;
  color: #3393D1 !important;
  border: 2px solid #3393D1 !important;
  transition: background 200ms ease 0s !important;
}

.wm-design-template-9802 .wm-close-button.walkme-x-button:hover {
  background: #3393D1 !important;
  border-radius: 100% !important;
  padding: 3px 7px 5px 7px !important;
  font-size: 12px !important;
  margin: -15px -22px 0px !important;
  color: #fff !important;
  border: 2px solid #fff !important;
  transition: background 200ms ease 0s !important;
}

/* Title */

.wm-design-template-9802 .wm-title.wm-template-main-text {
  margin: 74px 40px 74px !important;
  text-align: center !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-9802 .wm-title b,
.wm-design-template-9802 .wm-title u,
.wm-design-template-9802 .wm-title i,
.wm-design-template-9802 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-9802 .wm-title b {
  font-weight: bold !important;
}

/* Content */

.wm-design-template-9802 .wm-content {
  background: #fff !important;
  padding-bottom: 50px !important;
}

.wm-design-template-9802 .wm-content .wm-template-text {
  padding-top: 30px !important;
  padding-bottom: 10px !important;
  text-align: center !important;
  padding-left: 35px !important;
  padding-right: 35px !important;
}

.wm-design-template-9802 .wm-content .wm-template-text,
.wm-design-template-9802 .wm-content .wm-template-text * {
  text-align: center !important;
  font-size: 13px !important;
  font-weight: 100 !important;
  line-height: normal !important;
  color: #333 !important;
  background-color: #fff !important;
}

.wm-design-template-9802 .wm-template-text b,
.wm-design-template-9802 .wm-template-text u,
.wm-design-template-9802 .wm-template-text i,
.wm-design-template-9802 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-9802 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-9802 .buttons-wrapper .wm-blue-btn.wm-template-main-bg {
  min-width: 146px !important;
  float: none !important;
  padding: 6px 18px !important;
  background-color: #3393D1  !important;
  border: 2px solid #3393D1 !important;
  border-radius: 18px !important;
  text-align: center !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #fff !important;
  margin-top: 20px !important;
  max-width: 450px !important;
}

.wm-design-template-9802 .buttons-wrapper {
  display: table !important;
  margin: -4px auto -30px auto !important;
  text-align: center !important;
  background-color: #fff !important;
}

.wm-design-template-9802 .buttons-wrapper .wm-blue-btn {
  float: none !important;
  padding: 9px 20px !important;
  -webkit-border-radius: 2px !important;
  -moz-border-radius: 2px !important;
  border-radius: 2px !important;
  margin: 0 !important;
  border: 1px solid #333 !important;
  background-color: #A952F6 !important;
  color: #333 !important;
  font-size: 14px !important;
  font-weight: normal !important;
}

.wm-design-template-9802 .buttons-wrapper .wm-blue-btn:hover {
  background-color: #fff !important;
  border: 2px solid #3393D1 !important;
  color: #3393D1 !important;
}

.wm-design-template-9802 .buttons-wrapper .wm-close-link {
  float: none !important;
  display: block !important;
  margin: 15px 0px 0px 0px !important;
  min-width: 35px !important;
  float: none !important;
  display: block !important;
  background-color: transparent !important;
  border: none !important;
  text-align: center !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  text-decoration: none !important;
  color: #a1a1a2 !important;
  text-decoration: underline !important;
}

.wm-design-template-9802 .buttons-wrapper .wm-close-link:hover {
  opacity: .7 !important;
  transition: background 200ms ease 0s !important;
} /* white basic SO */

.wm-design-template-12476.wm-outer-div {
  width: auto !important;
  max-width: 500px !important;
  padding: 46px 60px 30px 58px !important;
  -webkit-border-radius: 5px !important;
  -moz-border-radius: 5px !important;
  border-radius: 5px !important;
  background-color: #fff !important;
  -webkit-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-sizing: border-box !important;
  box-sizing: border-box !important;
}

.wm-design-template-12476 .wm-title {
  margin-bottom: 9px !important;
  color: #39C2FF !important;
  font-size: 18px !important;
  font-weight: normal !important;
  text-align: center !important;
}

.wm-design-template-12476 .wm-title b,
.wm-design-template-12476 .wm-title u,
.wm-design-template-12476 .wm-title i,
.wm-design-template-12476 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12476 .wm-title b {
  font-weight: bold !important;
}

.wm-design-template-12476 .wm-close-button {
  right: 8px !important;
  top: 3px !important;
  color: #D8D8D8 !important;
}

.wm-design-template-12476 .wm-close-button:hover {
  color: #AFAFAF !important;
}

.wm-design-template-12476 .wm-template-text {
  font-size: 14px !important;
  font-weight: normal !important;
  color: #919191 !important;
  text-align: center !important;
}

.wm-design-template-12476 .wm-template-text b,
.wm-design-template-12476 .wm-template-text u,
.wm-design-template-12476 .wm-template-text i,
.wm-design-template-12476 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12476 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-12476 .buttons-wrapper {
  display: table !important;
  margin: 32px auto 0 auto !important;
}

.wm-design-template-12476 .wm-blue-btn {
  float: right !important;
  padding: 10px 30px !important;
  margin: 0 !important;
  -webkit-border-radius: 26px !important;
  -moz-border-radius: 26px !important;
  border-radius: 26px !important;
  background-color: #39C2FF !important;
  color: #fff !important;
  font-size: 14px !important;
  font-weight: 500 !important;
}

.wm-design-template-12476 .wm-blue-btn:hover {
  background-color: #1E9AD1 !important;
}

.wm-design-template-12476 .wm-close-link {
  float: left !important;
  padding: 10px 30px !important;
  margin: 0 !important;
  margin-right: 40px !important;
  font-size: 14px !important;
  font-weight: normal !important;
  color: #AFAFAF !important;
  text-decoration: none !important;
}

.wm-design-template-12476 .wm-close-link:hover {
  color: #929292 !important;
} /* white basic SO */

.wm-design-template-12478.wm-outer-div {
  width: auto !important;
  max-width: 500px !important;
  padding: 38px 30px 40px 30px !important;
  -webkit-border-radius: 2px !important;
  -moz-border-radius: 2px !important;
  border-radius: 2px !important;
  background-color: #00C3FF !important;
  -webkit-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-sizing: border-box !important;
  box-sizing: border-box !important;
}

.wm-design-template-12478 .wm-title {
  margin-bottom: 9px !important;
  color: #fff !important;
  font-size: 18px !important;
  font-weight: 500 !important;
  text-align: center !important;
}

.wm-design-template-12478 .wm-title b,
.wm-design-template-12478 .wm-title u,
.wm-design-template-12478 .wm-title i,
.wm-design-template-12478 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12478 .wm-title b {
  font-weight: bold !important;
}

.wm-design-template-12478 .wm-close-button {
  right: 8px !important;
  top: 3px !important;
  color: #fff !important;
}

.wm-design-template-12478 .wm-close-button:hover {
  color: #fff !important;
}

.wm-design-template-12478 .wm-template-text {
  font-size: 14px !important;
  font-weight: normal !important;
  color: #fff !important;
  text-align: center !important;
}

.wm-design-template-12478 .wm-template-text b,
.wm-design-template-12478 .wm-template-text u,
.wm-design-template-12478 .wm-template-text i,
.wm-design-template-12478 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12478 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-12478 .buttons-wrapper {
  display: table !important;
  margin: 43px auto 0 auto !important;
}

.wm-design-template-12478 .wm-blue-btn {
  float: left !important;
  padding: 5px 12px !important;
  margin: 0 !important;
  -webkit-border-radius: 26px !important;
  -moz-border-radius: 26px !important;
  border-radius: 26px !important;
  border: 1px solid #fff !important;
  background-color: #fff !important;
  color: #00C3FF !important;
  font-size: 12px !important;
  font-weight: 500 !important;
}

.wm-design-template-12478 .wm-blue-btn:hover {
  background-color: #00C3FF  !important;
  color: #fff !important;
}

.wm-design-template-12478 .wm-close-link {
  float: right !important;
  padding: 5px 12px !important;
  margin: 0 !important;
  margin-left: 22px !important;
  border: 1px solid #fff !important;
  -webkit-border-radius: 26px !important;
  -moz-border-radius: 26px !important;
  border-radius: 26px !important;
  background-color: #00C3FF  !important;
  font-size: 12px !important;
  font-weight: normal !important;
  color: #fff !important;
  text-decoration: none !important;
}

.wm-design-template-12478 .wm-close-link:hover {
  background-color: #fff !important;
  color: #00C3FF !important;
} /* SFDC Gradient Gallery Shoutout -- START */

.wm-design-template-12479.wm-outer-div {
  width: auto !important;
  min-width: 400px !important;
  max-width: 500px !important;
  padding: 0 !important;
  background: #2e96f2 !important;
  -moz-box-sizing: border-box !important;
  box-sizing: border-box !important;
  /* Old browsers */
  background: -moz-linear-gradient(45deg, #2e96f2 0%, #2989d8 49%, #1e5799 98%) !important;
  /* FF3.6-15 */
  background: -webkit-linear-gradient(45deg, #2e96f2 0%,#2989d8 49%,#1e5799 98%) !important;
  /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(45deg, #2e96f2 0%,#2989d8 49%,#1e5799 98%) !important;
  /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
}

/* X */

.wm-design-template-12479 .wm-close-button.walkme-x-button {
  -webkit-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  -moz-box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  box-shadow: 3px 15px 56px -23px rgba(0,0,0,0.75) !important;
  background: #fff !important;
  border-radius: 100% !important;
  padding: 3px 7px 5px 7px !important;
  font-size: 12px !important;
  margin: -15px -22px 0px !important;
  color: #3393D1 !important;
  border: 2px solid #3393D1 !important;
  transition: background 200ms ease 0s !important;
}

.wm-design-template-12479 .wm-close-button.walkme-x-button:hover {
  background: #3393D1 !important;
  border-radius: 100% !important;
  padding: 3px 7px 5px 7px !important;
  font-size: 12px !important;
  margin: -15px -22px 0px !important;
  color: #fff !important;
  border: 2px solid #fff !important;
  transition: background 200ms ease 0s !important;
}

/* Title */

.wm-design-template-12479 .wm-title.wm-template-main-text {
  margin: 74px 40px 74px !important;
  text-align: center !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-12479 .wm-title b,
.wm-design-template-12479 .wm-title u,
.wm-design-template-12479 .wm-title i,
.wm-design-template-12479 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12479 .wm-title b {
  font-weight: bold !important;
}

/* Content */

.wm-design-template-12479 .wm-content {
  background: #fff !important;
  padding-bottom: 50px !important;
}

.wm-design-template-12479 .wm-content .wm-template-text {
  padding-top: 30px !important;
  padding-bottom: 10px !important;
  text-align: center !important;
  padding-left: 35px !important;
  padding-right: 35px !important;
}

.wm-design-template-12479 .wm-content .wm-template-text,
.wm-design-template-12479 .wm-content .wm-template-text * {
  text-align: center !important;
  font-size: 13px !important;
  font-weight: 100 !important;
  line-height: normal !important;
  color: #333 !important;
  background-color: #fff !important;
}

.wm-design-template-12479 .wm-template-text b,
.wm-design-template-12479 .wm-template-text u,
.wm-design-template-12479 .wm-template-text i,
.wm-design-template-12479 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12479 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-12479 .buttons-wrapper .wm-blue-btn.wm-template-main-bg {
  min-width: 146px !important;
  float: none !important;
  padding: 6px 18px !important;
  background-color: #3393D1  !important;
  border: 2px solid #3393D1 !important;
  border-radius: 18px !important;
  text-align: center !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #fff !important;
  margin-top: 20px !important;
  max-width: 450px !important;
}

.wm-design-template-12479 .buttons-wrapper {
  display: table !important;
  margin: -4px auto -30px auto !important;
  text-align: center !important;
  background-color: #fff !important;
}

.wm-design-template-12479 .buttons-wrapper .wm-blue-btn {
  float: none !important;
  padding: 9px 20px !important;
  -webkit-border-radius: 2px !important;
  -moz-border-radius: 2px !important;
  border-radius: 2px !important;
  margin: 0 !important;
  border: 1px solid #333 !important;
  background-color: #A952F6 !important;
  color: #333 !important;
  font-size: 14px !important;
  font-weight: normal !important;
}

.wm-design-template-12479 .buttons-wrapper .wm-blue-btn:hover {
  background-color: #fff !important;
  border: 2px solid #3393D1 !important;
  color: #3393D1 !important;
}

.wm-design-template-12479 .buttons-wrapper .wm-close-link {
  float: none !important;
  display: block !important;
  margin: 15px 0px 0px 0px !important;
  min-width: 35px !important;
  float: none !important;
  display: block !important;
  background-color: transparent !important;
  border: none !important;
  text-align: center !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  text-decoration: none !important;
  color: #a1a1a2 !important;
  text-decoration: underline !important;
}

.wm-design-template-12479 .buttons-wrapper .wm-close-link:hover {
  opacity: .7 !important;
  transition: background 200ms ease 0s !important;
} /* white basic SO */

.wm-design-template-12480.wm-outer-div {
  width: auto !important;
  max-width: 500px !important;
  padding: 38px 30px 40px 30px !important;
  -webkit-border-radius: 2px !important;
  -moz-border-radius: 2px !important;
  border-radius: 2px !important;
  background-color: #00C3FF !important;
  -webkit-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  box-shadow: 3px 2px 13px 4px rgba(130,131,160,0.2) !important;
  -moz-box-sizing: border-box !important;
  box-sizing: border-box !important;
}

.wm-design-template-12480 .wm-title {
  margin-bottom: 9px !important;
  color: #fff !important;
  font-size: 18px !important;
  font-weight: 500 !important;
  text-align: center !important;
}

.wm-design-template-12480 .wm-title b,
.wm-design-template-12480 .wm-title u,
.wm-design-template-12480 .wm-title i,
.wm-design-template-12480 .wm-title div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12480 .wm-title b {
  font-weight: bold !important;
}

.wm-design-template-12480 .wm-close-button {
  right: 8px !important;
  top: 3px !important;
  color: #fff !important;
}

.wm-design-template-12480 .wm-close-button:hover {
  color: #fff !important;
}

.wm-design-template-12480 .wm-template-text {
  font-size: 14px !important;
  font-weight: normal !important;
  color: #fff !important;
  text-align: center !important;
}

.wm-design-template-12480 .wm-template-text b,
.wm-design-template-12480 .wm-template-text u,
.wm-design-template-12480 .wm-template-text i,
.wm-design-template-12480 .wm-template-text div {
  font-size: inherit !important;
  color: inherit !important;
}

.wm-design-template-12480 .wm-template-text b {
  font-weight: bold !important;
}

.wm-design-template-12480 .buttons-wrapper {
  display: table !important;
  margin: 43px auto 0 auto !important;
}

.wm-design-template-12480 .wm-blue-btn {
  float: left !important;
  padding: 5px 12px !important;
  margin: 0 !important;
  -webkit-border-radius: 26px !important;
  -moz-border-radius: 26px !important;
  border-radius: 26px !important;
  border: 1px solid #fff !important;
  background-color: #fff !important;
  color: #00C3FF !important;
  font-size: 12px !important;
  font-weight: 500 !important;
}

.wm-design-template-12480 .wm-blue-btn:hover {
  background-color: #00C3FF  !important;
  color: #fff !important;
}

.wm-design-template-12480 .wm-close-link {
  float: right !important;
  padding: 5px 12px !important;
  margin: 0 !important;
  margin-left: 22px !important;
  border: 1px solid #fff !important;
  -webkit-border-radius: 26px !important;
  -moz-border-radius: 26px !important;
  border-radius: 26px !important;
  background-color: #00C3FF  !important;
  font-size: 12px !important;
  font-weight: normal !important;
  color: #fff !important;
  text-decoration: none !important;
}

.wm-design-template-12480 .wm-close-link:hover {
  background-color: #fff !important;
  color: #00C3FF !important;
} /* Custom Balloons -- START */

.wm-design-template-13587.walkme-custom-balloon-outer-div,
.wm-design-template-13587 .walkme-custom-balloon-mid-div,
.wm-design-template-13587 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div,
.wm-design-template-13587 .walkme-custom-balloon-mid-div,
.wm-design-template-13587 .walkme-custom-balloon-inner-div,
.wm-design-template-13587 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-13587 .walkme-custom-balloon-mid-div,
.wm-design-template-13587 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-13587 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-13587 .walkme-custom-balloon-inner-div,
.wm-design-template-13587 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-13587 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-13587 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-13587 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-13587 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-13587 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-13587 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-13587 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-13587 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-13587 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-13587 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-13587.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-13587.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-13587 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-13587 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-13587.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-13587.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-13587.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-13587.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-13587.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-16739.walkme-custom-balloon-outer-div,
.wm-design-template-16739 .walkme-custom-balloon-mid-div,
.wm-design-template-16739 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div,
.wm-design-template-16739 .walkme-custom-balloon-mid-div,
.wm-design-template-16739 .walkme-custom-balloon-inner-div,
.wm-design-template-16739 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-16739 .walkme-custom-balloon-mid-div,
.wm-design-template-16739 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-16739 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-16739 .walkme-custom-balloon-inner-div,
.wm-design-template-16739 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-16739 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-16739 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-16739 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-16739 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-16739 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-16739 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-16739 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-16739 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper {
  padding: 0 3px !important;
  margin: 0 !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-16739 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-16739 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-16739.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-16739.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-16739 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-16739 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-16739.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-16739.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-16739.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-16739.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-16739.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-22603.walkme-custom-balloon-outer-div,
.wm-design-template-22603 .walkme-custom-balloon-mid-div,
.wm-design-template-22603 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div,
.wm-design-template-22603 .walkme-custom-balloon-mid-div,
.wm-design-template-22603 .walkme-custom-balloon-inner-div,
.wm-design-template-22603 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-22603 .walkme-custom-balloon-mid-div,
.wm-design-template-22603 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-22603 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-22603 .walkme-custom-balloon-inner-div,
.wm-design-template-22603 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-22603 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-22603 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-22603 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-22603 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-22603 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-22603 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-22603 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-22603 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-22603 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-22603 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-22603.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-22603.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-22603 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-22603 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-22603.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-22603.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-22603.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-22603.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-22603.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */

/* E-LEARN larger width for shoutout balloon -- START */

.wm-design-template-22603 #walkme-balloon-472317 {
  width: 1200px !important;
  min-width: 1200px !important;
  max-width: 1200px !important;
  padding: 10px !important;
}

/* E-LEARN larger width for shoutout balloon * -- END */ /* Custom Balloons -- START */

.wm-design-template-22610.walkme-custom-balloon-outer-div,
.wm-design-template-22610 .walkme-custom-balloon-mid-div,
.wm-design-template-22610 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div,
.wm-design-template-22610 .walkme-custom-balloon-mid-div,
.wm-design-template-22610 .walkme-custom-balloon-inner-div,
.wm-design-template-22610 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-22610 .walkme-custom-balloon-mid-div,
.wm-design-template-22610 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-22610 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-22610 .walkme-custom-balloon-inner-div,
.wm-design-template-22610 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-22610 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-22610 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-22610 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-22610 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-22610 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-22610 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-22610 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-22610 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-22610 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-22610 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-22610.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-22610.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-22610 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-22610 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-22610.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-22610.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-22610.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-22610.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-22610.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */

/* E-LEARN larger width for shoutout balloon -- START */

.wm-design-template-22610 #walkme-balloon-472317 {
  width: 1200px !important;
  min-width: 200px !important;
  max-width: 900px !important;
  padding: 10px !important;
}

/* E-LEARN larger width for shoutout balloon * -- END */ /* Custom Balloons -- START */

.wm-design-template-22611.walkme-custom-balloon-outer-div,
.wm-design-template-22611 .walkme-custom-balloon-mid-div,
.wm-design-template-22611 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div,
.wm-design-template-22611 .walkme-custom-balloon-mid-div,
.wm-design-template-22611 .walkme-custom-balloon-inner-div,
.wm-design-template-22611 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-22611 .walkme-custom-balloon-mid-div,
.wm-design-template-22611 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-22611 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-22611 .walkme-custom-balloon-inner-div,
.wm-design-template-22611 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-22611 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-22611 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-22611 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-22611 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-22611 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-22611 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-22611 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-22611 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-22611 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-22611 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-22611.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-22611.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-22611 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-22611 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-22611.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-22611.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-22611.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-22611.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-22611.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */

/* E-LEARN larger width for shoutout balloon -- START */

.wm-design-template-22611 #walkme-balloon-472317 {
  width: 1200px !important;
  min-width: 600px !important;
}

/* E-LEARN larger width for shoutout balloon * -- END */ /* Custom Balloons -- START */

.wm-design-template-29110.walkme-custom-balloon-outer-div,
.wm-design-template-29110 .walkme-custom-balloon-mid-div,
.wm-design-template-29110 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div,
.wm-design-template-29110 .walkme-custom-balloon-mid-div,
.wm-design-template-29110 .walkme-custom-balloon-inner-div,
.wm-design-template-29110 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-29110 .walkme-custom-balloon-mid-div,
.wm-design-template-29110 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-29110 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-29110 .walkme-custom-balloon-inner-div,
.wm-design-template-29110 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-29110 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-29110 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-29110 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-29110 .walkme-custom-balloon-content {
  margin: 15px 5px 5px !important;
  font-size: 12px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-29110 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-29110 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-29110 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-29110 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-29110 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-29110 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-29110.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-29110.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-29110 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-29110 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-29110.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-29110.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-29110.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-29110.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-29110.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-38289.walkme-custom-balloon-outer-div,
.wm-design-template-38289 .walkme-custom-balloon-mid-div,
.wm-design-template-38289 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div,
.wm-design-template-38289 .walkme-custom-balloon-mid-div,
.wm-design-template-38289 .walkme-custom-balloon-inner-div,
.wm-design-template-38289 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-38289 .walkme-custom-balloon-mid-div,
.wm-design-template-38289 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-38289 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-38289 .walkme-custom-balloon-inner-div,
.wm-design-template-38289 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-38289 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-38289 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-38289 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-38289 .walkme-custom-balloon-content {
  margin: 15px 5px 5px !important;
  font-size: 12px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-38289 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-38289 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-38289 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-38289 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-38289 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-38289 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-38289.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-38289.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-38289 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-38289 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-38289.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-38289.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-38289.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-38289.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-38289.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-39030.walkme-custom-balloon-outer-div,
.wm-design-template-39030 .walkme-custom-balloon-mid-div,
.wm-design-template-39030 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div,
.wm-design-template-39030 .walkme-custom-balloon-mid-div,
.wm-design-template-39030 .walkme-custom-balloon-inner-div,
.wm-design-template-39030 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-39030 .walkme-custom-balloon-mid-div,
.wm-design-template-39030 .walkme-custom-balloon-inner-div {
  border: 2px solid #ddd !important;
}

.wm-design-template-39030 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 25px 0 rgba(0, 0, 0, 0.20) !important;
}

.wm-design-template-39030 .walkme-custom-balloon-inner-div,
.wm-design-template-39030 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-39030 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-39030 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-39030 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-39030 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-39030 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-39030 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-39030 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-39030 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-39030 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-39030 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-39030.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-39030.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-39030 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-39030 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-39030.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-39030.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-39030.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-39030.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-39030.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-39035.walkme-custom-balloon-outer-div,
.wm-design-template-39035 .walkme-custom-balloon-mid-div,
.wm-design-template-39035 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div,
.wm-design-template-39035 .walkme-custom-balloon-mid-div,
.wm-design-template-39035 .walkme-custom-balloon-inner-div,
.wm-design-template-39035 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-39035 .walkme-custom-balloon-mid-div,
.wm-design-template-39035 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-39035 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important;
}

.wm-design-template-39035 .walkme-custom-balloon-inner-div,
.wm-design-template-39035 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-39035 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-39035 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-39035 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-39035 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-39035 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-39035 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-39035 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-39035 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper {
  padding: 0 3px !important;
  margin: 0 !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-39035 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-39035 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-39035.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-39035.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-39035 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-39035 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-39035.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-39035.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-39035.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-39035.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-39035.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-39362.walkme-custom-balloon-outer-div,
.wm-design-template-39362 .walkme-custom-balloon-mid-div,
.wm-design-template-39362 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div,
.wm-design-template-39362 .walkme-custom-balloon-mid-div,
.wm-design-template-39362 .walkme-custom-balloon-inner-div,
.wm-design-template-39362 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-39362 .walkme-custom-balloon-mid-div,
.wm-design-template-39362 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-39362 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2) !important;
}

.wm-design-template-39362 .walkme-custom-balloon-inner-div,
.wm-design-template-39362 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-39362 .walkme-custom-balloon-inner-div {
  border: 3px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-39362 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-39362 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-39362 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-39362 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-39362 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-39362 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-39362 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-39362 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-39362 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-39362.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-39362.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-39362 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-39362 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-39362.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-39362.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-39362.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-39362.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-39362.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-57896.walkme-custom-balloon-outer-div,
.wm-design-template-57896 .walkme-custom-balloon-mid-div,
.wm-design-template-57896 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 430px !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div,
.wm-design-template-57896 .walkme-custom-balloon-mid-div,
.wm-design-template-57896 .walkme-custom-balloon-inner-div,
.wm-design-template-57896 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-57896 .walkme-custom-balloon-mid-div,
.wm-design-template-57896 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-57896 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2) !important;
}

.wm-design-template-57896 .walkme-custom-balloon-inner-div,
.wm-design-template-57896 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-57896 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-57896 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-57896 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

/* Content */

.wm-design-template-57896 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-57896 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-57896 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-57896 .walkme-custom-balloon-bottom-div {
  background-color: #4178be !important;
}

.wm-design-template-57896 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #4178be !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-57896 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-57896 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #4178be !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #4178be !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-57896.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-57896.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-57896 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-57896 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-57896.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #4178be transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-57896.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-57896.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-57896.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-57896.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-74514.walkme-custom-balloon-outer-div,
.wm-design-template-74514 .walkme-custom-balloon-mid-div,
.wm-design-template-74514 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 320px !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div,
.wm-design-template-74514 .walkme-custom-balloon-mid-div,
.wm-design-template-74514 .walkme-custom-balloon-inner-div,
.wm-design-template-74514 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-74514 .walkme-custom-balloon-mid-div,
.wm-design-template-74514 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-74514 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2) !important;
}

.wm-design-template-74514 .walkme-custom-balloon-inner-div,
.wm-design-template-74514 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-74514 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-74514 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-74514 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-family: helvetica !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #3f88d4 !important;
}

/* Content */

.wm-design-template-74514 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-family: helvetica !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-74514 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-74514 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-74514 .walkme-custom-balloon-bottom-div {
  background-color: #3f88d4 !important;
}

.wm-design-template-74514 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #3f88d4 !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-74514 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-74514 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #3f88d4 !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #3f88d4 !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-74514.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-74514.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-74514 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-74514 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-74514.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #3f88d4 transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-74514.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-74514.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-74514.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-74514.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */ /* Custom Balloons -- START */

.wm-design-template-75263.walkme-custom-balloon-outer-div,
.wm-design-template-75263 .walkme-custom-balloon-mid-div,
.wm-design-template-75263 .walkme-custom-balloon-inner-div {
  min-width: 200px !important;
  max-width: 420px !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div,
.wm-design-template-75263 .walkme-custom-balloon-mid-div,
.wm-design-template-75263 .walkme-custom-balloon-inner-div,
.wm-design-template-75263 .walkme-custom-balloon-top-div {
  border-radius: 0 !important;
}

.wm-design-template-75263 .walkme-custom-balloon-mid-div,
.wm-design-template-75263 .walkme-custom-balloon-inner-div {
  border: 2px solid #dddddd !important;
}

.wm-design-template-75263 .walkme-custom-balloon-mid-div {
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2) !important;
}

.wm-design-template-75263 .walkme-custom-balloon-inner-div,
.wm-design-template-75263 .walkme-custom-balloon-top-div {
  background-color: #ffffff !important;
}

.wm-design-template-75263 .walkme-custom-balloon-inner-div {
  border: 1px solid #f8f8f8 !important;
}

/* X */

.wm-design-template-75263 .walkme-click-and-hover.walkme-custom-balloon-close-button {
  top: 5px !important;
  right: 6px !important;
  font-family: sans-serif !important;
  font-size: 24px !important;
  font-weight: 100 !important;
  color: #cccccc !important;
}

/* Title */

.wm-design-template-75263 .walkme-custom-balloon-title {
  padding: 5px 5px 5px !important;
  margin: 15px 15px 5px !important;
  font-family: helvetica !important;
  font-size: 16px !important;
  font-weight: 100 !important;
  color: #3f88d4 !important;
}

/* Content */

.wm-design-template-75263 .walkme-custom-balloon-content {
  margin: 5px 20px 24px !important;
  font-family: helvetica !important;
  font-size: 14px !important;
  font-weight: 100 !important;
  color: #555555 !important;
  overflow: visible !important;
}

.wm-design-template-75263 .walkme-custom-balloon-content b {
  font-weight: 700 !important;
}

/* Footer */

.wm-design-template-75263 .walkme-custom-balloon-separator {
  background-color: transparent !important;
}

.wm-design-template-75263 .walkme-custom-balloon-bottom-div {
  background-color: #3f88d4 !important;
}

.wm-design-template-75263 .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin: 14px 0 0 20px !important;
  font-size: 9px !important;
  font-weight: 300 !important;
  color: #ffffff !important;
}

/* Buttons */

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper {
  margin: 0 !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button,
.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  height: 22px !important;
  margin: 8px 10px !important;
  padding: 0 10px !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button {
  margin: 10px 12px 10px 0 !important;
  background-color: #ffffff !important;
  border: 2px solid #ffffff !important;
  border-radius: 12px !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button {
  margin: 10px 0 !important;
  border: 2px solid transparent !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #3f88d4 !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button .walkme-custom-balloon-button-text {
  font-size: 11px !important;
  font-weight: 100 !important;
  color: #ffffff !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover {
  background-color: transparent !important;
  border: 2px solid #ffffff !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-normal-button:hover .walkme-custom-balloon-button-text {
  color: #ffffff !important;
}

.wm-design-template-75263 .walkme-custom-balloon-buttons-wrapper .walkme-custom-balloon-button.walkme-custom-balloon-weak-button:hover .walkme-custom-balloon-button-text {
  color: rgba(255, 255, 255, 0.75) !important;
}

/* Remove Side Border */

.wm-design-template-75263 .walkme-custom-side-border {
  display: none !important;
}

/* Alternative Balloon Styles */

/* No Buttons */

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div,
.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-top-div,
.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div {
  background-color: #fff !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-inner-div {
  border: none !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-title,
.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  color: #3f88d4 !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-close-button.walkme-click-and-hover,
.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext,
.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  color: #3f88d4 !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-subtext {
  margin-top: 4px !important;
  margin-bottom: 8px !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div {
  margin: 5px 14px 10px 0 !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-powered-by-div .walkme-custom-powered-by {
  font-family: inherit !important;
  font-size: 9px !important;
  font-weight: 300 !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons .walkme-custom-balloon-bottom-div .walkme-custom-balloon-top-div-bottom {
  padding-bottom: 4px !important;
}

/* No Content */

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-content .walkme-custom-balloon-title {
  font-size: 18px !important;
  font-weight: 500 !important;
}

/* No Buttons, No Content */

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-buttons.walkme-custom-no-content .walkme-custom-balloon-title {
  padding: 2px !important;
  margin: 22px 28px 8px 18px !important;
}

/* No Title */

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-title {
  padding-top: 16px !important;
}

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-title .walkme-custom-balloon-content {
  margin-right: 30px !important;
}

/* No Title, No Buttons */

.wm-design-template-75263.walkme-custom-balloon-outer-div.walkme-custom-no-title.walkme-custom-no-buttons .walkme-custom-balloon-content {
  margin-bottom: 16px !important;
}

/* Popup Steps */

.wm-design-template-75263.walkme-custom-popup-step.walkme-custom-balloon-outer-div,
.wm-design-template-75263 .walkme-custom-popup-step .walkme-custom-balloon-mid-div,
.wm-design-template-75263 .walkme-custom-popup-step .walkme-custom-balloon-inner-div {
  min-width: 260px !important;
  max-width: 600px !important;
}

/* Arrows */

/* White */

/* Left Inner Arrow Color */

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #ffffff transparent transparent !important;
}

/* Left Outer Arrow Color */

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-outer {
  border-color: transparent #dddddd transparent transparent !important;
}

/* Right Inner Arrow Color */

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #ffffff !important;
}

/* Right Outer Arrow Color */

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-outer {
  border-color: transparent transparent transparent #dddddd !important;
}

/* Top Inner Arrow Color */

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  margin-top: 1px !important;
  border-color: transparent transparent #ffffff !important;
}

/* Top Outer Arrow Color */

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-outer {
  margin-top: 1px !important;
  border-color: transparent transparent #dddddd !important;
}

/* Bottom Arrow Color */

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-outer {
  border-color: #dddddd transparent transparent !important;
}

.wm-design-template-75263.walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  margin-top: -2px !important;
  border-color: #3f88d4 transparent transparent !important;
}

/* Blue */

/* Left Arrow Color */

.wm-design-template-75263.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-right.walkme-custom-balloon-arrow-inner {
  border-color: transparent #fff transparent transparent !important;
}

/* Right Arrow Color */

.wm-design-template-75263.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-left.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent transparent #fff !important;
}

/* Top Arrow Color */

.wm-design-template-75263.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-bottom.walkme-custom-balloon-arrow-inner {
  border-color: transparent transparent #fff !important;
}

/* Bottom Arrow Color */

.wm-design-template-75263.walkme-custom-no-buttons ~ .walkme-custom-balloon-arrow.walkme-custom-balloon-arrow-top.walkme-custom-balloon-arrow-inner {
  border-color: #fff transparent transparent !important;
}

/* Theme 1 Custom Balloons -- END */</style><style type="text/css" class="walkme-to-remove" id="wm-font-opensans">@font-face {
font-family: 'walkme-opensans';
src: url(data:application/x-font-woff;charset=utf-8;base64,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) format('woff');
font-weight: normal;
font-style: normal;
}@font-face {
font-family: 'walkme-opensans';
src: url(data:application/x-font-woff;charset=utf-8;base64,d09GRgABAAAAAGO8ABMAAAAAtcAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABGRlRNAAABqAAAABwAAAAcZN2QOEdERUYAAAHEAAAAHgAAACABFwAER1BPUwAAAeQAAASiAAAJmCwaFlhHU1VCAAAGiAAAAIEAAACooF6Ikk9TLzIAAAcMAAAAYAAAAGCiSZvkY21hcAAAB2wAAAGIAAAB4uXMQipjdnQgAAAI9AAAADAAAAAwDu4TqmZwZ20AAAkkAAABsQAAAmVTtC+nZ2FzcAAACtgAAAAIAAAACAAAABBnbHlmAAAK4AAAUC4AAJeA5x/k1WhlYWQAAFsQAAAANAAAADYFZg+uaGhlYQAAW0QAAAAeAAAAJBAGBpBobXR4AABbZAAAAisAAAOmGPdMNGxvY2EAAF2QAAABzAAAAdYSHu2YbWF4cAAAX1wAAAAgAAAAIAIHAaFuYW1lAABffAAAAdEAAAQwZ++MYnBvc3QAAGFQAAAB7QAAAuUaeDKocHJlcAAAY0AAAAB0AAAAiOUtDl93ZWJmAABjtAAAAAYAAAAGJUlTOAAAAAEAAAAAzD2izwAAAADJQhegAAAAAM9d1ch42mNgZGBg4ANiCQYQYGJgBMKXQMwC5jEAAA5NARwAAHjarZZLbFRVGMf/M51hxoKWqtH4CBoyNrUGjQ1J27GwatpaDZZpi4MOig/iAkJCY0hMExaFgbgwIQYrOTxqCkyh0FmQUpryMkxXLNzhaW3jyuVJV8QFIY6/c9sp4EjVxHz55dw597vf43/OPXMVklSpbn2qSEvru916/rOvenep5oveHTtVv+uTL3droyL4qFiU9/0316GdO3p3K+6vAiIKB2NcoXhv4Lldt3QrdDg0ELoDd8PpcA6mw7+GcxWrw+mKfTAW+SlyL3IvnIvOr/gtdDj2TKw2loLPudoL/ndt7MdYKp6MJ2N740ni3b1vRMvBgqUfNOIGFp2v2BfEKVntwxbfDklPeDo6T6V3gqoHAt5UorhHDXpVTZCEZj2tlmJercWs2qAdOooFdcJmSPG7i7GbsYdxC6Shnzj74QBk4SAcgkHiDeF7ipin4QzkYBjOwjnujcB5uACjMAaXYBwuwwRMwhXyXIVrcB0KzE0RP6R1mtCzqika1UE9rIcG8jcWrZrwS0IzfM38EfgOBuB7OAoGjuF7HE7ASRjE/ybzU4whouXJESVmJdRwvw7WhSrJZ8lng3xNeCVhIZcllyWXJZcllyWXJVcptg1iT/PcLDylKp6shkQQrUA0RzSnt/jdzLgB+rneDwcgCwfhUBDREc1phufnYNVSjaX6lqvH1+J17OO5KmqqhrXsB1/JozLO4DMHL6BKBlUyZRkboJGamhiTQQ+FZas4hu9xOAEnYRD/BZUKqJRBpYweV9Ufv6saEqyNV2ZBFUONhhoNNRpqNNRoNIPfHLQGXa0O9C11tqe8XuZbyNHKvTZohw7oJNJmSHHdxdjN2MO4hVhpxq08+wF8CBnYRp5HvRHL9T/E/VPkPw1nIAfDcBbOcW8EzsMFGIUxuATjcBkmYBKuUNNVuAbX4cbiChe4d5vafobS6q1EGYsqFkW8jo6qHVU7qnZU7aja7yqLNyuIt8HbLGqYR0OHhg4NHRo69LPoZ9HPop9FP4d+Dv0c+ln0c+hn0c+hn0M/nzVP1jxZ82TNkzVP1jxaObRyaOXQyqGVQyuHVg6tLFpZtLJoZdHKopVFK4tWFq0sWlm0smhl0cqilUUri1YWrSxaWbRyaOXQyqGVQyeHTn53Gzo22vCX9yFbtmta8GqFNmiHDubun5dm8bw0i+dlPjgvtwXvVZaus3SdpessXWfpOvsPO8TQtaFrQ9eGrg1dG7o2dG3o2tC1oWtD14auDV0bujZ0beja0LUpO0sXdodZ2hWrytZ1ubXwmkU4BRyngONNdbypXC/NlL8fLtiTJU+eRdtKmIZZ8DN9zPQx08dMn558aFf5ndQd6PHfVtuv7Bpip4id+tu9+mDk/2N/+YzT5JqFx5Yyl076tUHPqeDU9h7+5PZKWnTz+lj0sXx5+JqjwVfOSs7pKlWrQgmeXaHX9QarVa/1eoLzayN3WjjtnlO73taLegdbo03YS+pUl15WD5bQ+9gr2irObH2E1alf3+g1fYs16IiOqlFGP7D7hzRMxBGNqkMXsU0a07je4x93gnonsS7d0E2+vqawtG7rF+LOYR//CRxXWnQAAHjaY2BkYGDgYohiyGBgcXHzCWGQSq4symFQSS9KzWbQy0ksyWOwYGABqmH4/x9IYGMJMDD5+vsoMAgE+fsCSbAoyFTGnMz0RAYOEAuMWcB6GIEijAx6YJoFaLMQgxSDAsNLBmYGTwZ/hhdg2ofhOQMTkPcMSPoAVTIyeAIAoLkaBQAAAAADBIICvAAFAAQFmgUzAAABHwWaBTMAAAPRAGYB/AgCAgsIBgMFBAICBOAAAu9AACBbAAAAKAAAAAAxQVNDACAADfsEBmb+ZgAACI0CgCAAAZ8AAAAABF4FtgAAACAAA3jaY2BgYGaAYBkGRgYQuAPkMYL5LAwHgLQOgwKQxQNk8TLUMfxnDGasYDrGdEeBS0FEQUpBTkFJQU1BX8FKIV5hjaKS6p/fLP//g83hBepbwBgEVc2gIKAgoSADVW0JV80IVM34/+v/x/8P/S/47/P3/99XD44/OPRg/4N9D3Y/2PFgw4PlD5ofmN8/dOsl61OoC4kGjGwMcC2MTECCCV0B0OssrGzsHJxc3Dy8fPwCgkLCIqJi4hKSUtIysnLyCopKyiqqauoamlraOrp6+gaGRsYmpmbmFpZW1ja2dvYOjk7OLq5u7h6eXt4+vn7+AYFBwSGhYeERkVHRMbFx8QmJDG3tnd2TZ8xbvGjJsqXLV65etWbt+nUbNm7eumXbju17du/dx1CUkpp5t2JhQfaTsiyGjlkMxQwM6eVg1+XUMKzY1ZicB2Ln1t5Lamqdfujw1Wu3bl+/sZPh4BGGxw8ePnvOUHnzDkNLT3NvV/+EiX1TpzFMmTN3NsPRY4VATVVADAAeuoq1AAAEXgW2AQIA4gD2AP4BMQExATYA1AD0APwBLAEmAQ0AyQERARwBFwEIAIcARAUReNpdUbtOW0EQ3Q0PA4HE2CA52hSzmZDGe6EFCcTVjWJkO4XlCGk3cpGLcQEfQIFEDdqvGaChpEibBiEXSHxCPiESM2uIojQ7O7NzzpkzS8qRqnfpa89T5ySQwt0GzTb9Tki1swD3pOvrjYy0gwdabGb0ynX7/gsGm9GUO2oA5T1vKQ8ZTTuBWrSn/tH8Cob7/B/zOxi0NNP01DoJ6SEE5ptxS4PvGc26yw/6gtXhYjAwpJim4i4/plL+tzTnasuwtZHRvIMzEfnJNEBTa20Emv7UIdXzcRRLkMumsTaYmLL+JBPBhcl0VVO1zPjawV2ys+hggyrNgQfYw1Z5DB4ODyYU0rckyiwNEfZiq8QIEZMcCjnl3Mn+pED5SBLGvElKO+OGtQbGkdfAoDZPs/88m01tbx3C+FkcwXe/GUs6+MiG2hgRYjtiKYAJREJGVfmGGs+9LAbkUvvPQJSA5fGPf50ItO7YRDyXtXUOMVYIen7b3PLLirtWuc6LQndvqmqo0inN+17OvscDnh4Lw0FjwZvP+/5Kgfo8LK40aA4EQ3o3ev+iteqIq7wXPrIn07+xWgAAAAABAAH//wAPeNq1vQtgE1X2Pz53ZjJJmufk2fSZNG1D6SM0Ia0BeYrKolRAREBERFBEVBBZBGQREfGN+ETWdVlEZF3WnUkjKl98oYiPVdZ1xfWLrvpV1CqK6xOhHX7n3DuTpi90v9//X2w6maQz95577jmf8xyO50ZxHD/LdBYncGauQSVc/MSMWQx8mVAl07snZgQeDjlVwNMmPJ0xS8H2EzMEzyfliFwVkSOj+LBWSdZrc0xnHfnTKPE1Di7JLTp2gLxp2s7ZOBd3Dpex81ytYo1nBYHzirVEcccVbp9iT2QlK1cm1ioO46jVKXGW2qzLzBXCaVc866RHqkxqVadL9qhWIZ3mVLsgexRnekBj88CmZCLg90nRimpvRIgumjrpzHOmTZg4TSRTk9+tnThp8oQzzpliuqo9ztFxrRa2CCNhXDjf07kMh+MSkzguC9xPStAz+luiWOKKsC/LmzkZPuTdqpnUZiX6TrXCgMw8DIiIMKABjXhzAj+rSbBmN1mOr6btHV/z7o6v8b71HCdqpixXzJWTaVymiONqM/5AKJlMKly81RcsLK4MJuFaba28XFJaGUwoYrxVcJeV42kTnJasBQ48bY5nLDY7/B1RwnGlaF82xEYXcqsBGJ2fvoNLF9S2Dvd7rbWtFn8ACGpm3zLHsxb2DbMFv2EWrbWK363a4E/tbGIRUqs0Fe0YuuPb0zh/bcGOofu//Q4PlCJ3K19k9ta2CvRVwle4bas1ZIGDgLu1IGDz4tVaHX47fMFNX2X66sNX/E6Qfgf+qpD+FVyz2LhOiXGdUvxOa5nxzXI8Lwx38wLSwC0jsUpKy8obuv2nDC/CdUhFmqOpiDcpJPHHHzFH/LAs3ij8VCWbo/XEH28nkbH7x77Y8nbL11pbnPDa22Pfbdl1+ttjCPdC/AVyz+ufvUHu1S7Gnzc+e12bS+7Bn9c/A66ZfOxGcZTk4cJcNVfH3cEpgbjiTaolYpsSS2QCJUjUgB+IaosrVUnYRW2KkMhINjwvAbGJUk9ZvzChRsxtSsSt+kltRiipTCQSWZ+Zs8HSmGwxeKf43GoNMJnb3KY24O8a5H4Lcn9JALi/MK3Y5Mc4qztUWVcZTCuSR7HAhvAObGpOJf2BoLk6JpfxsDPM/mgKj0lQjjWQKl8gmJJIU2pgdWzyR6/eeODJ6fdvfv6hsZ/svfG7J87+fsZJLz5E6oeMWkkKbhg1Sgyt+y/ffXcXTPh8uFN757TLrpv8++e8r71sGk8stSPhIkUtj6+pS5d94W3fFzyv/6By3GMmbtixr6QfTK9yBZyPK+SiwPsKl/Ejx0fgRY2JbZkA7LIMDy+qR2zLWpwR3lGrWuCwuJYeFottRGlASmVtTBTY3KobmNTE3pncagjeVbJ3lZRS2TImKuJILJvsyVh4fzqdVkwy0EqtDAHNAmmlRs4UR4JpJKPFL3taQ2WVNUA+1VMMb0w2NwdvgIruiCFVmn2BZCI1MFoheUnSSnr7YBiZ8sfHMtseyrbXJ2bMSNSPE2q/bn+LvNDttMiTl79895NPv/zXiuXtR5YdXWnafmQM2YEnD3z65Xv0JAc8NuHYQYkD+pUCjzVyy7lMIdKuGGkXEdoyViRbHAmUQAKpZdY2pcytxML7ZFUCnpLiasyMp9Q6oIQd2CcJv8skmL+QVutisidrLY5UupBp7HLGHYpSakQK4QuhtBIHppLsAUoVxk4NJGVIWTNpao5IvJlEYkCCyiokQTNxEq8vOBS+VQ3EmLDkztNGtT2/4/2bNpCSUweSoZW/GUfqtTULn/n3d9r/kBErZ/9mtpYddNKk8yZNG50+aSy5+cbnJk763bnrd/x53eLdU7QvFj2xRjt2gbZ/weoP3p104RAypm4Gv3zy3AHnDk0NGc5xBGU4uZ/K8Aquq7wW8+S1aiK1ulxebUhj5E/CTdB28kvg7x0gjUHFcfCHTspqICSr4A9d7A/dnuakBBvIE4xW8xN+e8eRW2+/84bDd27gG4mVvP7oc1riu++15icfIS/CNYfANWcZ1+SMa9r2ZcUu10wGPLKbN0ebPKmB/JAjd2747R2H19x1u2n7X7RG7Sf4N2jrE+TlH74jr8M1h/GTxFLJxzlBhypCnIA6xD2A12k2CRGhKmjymm0k5h0WI5fWEKmGLIpo297/6P4bD74neo7MIfO12+e0F2pvLyFp7eXFpAauOZn7SEyLu0EvnwW7Mq6YqdJRTKD4CMoorsBamyEcHhIBxZU9rhTsU/hE1so0iJjIWAvwY6sZvllgxcMCzlqrOtjIUhEZgIE/IkflyWTVfrJKW76fn7WfXK8t3a+tICtxXtph8ir3FSdxVTiGLC9wVlw9c1zh96kiMKwFGFYE5apIVLV6miNBSRg2opIUugZeDX9dcDD4ivYFruUQspWfxG+ivADXUompDX+QFVQOZIJgRc4weCEV8Q/hQ2TrkSP4txSjkDTQooHrBCc5jGKnPMFgif5Ln2Q+6MgBDgNrMB5zwkYeRXk0APyA+5dQpoBhsbEkSYQ4+Qjxd7yPYgAxwphjB8XRptdgPEHAZRkrbniXqY2yqOrHSRXSDQ9bWrG7VQ8QSbK2oSBUPfYcNPIjSpK4NJVinkiCA4aLVHDEDVu1SXbjFh1zhIgdRDiqHe3QjpHkuZfNm3H+JZdO52G1yOXaNdpt2krtdnI1Wah923aQFBDHF5TWS2BOLTCnAli3jNg5J1B14j5VgKHYYSiCCOtG6LoRhIjDiOQiS8jbmvaqYBpbtlUcRhYfGSO03Lx+bOEaSqsWwEbjqLw7k8vIOGsniDkRZ10kwKzL4kpwn2oxt2UsQWQ3ixs4L0jxS1AGzisHgqpOGW7rSStFMnyrFOW+6FE4JMJQPpkoI36fk7gI8GUkRYbyTFSZW+bdtnXOjX+/8tS7d+7kl7fz5PIHZ9WdP/6sjWeLR6adXjMre+Vsdcc21am1v00WPrzyssGTJ7WMZmOGtRoJY67m5nKZKhyzCCtVSDWaqS1rt1UVghqzm9pa/VWFFiBSDPbaPrUCZLUbBXUxzMZdjFNw22AK/XAKNhHhZEU6rfqr4MhdBpPwyEpxWilE1QV8B0ocFhEGX0tS9AAnEWuKJESq53GWYqSi5ay/zrrvjq1PXL7gkd/9bfTd56x9ifg/IuYt96jbtde1j78aTMy1TXMWXjTpyynztgwY/NbtT2y+8dlKKfCndW9+gXwYhfVYQNfZy81ifEh1dZazWUE5A15WOcA1UoIovrhiRRyPq4NAx0LlgUWCBbLSBbKiaACIo1qsoJF5t0x1jY2jPKLwsuLGJUoRkBr+KDUoQNc0RyVzlF9JShVF+7u2kcwoECxVA0n8bUFpv/hr7Q0S//rw0IPeCS1sr82CtUjBeIu5iQxZq6LUlnHgWriFtqzPUuSAtfDhBiqJK9I+NQisWgpjCoJOBKsCRyQWycguikXOEBvCA8XnUe1y2qB6ODUwgrT2AgMJzWz7c5GKWWf8fTop1vanrum3rFkIdfxQHB0y9R9HYdSffjeY2PqnPnvPbx/Jt2lHtA/Nzq/2fq8dZnbIaBjzONMewEeV3OUMHaklxl63AAe5KvyCg+5/olTRbR8CEgPKL8ftDjKyGn6HgI4Zm92B4y2XM4KLAh6PRzVRnFhRAvPjPHDKJSt2mBwKVBQLXCQR9MMOcBJzUp8LiDKeqvMmtjdGk8vJZctPnXL271+eZXVc8N8v/Es7/Pmmf68iyeUzLph7wazpq/lLSYZsdf3om7Hzz4/88M7n2qF7SHja4s2rl12ybCmuSzPd11mQ82EuY4IZUgGNO9ocRxHPgb1JQQkMCVQGCMRmMdTxNmjSKlEh4q6jTlFBPIS0GmN6GaRiBUjqK3VqAURkUKgOoVCckqgQ4Q9urygcFLrVMkYrxeNW7Hi6Bo5r4hQTDYCPogwTASZs9RdHrBQQeRQXUK4O0CDCIE+kugsMqkyyrUZ3mgGAKJaWvACsDQw0evWdyy8j4ht/J+Tqmzav1T755GvtK1J21ZyFVyxY8VZi7OyZLbNazjifLFy+a8wZ2Ut+t+uZTfP/cvLkZ67I7v/ra5NmXDD+pEUjZ/LNJ56XaJgx7ORx4xnPjKR02MOFQP4CzxR00Q9R4JlgaQHyTBB5ppoSpAgmXORWw2iswqRj8LsIeabA7kJOCcuqAMyumD0Zj9dHt2YQ1IfiSCulsuJNK1GPamaqZCAHfOLxA+tUxFIw6aGkOeokwDX5TDOS2D7Z9O212l3a2mtPmjjtty/NtdgHrb/imXdJ7cxZ069ffv6MecKrXxB5vfb+S9o4bZLzsP+c5/80/fTv/zX36mXjFm++rtN3IC6kejDNZVwERI+fKuV8F0JhNxeCxzhChdhNScu9KWz8fe74TsUt3IwH46dMxjEgRsExSJyHGwy0xjG49Tt7UZRnHey2YkJxuFUe6MzHVR/Q1wG4JSMVuNPpTuxiI3kDMHDMFmMAOUAjvpEbAUex2qtiGvaNxHEgIf1W4p8sfNgxkd/Gr1xLvv5ae1779BCOdTLZBJiOoz6NIoaCANIh0sCdYYmjr0JHPwR+4CLt5cKHZNN+0Pf79/e4V3PKSuB2k/ltHROFD189REJkyNeaey1dG+nYAWEj6D3kwV9zzIQDflOi8WwpW6JQnDJf0b5smHl0HOEiC/UuAA5Wwm5KJJPOjHYHWCO8HCyN4uYDdrSCtFJNPhmNWU4NlQItTT470FLlg7Ku0A1bxElKCVUX+rYze/OoLL1/5PVvZ90yI6n9OOHSi0+aMemeZ1caK29qWf7iQ5dtnHXqmBNPHDPjtnGnTR80YtTM9pIcguO5C49dKO0BmTOQG8bdzVEwkq0SOR9MIRHP1rEjT1yxJ7PN7E1ZQhkSzxbSN0QZTsFjDcPMNdTKz6bYu5QbfSy6H0YdAVSIpGTPcKtd9BRW1cUTg4EUnOqpg+nG00qzDAJJGeLJWjh/BG0ypRAhAe5ITyUofg8CG5hvLIqzTtFtGhR8dEs2wAcij3s20dTslyJhjuAHwwju1QvfIeuI6V0ydee0rZePuSLknvew+ldi/+ekvScFTx9++vXf3v+Ktu/3JEYK52rL9mlHteu0s/nzt02dXuBIDl9+Mz/1R3LngayWfef2QzecOmjlW0++SfhIUAve/F/3/uHHa7doe17TDmrvxOufPYfcTpa/uWLte7b7mRxDJ8Fq007gVgd3GkPHipCkYDIrWTgCIkxCLUGNMtUMkMnsVkWElqC3XWgamMFWJ7zFSilFLEApO1CkETRIBOwib4QHecyLZBkvaZm5HV/MfYIsv7PKEjHtPDKKTNM28zPIO1dXXoM75gnQUd8BdnCBrAlzF4G04RhsYKwdltqyhUEXuiQKUapG6JDcMKTChOJmvGyHdyWoXUwwvApkbmBfwDtUmrrp2GDN6Akl7FFMMFLAxeE8yBYV6HJFoikD3T1B9pBmElp24c3LtPcPf/nKNUu19mezv1mwbPWDpu3qc6u2ygXlj9z60geEmzl7+w8tUyf+CvbwYtAPb8DeDHAncxkf1Q4Gji4Q2lrNPhGBaJBOwQFjLUQV7PIx3GyWM5wD0ZkqFsg6TgAOSyaCZmQj4KJIolmWomFu8RbS/MZbb8+asGXcX54ll2/Yn/2X9pz2KP/Ox+Tsxy9qjw3SfvpCC47V2k8jq+h6A41Ni4DGFqDyCVzGgiOzGhR2SW26O1i1AiGtbmpEICllOjyAjTmSgSnDRYRkWHZHok+QV8mF5BZttnb1nNXkWW3GQ6bt2vXan7V7tWsIRz4kb1O5huvLUz/0qYzT6J2R1RAkZk2M3Uw4CHtuEGjjUhPYCtgcbF9m7OrGH7Nu6Y/8hDCm4yA5pMm8D+6uPaNpa45xxn0FDe5r5Ybn2X/0nhYTvacF71nA7mnOvyeY3foNbd1u+IRwSscXBGQx3mxNR8fT7F6w7qYYrHsRWGjUV0TtJ4YkAf96vIWICjy4pYrp/WwwR+ZPU/1mavy7/dQU8cBNSwz3mWApRIzgl9EKV53oHvKnVa8HMaUtjVAZPlAEtjwMU5qrkVOoU0hG+oBkAn4hd5OLPnzjoo1/fvmb53ecP0v7gh9160/Xao9pD/LvkZnklqmHx2nffPzVUR9pJHxHQUMVWW3Q0HQhXbthupQwMymhmJJZoYBSURByK4ez4hM4McCWQE+UHJ1rlvv3BGniTyIp7dWOp0zbO57nhxwZwy/uuJHdj3xFbfZIN5sdL4/CB39MuSvClZjpzpFjc7QJ9G8dXD2XkXCMtrjK61LMBNYrE12cytsYvpJkqszMFDzBxdx8tCK2ftzICyeTps8PXNxyj2/FGtPUI1uPcdp3gRxPmcbBPezcAJ0elhw9iOJgvgFKBNVpoGtVKEiz3SM3k4gVJKQZx72U3EImazzPaxu1lauADhdsI//uWNL+Bj9nescP+r4ZBvcycXX6vhH0fUMUyaBHRqAcK5iAbcx5hEYSjzdtPzrmmDFu6R9wLR93k34tsyvJRq7yJoxk+OkVfea2rGzmykFH+mhIgrkz3czhEcf4BkYmdr37pY8GJFwNTsX9rCrYfjIp/LMCpwruhgbSygsutx4PUG0oik3ONHo6geq6xWFnFCFJgqMd2OSNAl2iHj8MfAuZKoHl87D2L8Fu1dZoH2sbrV6YyiZxOvBJtvEa4ju6RlymbVrUMdlYk5ep/jhXXxOrvibmpCHXXDB8l1uV0AqGQ4sbnYI4S4BoGNdy4TrZAOQAU6h8AXNdCGljAW1pY7g8Moox0jX8MrOLBLVfd1xHR/gkKf01nz0yRpyg7V/eMQ7kLsqFT6k/yd/pTzIkgxd5M5DjGbubDgX9SUH4LaM/SaAqzIv+JE5K65ucCWFEEgEqiCukxeRiMh7+zdbWawr8W09O3vEkWaitfXIn/z65lKzUrgaD4G5tKbmeXPL9YfIl+eonQy+Ij+h+hpH6jqM6wQtS0mrjUOtaUUr66DALUGollAI3xQCoIfzI5V6b3EWpipFoiHTq0TdJAfFr72hfr75w7W2LV9xq2n7go4NHOg4L0oJ5l86h41isbaZ0cgGqnc5lHBwjT8bhRe52gA5gJAsiyYpyCMBNUR0lWTFKUlD1rYLNTs1I2N0FSDuAt4o1rQTlbhREDzrKxl6o+LhKZmgLte+CfZJS0x4cry0mo3uhp2k00NMJWOYcnRsLkjpGB5I6XJSkDinnSXTCNFwJxelWvTpJ0ZnodTLQYgLQYkMWcDkoHodpdEUvXBAmkU/sR0h/UnbbtWTMLG2r9uBDs+68Ze09003b33lv5ctpzXs739ixV6ifefGcyVQuTAe8EgS9FeMWcJlq6rcBqntwuCHAK4FqD+KVfnHFtU8tgY1TQgOw1Lb3J2hsrMTFRmqWHxNtnlAYjXW0WQMR6tOpZj6dgNxKXCVRGuUJUS2W50prILEGnhr2AYZ0JL+vjAR1A3/6Xa+ddeGlA85de/3144j5syv2Lpi16L4xk6dXn/nb19ZrH2mfjyLhkU0tY2tPGjpq2JUbLtr1r6bGfw+onjCyZkh6zMzda1/8GOZZA3yO8QYzNwh0Qw4LcAK6zGiQWdqHxM+YJGQ4EwCAjGSiEUP0nunWm66+asRxwB2viFnCa9rR08Us0w2Pwl4HSoO12sxl3EhLSZfXwALUZGUiWxHcNHQNe56CVysG0t1p/QY+Qxv5JBG481GSuuF3628kqXXaV/+lfaK9xFuER9tX/vGB3z8iLG9v2fTdtSQC90Y8n6R6egiXseH8aFjdkjQ0M4H7EqqWEV6hToZjkCoFlLs4YwODaAPKNzUjjCdp4g02SrbhxE/Smkt71LS9fcPY1/pN+0S4kKpcdl/zTrhvKQlwmVLkdm+S3lq1yKhVytjNzfTmsu42K9fD2+6vz0Ml4lRMbsX8rFps/0kJPbvj2cd+uJ6dLnQrgWdVm+MnxfHsjqFPfDscTtvgy62Syeyt3fHsoe9L6Rmbu9Vuc3hr4Q9ag4UB+GjoH775B/2o2N1aVBzy4mKawzeFb4pKsLHSGTiHv+Cv8k7Cn8Ivbrjd7CgsNkk2eyAYKsqPbpO+PwJFR2B+QFBvKSUoWM2KSAnqRZ9UszfiBcLSAzCQqvmYk5iFCGn8r8aAVOt9i1S95exvK6jz7CCN2i3a71+0pURpgGO3thGI/j/vbUofGikk219r/p/xLW2jhbIjYwSuhpC6pkPJDl5fB9Mkuv7VnbiEN3AJKG4HBT6ozESKRhqtFIrQ/8kBbRCZRAaTFGnRUuQr7QFtm7aN/4Z/oeMb3tlR21HO13S8bay3qFE7AvCPOcdnAtzESr3rKIoLKGwAAvBICXaAlEDoA4xNxpE4wMwWrVj7K8CeLfzU9lUde/g4Xr9R93tbuQYDpxj2E4WZBXGKyFUz816DtNINpST6r9GBKTfyT3VMEos6RvF7Xxa+JNxL7R6GgdZqO/mFhgygElkU29APqvtoaPjRinEwjLWZKD4wTgiJThngj8pJ/1ry8QcfaDulI28e2fYm2wt2sDdGGvEmwaBNXrwJl95O/HxE+4KBVsIlYUxBOqaTOH2abEycPibzPrg3etVwFJI7SxhsIXF8ow/ObLiXgkk5mgIyJN9/n3yslSwwTXzzJ4mOzcJbxCGmpzmJkzkdQuoOYBojIlErsZDtt5NDh7Sntc9AxmxvH8Ov6liOuLpd2ym0HBsN8yrFGGiWEzk7UIb9ypseZnmIwoT2R5+4Be9JThffEW6VIsAr/TgArBhjpL47K6W0yKKCBZQvJbqaAxpJKhII+qMN8Mdk0rBtrwz7TrL7Z79UXLcbSDkJdNVgcRFXyFWgBxqjVJmA4Ya2E+QVsS0rhAN2R21W0J1AUea3t1K/fRkzSgAMqpW66161ItgrkzNmewBNLZdH8QLXCgHDJEfsYPcAlKAe6GEEAz7mGHVyydGY4X8FmT2EmJ1k0k9Hdz16/WOzn/viw6/fGmwZ++CqPzxJ0nfNXfHr1deSlswfrVLjI+Nfn/3CSx3B9eef9sTWlUtnTxPFyRQ7bIT5ZSUf6I9y7hIdizlxfgFTW8ZC9OiEhea3WAgGhsN0cl4zNbq8NB8DTTD0bale9DGbJPSBKiFAEU4USwGOqhqlRFZsNBahYwnZR4MQHmYCRc3ePIeyeSNptNsv+fuLH3y6Z/d8f3L0JVdOv3z++Qvm8JJPu+fk9Vu0V7VvtS+0v61dxiez9//5oYceunkj8ty0YweF98SFgHyH6L4QB3rKcSJWUw752hjc5VQHekHktGKVMxwbdle7FoGB7IZhNVObdhopIdZdG6aOvnroV19Nvue0Mfcu7PiBryGlpP70g6VV2qPaE/GEdjReSWkLYxEX6LQdz2XsSFt0M+VoCAziZeqxAMgJAJeGemCXJSk1LV7ZkxWc7kApwhugp8kBAyxA5MPyFJKJYLIa1XaUegF5QinYzEg47cDLb15eECSJzwc75ry1+0OSumLuoktNly+/cAFfT2D/bV4+k1z408F1D5EEsT300A0PRoCQxrhnAg19XDF3MZfxIBVtok7FELC73+IRgN39OruX0NmApQvwDKwctNfQgqOhtoAFPQo2T5pZOSzoZvPIGG5BT4Izrfh1966bSyZAp0coQGv2Ux8CiVBoNo2EDn9JLB1x0+3Xzs7OHLd9lfaN9jdyItnGX3H++ZfxMQJoVPvmq7uuvaN/w8F+MYCj6xcsW8YwmLBIKgd+mMr4gYYVMPtI4RIZnjCDXdJZw4cZD5S3nYmM14dM75UBlfmoReBDVEbZxuZi+B7gPs29SjXTTBnqB5FgCtRJVLN1594HlrVMaxkxiFi0w9peYcmdEyY8o8Q/KB174ikH2tcIS1CGC5yk+cRLgd41XBM3nHuHywxEioeBbz0YfhhGZZ7iS7CIyDDmdo7Fs/X0KFs0aKALVqNIX40RccW+T23GTKCEwoX3ydn+THw3uzGHEfOmwJBvdqtDMBIKXwu6lUr82gDmqR8Qx/QqzF0ZCV9oNgxCdQjIy6yrJByrR24Ey8ZPwfbAevhCJUeDShhTK/KoEgawB8mqtQR+D/Nk/EF05IOmMHKKcplFwYjfTP32cQLwezBBJ74YyYst1ZIKyZALQNrfLI2fMuaUyRd99V58pYdc/5cBR99vro9vffqJ57Qntdc//5FYlly6ecdlCx+YuODyM8+aNG7L1u2zbyj1nZMcflZN9dYrHn9JFn9bf9q52ZcFU2XdyAfue+GfD/5p2OipLcMGnCGMPWfu3HNeQRkCgkTcCvvWj1EoimscSUNy+Jnc87vR1aI6zMxs9nMUEShOWTVbafyHyjcXYVFWdDaggSGDVDOb3Rf+a/dftb3Za64AWfZ81Y1TN//jxY4Yf+s3jz7f8Q3uvzthEO/D/S2g3Zv1ODwGojCLE/RZFFfZQQPwXIL6SETq+AFsD0th5ln8aWAyQQMiCO/v3LLlzDO3OEijacXdd596xtGgOP3oJuqTP7Zc89F7OQA/nApWir4heBNs5jhGvujdgujLgj1B/RieBHqQVYsJcxX8yAN9+bbw/jFijGTVKb8aeyppfP2pRRNJgI7oI++kieIjR2syz4XME3BkDNMg/X+g+U/NndasmaDgdDHzlS4C9WM6Kbo04SjM9NBuuL3MyZzjC8juFleDaTFZG0Xe1jZqT6+SfB1jtEfIRK24Yw3ZfbG2md2XvAH3FbgSdt+cCxCWGX86XYBwRcn308HceM0jYf9Gufk6fpSL0M8FI6bDBvZRy4GgATD6KukF0ZSNuqn7QI/UYlKPDLeoQkOXozheKZYVM91QBVaWEUIdWeXobhCtBTQ+nZSTweRQgooAXxmrVVNeyx1sbKuR6x+57OiU4vq/XPb089rr48+ef7m2d/zZi+aK09eOPXtzy6Tn30YGXLJk46Mde/H3tt3Iibm9QHXB6fpa2PJmprpRcOa8eOi+Qy++DSaCSsCnT8SOE4Ghu1GWiOn8cQe6DTTZesXzr2h7J02/5goY3Pgz39zDRvanF9neQN20Hsbj4ELo26KxcNnQ8DQAXpTzcDhZnMasO2p8Tt0tyqlBWc4FuFHR6wHurpkQ08AqFf7ww3XaB9ox+EWaL1229JJ5y5bO4xuJhwy4RTuiaIe0v95KLMqWR/748JYtDyGeAlmehfF5QedfpPuUYFiMZJKOpxQuno+jfDkcZc3HUaLLwFGSgw7aAYPGc4ikQPkQg5heJCZFUj4ed1w04A9RKCDrWOpwrROh1MW7Vu2e73ZfcuVrs+cBktJ80ph1W7TXta9btcM3rb0loA0Wy7P3kwkMSwGtYS4L6NqHUXsiGjQ0phER86PSZ4yMwQyrG9ceBQjGw2x+xC8uT2E5aoxigLuSkyXggrxo5SR6XgcygWCymTplWXZBFygz7cCeuQ+caCkmvPa6w9G4ae6LH5DmSxZcOc90+bK3Act4yMBxE9f+tJ28NeSS8RPByrNv3bJ6S1X2fsa/wmKYgxsjUMy3n2NeOxp3MvPrAcfiFnQzjgVetffk1aCg8+mn9a6B6pyhNcGq1B0PitN3Tl9o1f6n4J41HXs4A4Nug3tWIaJmGT4GerKKRooGZoJTWuWyVWhgnGZIRdE4eEywOv0lFUg6jycjuUyUdCV+lgJulYGAnhB+aiBWhkAQL/l9gSBNAcf4cArxlO7vmvbpP155ZtrEO05fc/adq5YOOvTV0m2nnfXW+C1186auXNIsDL77wcnvVjb8qubEwalpV525LRsJt/drmlFZn65umraYzi0Oc2s2nQ66cb6es2cH7jbh3CwMU5lo/pdJtDJm0XFVLtblM3JIEWL5rPm4SrX6dPvdLucDRBOz07ypYSTpR2xFA01+GveW41snP0/S2p5fnThu/hVbHn9YWLLywoNfHeg4MGJo9KPkk0/yxXTcG0BubBKnMzmGu5LBWknfmtRZ5jeEveEsM+QYdZZ5MO+eJglJDj19rJvzzLDMNpBGlF+k8fMad2N24e6XyGr+nY6FKMR459FNa1vOejPn17gVxmTDuBPzn5Gc/4w5T6iPLOfSSTZRTw4Z9s9Kq2Tq9zYZpk3S9ojTO1YtmTdjNb+cKnUCc+Sk3XDdUu4T3T8WTNJLt5ICf6Ay2N1Fht7sQKeLbJfn0Ls0zsK5ldJnnfANhX92x3P/+Pp1PGtSChqcivNZtUiknrMhew6dyjxnfrfie9akBNxKEL5+z7/foc6wAnerrcDprW2101cHvmbgTKcPDB25oNke522+UJHd4ez0fNn4ApsvGCoqzTur+72Yt0sV3XQVGHGGEXR4CbhZKZ1sJCpEfGTAyvKwJJa7byLjVomy20Eka0PB9aRWe1rLTrrS/FftCXG6Jq/+/PSHzuILOz4LTDr/3JLRR+vIoaObyBryVfvNSFNQNOI9dK3yfV2kb19XEqBHMQUgNlJAlmnrydR39pOp2l1kufbQFwf5wXxUu5/M6nivYzdZoa2k/ADyFvkhwNVyBisA0MPEUoRgLG7vcbCtwcn65PM4A7mPJmkBKUjLm8UFki28l5yqxUb8+w9nnN48YvySCg9wy80T5l90Dr/oqPcvj8rfOC6Y1cxy9oRH4N55PjCQWSJhzqGf8YFhglHE38xLWkgYqVn4giz/XNuLHePbGIYo13byb5m2g0a8jGOpewUi2rlqIUqMOMvbBnVYsg8kBFYyldPKsIyfeh38IZAV1kSmhIaqS1BWoIr0lzAHtsoVogMUTQ0iqy6ZWsgqKhqUGOghwSQwsCb9smT2B0oJ7NegHyXHwOry31y767sLTpM+/nzMrO92rSLPHZo8wUKG3rf8Q+GUUdpbOyvsUdWqvTXqFOF/lm8gg8+eRudD9mhxfpPkpL4pHSJmBZrVo//SgSKRkzLZs1+Lm98/HGH1B4IF6FCBdHDTJAggQAX1uwFsUUNIhyiWMii2BFa1lDOzr0zAmZcVYTyqjAZegQiKK0H9SWWCnjOF+X2qqYwhBqwXUlwe1eajhtdQkpLR7sJ6oIGgEjAvWsZ4vR/1GSYSTbjgtF8v/EgaM+vhp8cvW7181YSnHp7JjzqV1NomXSLbK3aS2lNGCR+mFl6m7SqYOPHQhPO13fOvSOk5ZHxMTAvLQSckOZq8k0Rd0Oq1OC3MtWhLoBZgprMeZFIFi2yIdWoJUnVPZXoMtezki+771crTVs5M/aZp9m9HXjV11Yzm5Xzs00vD4ebh6U8vLao64SSWM6itJW8C3wqcizuFo3o96+gsNhTRRsoWsJQ9wTgCOShaarFexCgx5NGLbnZQ06mYJL35eXuLkt8ltS2YsId5ZNpaYW97o6lq/JTJEyZOorHgtaBb3KZXuWKs2QmhHKdpY3YBq7owwoo0kBLZIjkkOgDxAwAMJgy3ictKg8SA/nB8hbQSDDMzCkO40oV+YHf0oxSGZJaXzIFxQWNZWMPDWX26z8rCgJReAsbiWW5GUqwDq1z7xpuZLavRcbXkyi8nXDdrxU0ZbRp/gJhISfmWB6wjviitfPhP2pPl9doQ684XBrN6GZB5c2l+/q91mVAstNGSToTcWbPE2R2oW1BUKP4E1SpAcEuC+rGAcUMiziFUioktoSCwr0gnJXIseV8NYclAMUypWJcqspkJN7tMizyTqaFkCImmkt29K36fOSJPuGhsJnPgjeefP/d3C1smksXajffyrx+uu2LWuv3Pv/zOhE+GTznzuf1rH2nR2oFPFnCaGBEfgTWKcVdzTLBVwbA9cbUc5Vu/uBLaly1hmXolbsSvWIGGm5kGHIH8j/E+PwkWI+SqkFUPYEPF5nlMMlsdLjdNSCv3wJccTjcIGPxSlayGbDSo/xjHSxZrMUO7zUGcS3MQHR/moBnrqWLmWHN1amBzMM/6WHDninPmXnzOintWplLL71hx3uyFE5evW9HUdN+l48ZfvuCMlsvF4J0rUs0r166cctkl05avW55MLlu3/Nw5F563e+zll7WMu2w+XUMJ1vBGkDkBbilHHbtG7CTrlp2cA9MWsm7mUQKZ4/PTc6Zk1sfOmRPU+HfuQ6vfgUkMiYzDaYTHsW7W6cB3TrcVRRV1DDicRhTGr0dhvNQOT/qjfvyJpHBF4UciJxKJWAC9rXz+hx9+0D788ccfn2bBmQ5/5qbMe+/BC8fnyVsz2Nh6dS6qCr1AVzKO9IgEScoYnUbZu38/md7+hqgI8fY3qLyYC/h1hVTD1YM9sJ7L1AFFsiKba3E859FMxxUHTjnbwMQ6qzBUGtxYUofuMbxZsCaRUCrznGrqIJh9A4JDG2hmVSqTPY+LBf7iSF1jEwahK5Ng1RVWVFMgL9axIHWx/BjxFNbQb6ArFHmkOQ+zU39ZdaoT3EsU3RNgHnxBDw+8p6noTjJ3/Iun7KqaOu7xm0YPWf3+9keemzDq1pbxYy644sENy4cOO/Tyq9OuvbJl9uqq1OC9NelFsQHJijG/W3TGqn4T7171wMSnw8mGAY1j6of/8VL1zH4Xj7nrL8IZJ81pSE8ZNb3ReQasQ1A8LOyWRJqfHcfKKcWfxAgZqiIaKGPJBUbyjm7VsKzsfIFalXdMgqcNH3na6SOGn0buHH/iiLEtw08cb1o+4pQxQ0781SnDThkxetiQ0SNg5WcdOyiNAlnkAhSR4u5k3nTkUruoi9sSFiFK1ttByGaTzDca7UffRfV1baK62s2ErJvmx2drGRPVupF5MTsXPlObUeTWwvrZfWJJtGpAkm7welhApTGt9JO3W9yFYa56AMs7UKpyWZOYl8tjhQDf7POIyUQlFvxVYjpusFOGGZIZ5j/rJTL9FfzZpW36215t0/O3bSYlmzaT4gc3ax9v2qwdeHD/e3vuvn/Mgjnnz301fV36quv++gG/n/6RtumV3dqWv+0lU1/E7+X93cZ3v2/ZOuiuVdpnZaXPpI8g38f5r/knTHtg5SLc7awuPysxx7I/ni1mR+Vx3As0wFZBKVXIaFNoRLGwPh9PuNyYsIVElONqFGnF6amvGNWS7LQchdpMINv96Cf00EoVZHgRZQLznGOMy2rEuGiIS3cJRWPUkKKVthjjkuIPPXnBivE3jBz5+wtuvHtNee3VYxYtf60hPHbKBeuEvZdeahUXDVkTTty2SjvlskHDF82rrjxzRKVUAPOewE0XN8CkJM5Bs+mDVmLWf00gC/drbSS4fw254l08eJePFpE9i7XN2ubFZHfuUM+TPwwYZxhnQozDMu2Nykla3S2h6tPhX0YUcmrOnKuOjMqThQ+xJLLjSTKP+7/VMIpd9kMd7IgH+94RFSm6ByrYJ6kKHFsqDPK6X6L3HVHHFrk+odS51UY4UcVOVPXYIo0gxLJ2X0l/UVd4sZo0rVrrBwufAmse9glXWNW/Xi+mOf4OITKtsTZjzX5ndtHP7xBSTyyP/XHtl1omXj4yfcLJpT+7QTruFO66Ze0jw7T5ZIL2KDmSHjmiiWLZY0cknyhJ77G4MxfPEiZHiC5AcnFnAZZDEu2S7+WXWaxPCAmIAZ1cEdei1w2wmgAwDrMe/c9pGm7nJqLVAXo9AKbf0hJOO/aVUAsx3dail+DgrmCVjLlNobsop22cPu0P55678dx1Lz8zZeTIqeeMGH6OuADPbpp27h+m7lk3fOq0ocOmT6NjBLAqpk08xcqzdETHKkYUG202gWaWSBOQRCegNROFbyazlWFpAAGgaR1s8J04QABOKsjhALRMxATN4Ub8RitPOguDsQLFKA7ev5/ftJ+s1pax8mD0LfFj+KdpHvtUlithoBCgoFWnIIAReR/mSeA+M8l0gJioJ9Nhy3bYctRMttpZSMInw7dokJ3vWkXiQhyZypWQxO986sYHpq+8mMzoWPLBhekB/cZfYBqzcvWis+5ZdN5LW/fPmpKo7jcZxjiYT/PbTS9zVbQ+H8coM9lZGcfwv53VKhXoUrQa4ybZCCOZE4NsxWzkTloC6rTCcNHrV4yxlNIyXHihkuECq6ySCDNm8QNFllVfMdtcfmo10SYEuYJQ6ujVxaePlReAehl817K1k1vmTztzfCIZn5iePfTei1ZsemT6HGXHWn7F01MvSaU2DkxXw9RujQ+9Zs7aZofvsjOW3Nwjj4LrrL5ieRSmXB6FatI9pphH0dQcAUPbTE7fNoxMGnj0VPGd4pdm+we+ltBjCZpP3Aq2WiGub68+OOoYD+VK+vgEqh7DE1ek6xm0fawy9cd5cv64jJPWQPbhkYuVEwzZTJ7+mytI46e1rv5XTR46J2wyoQscHXN/fgEdc/ecdVZD3Vm/056FsS7Q2sW1kg92yhkcAE49tSNjoZLd4kCLxlJgRUuN7o2CfVgnjzLU6s5yVs4sYtEj+sMl1rzCxgxNGrdvSuJmwH+IABb892f8tD9s2TR04j9fFT1E1A5/Jo37CRC65wjWqvM15E2wrf/jWnVv99I3NGD5NzsLzcix/ZqPoMfQgz5RrM7ImhkHuw1epgmEwMFs07MyN5Oev4Jp10a+isphZoKFZawIDLzGmpMGQo1VFZ8TGr2l5bniMZPvfaBllPaG2Tn0zNCGIYWzh19zhZ/6zGHvjzZqzPPKyw2PilFhrhIzi29WAchnNebTSP0zXwmm4gEt4qtftN9Fnp5/XmX/ISDv0oB5PgTMg3i1hXV8QISv71GXPkMKWvUmOHp5vdHrJ1dhzzKi8yvs86ibL5DTrQ+u3/H47+978tURo0cPGzZ69Ahx2h937d7yp+d2Pzxr9uxZsy64gNVCdcElzVbSTPykiv2aQALa5/vJQu1WUp47fAumOW2xli7SBi/uPKQuZOAMTrqD0s7JhQDf/Y55k9HrSxNB7cmsq8hGHJgnqU8bzPVMkQt5uchjZXAvR2v0foMMVYoT2SA74UlkgoW07N4PoraQFuMXukB2RfVVyRCzDWVsoZyxO4vwKOhRZRq1KnKx7B8iq0IZJV3nymESWFUKLDU0C6OpGNj5zSA/GnIL+pBQe6j9LbKErDy4fPlXL74oWVOu/EU+msWctvUb+BEdr229996tmyfNLJoXxJwKpElWp0kVt4GjbVRAzelKOUcYOYqEQSHu0wV2FzogHPIxke0L01gFeuHCNIgRLtaldz4FwvJjdofTJRdSg6GwGCZfAiaCnBV9QrgKURLzcAA5zAU9yWElvaunHiT5oae+6kkYgfTQYMgvU4E2CtVhNdxA7kTuW5aFrSSSmRj258lTa9n+qepCYJyGZLY/Y5wBiUyqP4WQ9VYwhQX8OFvJvlxgpe8M7Tfk57UfNkJKYtghkU0YqDOTSOLHiQFA6WQCD5P9gdJDdT2ZKS2rwXI1EKIeNZYCmidkta4f8lqqPxC3Nk11qMrhcvShRX+p/uyDQaf2rVb/xJZnXD7HHkfVduzplYF5boi2RHgbdCX6q5ZxmXL0a1YZhbYsItAvv8gE4GO2gjk3rRUlFirCyqlXAhVTue7GcrG6e1XCBgGigxIoa/eEyqtY7aneK6lKznBmfy5nB51wEVZ462dh2SDVqvk2/ZDz156XIpYp8y5Nnz3ljOyMC2f+OPfdo6TFcJuWznvgYjDqB4+ZedvYlsnD0mMG9X/vhJOfE5fm/KgCqw81L+TMnBsw4NjuFaJyZ4VosLcK0UK9QvQxwltAaLMaUVnP+8/ViBrJnj2LRUU9+3N+16JR83SWDHp0FCsezR8nZs1MOk4l63HHuR0rWZ1ygMZwZdXjTfdd1CoY2KqX6tbVOtrqVuVK/t4JvvLH7AeeOq/7mAOdYy7pbczogjbnbHxRfpzwNrvsZ45OgaUlwOAxgbWoc/A2CgnLCBAc5mDuSfKhT51EZpffN/rV341tube2K92l2uKn5g9sPaX43DPHn9ee0it3O+cyA+ZSzlURS/e5hI25YMzMUpjMOThdidYSd9ACmi2ZtdFTqt2bSBg9E7pNOcaioQeHPh+m0dDiBsXVoBS7Vbv7J9xxhe6fdhzYtPsvNMppd7c67C5vbasTX7ECIFRcCG+L8DUDH+WFO51YClCIR6E01+pwsqR+8jjqjcJQUXGX9P7uRPcGy8MRneg+mnxFwkD0ynyiU3ORx32axH3awKNs60n8GtvaX9ecMXZMZXnacbdt3ZXG8end1qFm3eZILDywCX9FUk3tzWwpRH0dJsE6eGlfgOXdV8KXWwk5rkSTqg2OSrvTG9NfMaHL6aYIPwyH4S6roDoxh1QiNNRRhE3dlLAnY6JN3mD6PpoQkbdhunSGxEnnn8knQLnheryPzXh6zgFpTH2v7og8+jc6Z/7XhkOS6lE2/4Lc/B/oOn+lNGlo0TxKROPIe4Z12IUM2SJmQrDGHdgBE985uxLDYmaphkWg2Xy0sjwjF1Lo4ZRVpAk62ExGxWMhYg+ah308Agl5CDafQMvWLLjs9tvmz79hCCPQiAED+jc19e/flCNQ6byV110077pr2lUmc16oHziwvj6ZNOr9zVW0RtJLe4HSTjDJzhJwUcJkwqzTbcfyNKeAZdn00KQX/zn2KXIiV5lNHQxWnrob9EJpPzV1GklnZTa26SFgXvFrxXs6XuOdHd/wyfZ7Nf89YJYuXdFZrM0EJd/C6gB9ev18DbeCZQlnyzv9aFhEj+m2RfSUUU7f3yinxzYgJZ1RgVqMFoFB2hosK4/hRq2UHytw+US6aznVV0Q/ilRiQMAcQ5zi+AW196SnTdVHOT5Z2dXW6rU8v2NmVwOM1WTyZuy94sNc9eNXzPt/rmKeJs2g5LI7jGzY3Arlyi3yiug7iK57OxfIULvdxjbx/zo2xZ34meHpmjZ/eFsMFZsbHmgnXbvy3F9gfD4zy0kcz6JsWDOacdGuYDA+b8DpctDyVpqe6KSdqKhVRV1owRAdFjOvaC5dkKYqssF5u+hQIW+of8nXnrs6h9tFc/70Vl6HAkGn5SRqE0cxEno8aiIxI0msHQZj0MhdPQ5prW7Fgw0x9LptD8sIRLxTpqe2oltORU9Nd6r3ER7KXwRnL5GizvXY2z1mxB97ETa3GdYF86hjRh41dS3Q7GlaC5nLm+YlOighhw9hVIN0rnyUNBnsePhjvfQf1v1hePnsl15fsHSuJrIXLKT8sM5WO0hTjp9wvegN+GOYu2iifCWjV4RGb130+h7KRDJcH+t3ZQy42tjou+AtuMWMfB4ZS+/TlTfovYRjHXDDP1G+cAE+nKJXqzhY+2YlxOJ8Xpa1YKdZC62Sy26pVTkzzeGRzG2tbnoioFd+2DmjciCAfhNviNE3X/nA+PLfC8YC/xdpyuni3ML+NB8HK+3NrS8X1/uL2LlCzLWlucAOo3LPB5zMkQIRjFd/UuUklnMRwt6cmDuOgtuXyDhog14H5ibYqH6xoQPbwXpkYOJwUa6hgpmlmqWMhiQ1RCbJsIwmJJqH8Rs7G5NoM0nTKrLrb39/8Msv+YkaP8toUAJvtpEPPzukbdD0uu2XAce6uBgJ9OgioJTHVXc4aXgsYPitlYXlgF6jyayXoVdfMaLXfj/bbKCmG5SNNijBBkxA9wGUDQLayIeyPner3xcE7BrAV/hWayQahrcV+JqBj/KgbCCdgdN4FAEo6w9EKhiU9YFlEI5URLtAWTQ+W212t8wK5R/jC7zFTEXStgeKRVZLaB3rcdofCL1i225NEWr7ALY9myV0x7bMvqD9E6i+8XNlWBXRSweF8t46KIT1DgqtgjVQRNX9zzZRyNmjx+mmYNLFUJ9dFYRbdF3Zfezj/vOxZ2HsoTK2RGpRcfqXTUIXaseZxD5d1vU5CX5Kvr3aOY8Q6Kkp+jxKjXlEcB5MHxVZaQFFuT6PKr3VHdXtSrn8mOBy+0OsOQNIIR9teVza+4S6atrjNLqQ8qXqLX11vRCfzLdgM50tG3LzmwHzi3L1sOPZ/GLG/GpR5cZVe0kyl4rjTbSGfcWw/8upExf3vzuI+5+2y1YrgQysHzYlQ7zbli9vULwNSjkINtjyXkCs+Vve7W6V3V7Y4x58hW+1lpaXYCt2fM3AR3lb3pPOwGk8KoUtL3tKy9iWd8seb353drrlK3MLUYMLYQ0WR/WFKER1oNbGel+IXnf58RakuI8tf0mfa/N4N6s2ayyPqK/NJLqHIlw9dnrtsYtwE9UmsV+FUpVbA31LIbzU+1ZgGUQ/OOzXudGwTTk26GwVXF7rLxQSfaCj42y3sp5gqe+d19EdOxFuJbGLbnED0IDzNltpvoSVxMjK9aSeNN6n7SX1d2t7tTfvITUit0F7i9TeA2/fgE+1t+DF4PEtpk8lEay/Yq6Cm6dXw5QZVAwJbUaptM9Ka4dQBhVYWZ20T68aDsuPmQSXI1iCjFNAO0OrZRjwA6Kx8phWriBQwVwiGZPZks5V9dAkO5l2rsQEO+IL0gZ4XiTrwBgl3ot3TNw4eReSb/fNUzdNfZGcfAI5MvHiJ3c+c/ocsjDJSHbK8jmrdoEKB6qNWDPvhl1k5TNX8t/V/9Rxcox8mV1EsSDtwwHyygNzHdVbJ46S3jpxIE4ScI+gXMKaDrc/iDUdvbflyOmKHv05XjY0RM8+HdL4nB31vx8jFkC0ur2BYtY7Xg0WpvsYY8586jFGss3QAD0HaSrrlP354wyjF7jnOCO9jbOiGy2z7kCwJMx6uzJF1gdR84V+j1FvyZf0vY+8U8YDz7OxT4Kxl3H9ufN7jh6J3C+pBkBwVIDgqDWm0uoVOEDPIXP+pFqr7FY4WW5GeaNWAbLG1v7lmAvslvpcgj6kRc8VEXoREr1McVd38cB8O6JGbR+ZG9i9K4cn15XDq3flyPB21gG6Z2eOnGs7v0VHYc7g7mzVIbTnmKSzh5QdZPRpeV3bsjYHtV5tpras4Get4qT8jlcq70gkDOBjNvoA+LGqwswAp5/2+u3WTqopoxG79pF25L5Z625bccPVpu0HvvrwwGFtP19+8dJL5rD8Blj7ORLmJy7WR0Sb8pWLbUpjHPuE6+lWagrWM+XG5t+G55NWNAA/N6D5jKPC7Kp+KVjnkmLq2suKheVVjdRp1KAn1pVzNHtaaZQzZn9JmsHlgZW0KbhT7KsGjOQ1TqUVyVWE/45U9x8+Znj/1Mg7Lk62fXTB7SemHhq+NTxhzG9mnnLK2KErZl15rbjw5Y/Uu4eff/qgAf0DxQP7nTNzacu2R0srvqlMLKtJnth/9OLxw+c2No9rOHH8xTOOrqfyn/bOkCJgnUW4WvQOd3bPqOzSPaOmS/eMOkoj7Jhe4aZeeL17Rj0qTrQhrAUhRNdKTM6a7YFiWl3o8mS8GOH7j9todAaEjttP4z5dwk7rs62GaY4eJ7q2s79GPg0qgAbLfmkHkbo+OojUd+sg8hgQIFpda1Ag1u9/QYHORiI5HH+8jiL99a15nM4iQjIv78egQRhoUM0NQA9rJw1qutCgoQsNGikNYkCDGH2kiUGDBNAgxuHTTIAPaOevOsoIJZWMDK3e0nAFBVb/KSd0cZ4clx3OyVcL3j55QhyYbwFcmWMMgyZOoMkAbhBJ5tMk2YUmJ+TRBEx9NVQDJkGEvQ0nWusj/cAkqEtisieaBKWVaBIMpqRrBNI1utWmTtKd2M0qqGtQwg2Y5VkKVkEYrId8q6DU3VpWipZ/Ob7Ct1r719XA21p8zcBHeVZBeToDp/GoP1gFZeX9a5lVAAZBuKZ/bV0Xq6DRWDyaPt1EmbikX72xepGqarp6J8igNzgMi2J8FJOGzbTphl3+mXXsPf513PVc1Yf9EOl7aZPdDIhFndsebAi2viLt89/ADeI25q9wrMsK1+WvcEVcOSGplgA66FzHKgACoSpOBwJVbrV/bkWVOCqMFFtaCgwy1kAMKRYHPYKtJVMeVaaR5br/LTnzPXY5IuaDjN4IuseAFlfoFIwYCKM3Wr6jI4x2pyFB3s5hDYOWmRwtH//FtMwmWNLKCXE9GboHSbNxFmXrStUUJquUs6w9JGxcT4xIoaCpiFFbpPwXEVY9IQHSujyUPh6JSa8kzu+H1KtAjhnhOQ+j8fVGeK437RTRI3VHv9dJLJZ3xuqoPJI0cRHXj0twJwC6yoTRG1mdVIsAvdQmMg5M0PTQwj6lOZFNBsOOXJWFIiSUpDs7oLN4BihcA8Knxo1PMEOiYp+ZZAJ9jQNZ82FaK1PD6c0AlQY5Y3FU64ljrij8HihnPEVh2ojYo/sFg0VI6BKa/TMgzOrkLUhkxeFRba48ElfrNA6iKDB6CtGWQhXVsW5Kj7UYmvTNv5+ZMvaWhy54qu2jhSP/fNV7hOuoN91+7QtPnPHE9Td+OHrm7gf+8DxJ3zL7qgVXX81vIo/ycye/w+g88eSRY1+ZvWr4CO3LtruuvWPywVi/2RcvmvLUg4zQZxPz/Ks5vZ+C3puqH3eDHmcsY3FGo0GVUh3PhnROrcnv2VxMarNRFmHsr7cJyARKUd1jY4VQGaVd1POY1eETysNUfoawDWY/TIFuDZSGaRtMaxlSUJJ1Vu270VUv8cZee18Rvlu0sZdeWNqBbtmeyG+0xxTgIh9XCrv6yu5dpipgM5exLlNlOltV5bpMldEuU+V6lyl8HooFGckf0B1+Nk8wVKz7mXprOFV2nIZTeflBx+k8ZaDB8/puQCX+wOBg+8fYiKrbnIvZ019+trNWVR+dtar1zlo415LySuatbXW69CDzf9xfKwf8fqbRVrlhwvfRcIvsyPfhds63gqvBHuVd5wuSOxtl8zXqs/rn5hul863U51urr3HGH6hA3q2kq1wYCrNVhpmXlPUy8+hxF7pratJxVvvCfLBn63vJhefz0F7HW/q6izodRNpHJcYluWu7U6IKKBFhlNCRXVlcaUyqhQLKXqIMzJElkmj1WxAJFNMYDzUhG+CwQn8IoJrCLEmsu4xhmVqrzSOw1D5suYIkicjHIUmXxBBKkHzN1DtxXjMU/eU6YUhJzpfQy664SNf0HfOBPPz0vHwa/thvwYh+l9Yc5MVTSV481fwz8drZ+rZ8jjQaLRyPNOV6XXHr4OXvv/T6vcVr1+nsv5M05kobjsb0G/DHroeXL+D6XeK1JC9ea/75eO3SfF47g96nk6dy9xKOfQT3WkdrMbvEa0lf8Vrz/w/x2lJj6Z8ijef0KN48sgsHa1reGa+lvZukKM1pnckq5alzpCrOekywQGaJNec5D1jbWPU1xQkYRqiQtwtWyekO2XDnBzwZ2euhJm9VOXwlwFG9ppqk3KOLgs3V1Pkbaw5QdzA2eopWcF37PInvvXaK5aTln8xSxo2effsVH8565P67tH8d+177b9J81fxlc5desuRy0tZG5JnipsW33X9JKqaMOP3mDXPWand/pn2m7SGetltu2/zgvGtvZD01af84J+z3ulx2YveuWUplXPVXgSlXyjZ8SaK1prQSTLl+RsBXDYXRBKjvrblWQzc7rl+DUtKAQYYQ2HFAvKp8Oy7kbi0KYTinGF/hW63V/argbQxfM/BRnh1XnM7AaTyqBjuuqLg6xuy4UFFxSVV1rF8XOw5d9K2iP1DHvMJZc2EpfXqoYvNkwpEKui5mt/6kr147fvUezu3WB2xvH7ZZj/5g4tvdo7mCznMRmqlbgfFQmiVQZHQMC5tyMQhMyQF8Wqq7BVH1BDm90Y9SKmcFd4GPJRWHi/roHpbnS+qzjdg6XUbN7LObmHizjhwuMtqKdZlHKG8eXTufRXvrfFapdz7LCgVFpTRMYpbVsvJf3AUtDxr00Q5tuAEK+mqLxhMDFeTPA6XAFH0e5cY8qky9yQFznhzIOF3FaSoJHhNkAHoFdEqY5K0Lgd4Xpqtrp8/VmdvF3d/nEgmT8zX95B7r5IT5VXGNRNLnV2PMLw47vzSuOstg5wfYzvcnWisCpbDzI0m9DEX1hHDns6f8VgMZqtkjfZEMyW47P9Kg+BuwisIDO9/vVsvyd77H3er1+PEx3PgK32otj5TB2zC+ZuCjvJ3vS8OeLWO+HK7V6ysPs53v8fr8ZeXhSJedX80WogoXog4XoiCg85YnE8JYCyxGvKavxejDP9PnoqzoQwBE+16fSV0lQcfU3BLpeGw96E4HzdptzD1Tr9RYpSh2aIkr8aQqgxatya1FkbWt1VmE8MuX93w9OFlnDsPJajPab2qd/uTlah8GeQvoI844NVraFzm6GP+dROgKvboQJOdcmW9QgERzoKsHLdoN58q3xn58qLOvwmTuPTEt7qE1wcXcQA6gUNYscMVirfE8uVA866UnKJYQ92ECJbYrDiRQVuqV6aY+HrqHD65bNWbkyF+NGTHitDEjTxqNv/lZ+/cfOv20ll+dMqFFEE8bO/7UU8a30L2TFdeL62i8OIpRdxYvNlaFtkeqzI8XR/R4cZURL3YhwG0VOqPFpp7R4gIuEP3PosW4IjG6BNdd2bx+0G24Cr+Zd9KGUetJs5cMqR22dN4t1U1LL7Ez2g+cMG/ib7WjSP762RfPup/4po8m+4MPaYWuPz48/kSGRWk/Ot3+ndJnR7qy3jrSlRuBTmrwWuVWw9zNK4c9Xnu6nJbq0afuHF039exXZxqrR5G7j/2s/3zsNJjs8RfSrtY2OeMKFVGB8XPjzoWWe/bXm2zEJHoMXCzqzNPtHHcFVsD0Me5ob+Ou1GluGKBIdd38BLAD1ucvmkFXNdRjGuPzlU+vU8kLNcN+YfNhdmUd5vL2XlMNC9Gf2ZKVOTwJ02v1C4Yh2TnR1pgNA84ROBmhj5NHqMkMSg81HqW0EvOoDtcvmm4fgegeE9/WMw7dy/Sf7hGGxjg09syDNQ1w5b11zQvHUUj88q55ncHoPtrnJY3S9l7a6IlvdPIa7QNLe0hHuAv1pwuCAMtYCRNpWB1O4nqfFeoQ5QOJhNFLFePUUb2vdKtJosVsSrGsWindQ2ifoTxTyujjfa16A1AgvYtQjG301C8nXRvBYvtpZ2LTxS9+8P6et+Y4zebOXrAWTlty1ejxZ9HG+iC6bhw6vWs/WEGntUiRdANacF2pjS386pL46G6lOkGfzBvcp5YCJ5W66WRq9KfvlgaxjBtlVxRMNWyjVcM62P3iReqrl1Afa/ZyT/bqbflMi3rJc1h87KB5nOk1mHPUiGDTp+zRRwvAVOkz3/BpVbm8xGyBw4fP3SuQcuoqz7RAdG5NZJyltAIW21VU6STJyAJ7Ei/tn1UK6ktWOXxILyxvWQ41BPNKXZzGk6TQa0vdNYvJmWTokOuiwqzO2pfq2+q15zSFDNu2ecTS6ujq5i3b+PfJJWSV02okz1tt5CZy0Xc/+T3Czd7AUR3HmpeJC+muSnCb2PMFlRJARGIbS2uI6noZGKAT3w4Q27J1DnzuoP6sVKIkKQnCVlrWVd2Z8lCvi1YMCFSHMdNBYEVMEqgDpd7TapEL65iK0CvdHFEgjA8RZ4YLo8NbFbD3I34/R54m5tby5/m1YlL3Z1ybDG9fMeHnv3Tq7Ye+I+6OgPnu1ZfsmDX+qTXav+++9cimw6s7TRzBTHbxi+ZMvxo0vJ/UnzH2fvRqWVbc2r/hYKzfb397C7GoOrjqf/nyhaxGUdTMkzgLlc7zu2bIoD+oLIn9h5XCBE1nYukyrS7JbNE7Kcepz8ZPT4CM1u0gLDS3I5KhzQgUPq0WS/iAhcKyvrJr+toreck2O3srrOjMuxE39tgXhNshviOWUzsugv1BgAlyPSmccfbEQ9SXii3dvYJlR76W6+LewuvuFd8W7RI+yewxTnHFVc4NlpLFaEbX6rO4LLSNAQvxqaINLaXCOO2fmG8XeRsUcwMmuopgF5lp2munXSS6W02iGQwhCV/hW62y143pr/iagY/y7CIpnYHTeCSDXYSymNlFoklC34a3S1NamGuvxk2fLoy3e+af5/eF4rp0ffq/fDaBZIVH+Q3wWdDoX4U/+Q8Kgj+ZIEwj2U8+Yd83/4Lvm43vh4TnyGb6TKGY3mkDrAgrsoPFaApHMYbEKtDx75s8zUneHAkFZqf2j4xqnwlvn0O8C7TvP+fyrifh9WgvIE6/njmu8PtUEa6HlaMiTwvnck/cFkIng9JzJn4Df9/vtcBu7RM2f3yu96vcV3C9KtrPhv9lVzOe2Z17VDfqBBibsJjO1YV5lALPOkuwCSvOhPH8R70Rnl7gyhKA2fQxPiGCsNPdwAYpqrqThOzuQZyAQaTOcWAPkVGMStjOkRGKtm50GrMDls9hWVfnRLGPjpkaDo68SSe7UvIw/C505VG0k7D0eenCA5SuDm4klQTmpE5c0HP/xxEY1P+x+yoYi0G4meRRfqNYk98fx8z645i79MexsP44ll7748y86+Yb77n3hpvu5g9ueHDzfeu3bKHxq0XHDkgzSVqvlRuL11f9kaQh6VRXcSKRk3qVeZ149PaHWY/+hHrWN62Mteep6vGU+qo+jnNPrOdPnXo2Hp01jR9tnDOeXj++22/at3U60AR7y0Q4yuGsY5OZPVLM0qVpU/deeHkt8PQesD2uRR9URi/XeS2C12ru3r/mrfxONYQbCfbKKtNzsKOv5zKV1O8HAMpm9JPlSKXNUasUJfEpX8wnnjVL9Fwgia2JfLQdMvUPAk+FzG2ZEE8bzJbQBrMB7DhPG8zyHO1NSn2GIR4L6GNUO5bDSCN6l1knK+aqTjVHU8kmLtddEx8oZvYjzAqw4tsKLjby1yJ/5eoqMurbnZtnnnzViKUPBMmd2nSeJxdojyaJc+11V6rfay/UkA8zwVhK+YaEJnxWHr31erAlI5lv08e4waTgC2b3u/kDpk1UdhRyO1mnI7XADjwlUY7NWJy+RCKh18+zU/SYPfiMPjcSHxC1T+8p1fujIxUTqyfXuwkX0ien6vXkWNFGu7wfOvhPqil9DU7F/6xq8/9kUgrwabo2Pz5Nt8Dm8xtP03UhzELYATSU6AOzmPjHFlZEThZjw1W5OSrAvyBYHgP3bCX3/7jxka+3itKjtz1kFk2Ru+/ueIE/EX7e0HiidcTJ+iUdh3j5cm263gd/hjgDdlws7xkNuc7aVrajGccx3QP4RsY/OUrtEnzO5mH6jKcysEzuYpkVSnmSBt+UcLKXpz3hY9wld7ZUf75N9Jc8+gnRBLbIDyTUCnT/sf7b5V6EoBbqkVZLC2m2QanxdKiMJVDEPEy9PiGK5D+kp8fjovj9xmN7ej44ipe6PMiHpzT4nNIghN2aKQUCyb4fdlX0S2eMKQew1ahZGjDmmv8ErIwFqwH6nmOvU/ust0m1rzGeqSPifCxOOp9abiB3Aveh/jS3mlRSn1VVU5KubIYLxHDL4PQyhWyOWLUM01RLGhJ0nZN0nRWbW7GG98nAGjSPqSxBk5V+GR0wO6wwgUasUpnI1NAWSDUx+Fr/GjzsD9IH851S8LW6hHoCfG1AgiY59TeIpqbQI46uIuUEWU020CehYKi5bkDf5Iv8bxhnQY8z/+yblX6Gtdj+snD6WsS5XcZK1OkroVT93DqAJO9B+AH/HxMeAyRx4NPGLiSvM0jOwXs4rG/4j0n9Cyl84JfQVufw/wdKBT0FAAB42mNgZGBgYJScdeL+RZN4fpuvDPIcDCBwPvbqCRj9P+OfCAcfezEDIwMHAxNIFACYZQ3OeNpjYGRg4Oj92wAkF/zP+N/GwccAFEEBLwGTvAaoAAB42m2TT2gTQRjFX+ZvkCA5FCRIKSIiQWqQIqXIEggeQpAiQYLIUooEiYKHIBJK6aGHCCISSm8VZAmintRTiaVni3gQERGJtx68BA8iHoo2vm+zhaA9/Hiz38w3O/vejhrgYhqAmQCUUMFdvYO2PYNps4ar/jyKDqiqE2irTeomAhOiKHOqiqJaR6DK7JnHUdYqZInMJ5wkdVIms4mWZL30yh4H6A9wfho3bBuwi+jZHFp2gJ5ZJnU+v0PLTaGnngrDhr3Mehs9/wA9t0oWuN4lWuZcAwumi7zL4IWdAfw2963xO/dJF+e4T4dnzlBnTAlpXRn+Nv3UJfMJNZtFZCYRUkOzhVDnkOe7nC0hUk2sq+ZwxfyKx5HvI5K6+Rmvj6RHdxHpPeoSCpzbMA8B9wUTJsIRGetvmNWnMWUaqR1qNfYy8Z7jDpFak7h4zS5u8WzH3HPUdRYFM0h66L3UDIZ7+jbPKj6mUSAX5FvoQ2QDNMXv1JNhn/VQH8ec9PsMziZco/dB7Psh+MdUZhHnMOKlKDN4Q++eUSPyh1kVDnL4F55rNR4zi3EkC8nMvqJ/9P0wfI06OcphHGbwiP6vUe+R3dj/JIf/kH9sNL8xjmQRZ031b9HyH7lW/o8+tsh7/Zr1O8wrUbUMpL6SYAS+U1eoNzkn9yDB8L7wTlVT28gJ6gqKuoOcYE5xrHDdfWYm7FU/eKeI7Ct3w+4jaxZ5rvvIC+kIeeT/Agfi1MAAeNpjYGDQgcIKhi2MM5i0mE4xRzFXMS9hPsf8g8WKJYGljmUNyzFWMVYn1jlsXGxJbHvY9diD2K9xeHH0cJzjeMTJwinB2cNlxdXA9YzbiLuAew33Ix4/njaeJTzXeHl4jXgX8L7js+Nr4nvGb8e/if+JgJJAnKCSYJhgm+AWwSeC/4SMhAKEcoSmCLMI5whvEuETKRE5Jtonek6MRcxPrEtsmbiIeIz4GgkhiRKJdZIykhWShyTfSc2QOiXNIW0mPU96l4yaTAoQLpMVkq2Q/SIXJlcjLyUfIf9DoURhhsIhhQeKPYorFH8peSnNURZQtlKeoHxFhUnFQ6VI5YDKM9UC1X9qF9S91Oep/9CI01TSXKRlpNWmzaEdpr1M+49Okc4inUu6HLpJuof0+vTe6AfoHzDoMxQwNDJcYfjLyM9ojbGCcYLxKhMjky2mZqYHzDaYh1lwWOyydLDcZWVktc3ay7rKepX1Axsrm3W2JbY37Gzs1tjXObA4eDkccJRzrHJ85JTitMFZynmKi4DLBlcFVx/XczjgHddXrj/cBNw03ALcKtzmuT1yV3FPcZ/k/s79nYeIhxUQ7vF080zzfOEV4C3mfQAAxwuXMQABAAAA6gBBAAUAAAAAAAIAAQACABYAAAEAAVwAAAAAeNqdUz0zA1EUPZsEMb5mFMYYxRYKhawNCqPzEcaMj4Kh0Ww2ESERs9mMoVIo/QyNv6BW0Kr9BOM3OO++mxAJhcncu+fdd+599573AmAEj0jCSfUDiGgWOxjlyuIE0rhVnMQ67hSnMIlXxT0Yx4fiXkw4vYr7cO+4itOYdp4UD2DReVc8iKPElOIh4hvFw9hPvCl+xljSV/wCP7mONZRRosW0axRRgEsLuA6IQtRwgSvOYFgnjLp4oM3BR5aWUZTFDKMbZNfIq7COi1XiiNnGB1K/hnN42GWsSORij/Fz1LHCnQpPXSYOZa9AH5GRoXXy3VaGQQ1Wtth05P/JP5C6de3FZHiS1cxpZmRaGd2qlcUbfWKZzXRb5TfCGWM1HHdoEchMrrCu+M1LNKIvSbVY+rLql+W0UCLmFuz6lHNGwi3Qhy0965ygU7fu2pv7ixldwix/l/LzuN+eHWquJ6hK5n/zYs56IVMVRfMSuVZ/T2pWqc6WTFOUSez8jW9zxOQZpZZZJyDPrtpzzMv7ea9zPMH/te+vWp70XOJupa1mnZEtbFLHHHZ48zl56abmIXfzvGFzTqwvyCejIeduyytwMc+YfY9LtEX1zf/Nwidgq6ieAAAAeNpt0EdMVHEQx/HvwLILS+8d7L3se7uPYt8F1t57F4UtioCLq2JDY6/RmHjT2C5q7DUa9aDG3mKJevBsjwf1qgvv7825fDKTzGTyI4q2+uPDx//qM0iURBONhRis2IglDjvxJJBIEsmkkEoa6WSQSRbZ5JBLHvkUUEgRxbSjPR3oSCc604WudKM7PehJL3rTh7440NBx4sKghFLKKKcf/RnAQAYxmCG48VBBJVV4GcowhjOCkYxiNGMYyzjGM4GJTGIyU5jKNKYzg5nMYjZzmMs8qsXCUTayiRvs5yOb2c0ODnCcYxLDdt6zgX1iFRu7JJat3OaDxHGQE/ziJ785wikecI/TzGcBe6jhEbXc5yHPeMwTnvIpkt5LnvOCM/j5wV7e8IrXBPjCN7axkCCLWEwd9RyigSU0EqKJMEtZxvJIyitYSTOrWMNqrnKYFtayjvV85TvXOMs5rvOWd2KXeEmQREmSZEmRVEmTdMmQTMmSbM5zgctc4Q4XucRdtnBScrjJLcmVPHZKvhRIoRRJsdVf19wY0Gzh+qDD4ag0dTuUqvfoSqfSUJa3qkcWlZpSVzqVLqWhLFGWKsuU/+65TTV1V9PsvqA/HKqtqW4KmCPda2p4LVXhUENbY3grWvV6zD8i6kqn0vUXCWqe4gAAAHja28H4v3UDYy+D9waOgIiNjIx9kRvd2LQjFDcIRHpvEAkCMhoiZTewacdEMGxgVnDdwKztsoFNwXUT8y8mbTCHFchhy4FyWIAcVhUIh3EDO1Q9h4LrLgb2+v8MTNobmd3KgCKcQHUct2DcyA0i2gCHRClgAAFTOCVIAAA=) format('woff');
font-weight: bold;
font-style: normal;
}</style></head>
<body id="aa-app" class="customize-bs fix-for-bs lang-noop lang-cn section-storestats  body-page-app-reviews wide-screen branding-v1 no-touch ng-scope"><div id="lightningjs-usabilla_live" style="display: none;"><div><iframe frameborder="0" id="lightningjs-frame-usabilla_live"></iframe></div></div>


<div id="get-started" class="get-started-container"></div>
<!--[if lt IE 10]>
<div id="no_old_ie">
    <h3>您的浏览器版本太旧。</h3>
    <p>要享受更顺畅、更安全的浏览体验，请选择升级至以下浏览器：</p>
    <div id="browser_upgrade">
        <a href="http://www.google.com/chrome" title="Google Chrome"><img src="https://static-s.aa-cdn.net/media/pictures/browser/chrome.v-8f9bd35a.jpg" alt="Google Chrome" /></a>
        <a href="http://www.mozilla.org/" title="Mozilla Firefox"><img src="https://static-s.aa-cdn.net/media/pictures/browser/firefox.v-fd4ea3bb.jpg" alt="Mozilla Firefox" /></a>
        <a href="http://windows.microsoft.com/en-hk/internet-explorer/ie-11-worldwide-languages" title="Internet Explorer 11"><img src="https://static-s.aa-cdn.net/media/pictures/browser/ie11.v-fb7889f9.jpg" alt="Internet Explorer 11" /></a>
    </div>
</div>
<![endif]-->

<div id="container" class="">

    
    <div id="sub-container-aside">
            

<nav class="global-sidebar min">
    <div class="global-sidebar-wrap">
        <div class="global-sidebar-inner" style="position: relative; top: 0px; transition-duration: 0.14s; transition-timing-function: ease-out; transition-property: none;">
            <div class="full-menu">
                <div class="section logo-section">
                    <a href="/dashboard/home/" class="brand"><span class="full-aa-logo"></span></a>
                </div>
                
                    <div class="section action-section">
                        <a class="primary-item" href="/dashboard/home/" data-name="dashboard_home"><i class="menu-icon"><i class="aaicon-aa-home"></i></i><span class="name">首页</span></a>
                        <ul>
                            
                        </ul>
                    </div>
                
                    <div class="section action-section">
                        <a class="primary-item" href="/labs/" target="_blank" data-name="dashboard_labs"><i class="menu-icon"><i class="fa fa-flask"></i></i><span class="name">LABS</span><em class="badge-aa-new">NEW</em><i class="aa-link-icon fa fa-external-link badge-external"></i><i class="aaicon-aa-lock badge-lock"></i></a>
                        <ul>
                            
                        </ul>
                    </div>
                
                    <div class="section action-section">
                        <a class="primary-item" href="/comparator/landing/" data-name="my_app_analytics"><i class="menu-icon"><i class="aaicon-aa-connections"></i></i><span class="name">我的已连接应用</span></a>
                        <ul>
                            
                        </ul>
                    </div>
                
                    <div class="section action-section spacer">
                        <a class="primary-title" data-name="market_intelligence"><i class="action-icon"><i class="aaicon-aa-caret-down"></i><i class="aaicon-aa-caret-right"></i></i><span class="name">MARKET INTELLIGENCE</span></a>
                        <ul>
                            
                            <li><div class="secondary-title" data-name="market_intelligence_custom"><span class="name">可设定</span></div></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/apps/comparator/v2/" data-name="market_intelligence_custom_comparator_v2"><span class="name">对比应用</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/insights-generator/" data-name="market_intelligence_custom_insights_generator"><span class="name">商业洞察</span><em class="badge-aa-new">NEW</em><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/alerts/feed/" data-name="alerts"><span class="name">提醒事件</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/advanced-search/" data-name="intelligence_advanced_search"><span class="name">高级搜索</span><em class="badge-aa-new">NEW</em><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                            
                            <li><div class="secondary-title" data-name="market_intelligence_app_store_ranks"><span class="name">应用商店排名</span></div></li>
                                
                                    <li><a class="secondary-item" href="/apps/ios/top-chart/" data-name="market_intelligence_app_store_ranksing_top_chart"><span class="name">排行榜</span></a></li>
                                
                                    <li><a class="secondary-item" href="/apps/ios/matrix/" data-name="market_intelligence_app_store_ranksing_top_charts_matrix"><span class="name">热门排行榜指标</span></a></li>
                                
                                    <li><a class="secondary-item" href="/indexes/all-stores/rank/" data-name="market_intelligence_app_store_ranksing_index"><span class="name">Index</span></a></li>
                                
                            
                            <li><div class="secondary-title" data-name="market_intelligence_downloads_and_revenue"><span class="name">下载量和收入</span></div></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/top/" data-name="market_intelligence_downloads_and_revenue_top_apps"><span class="name">App 排行榜</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/top-publishers/" data-name="market_intelligence_downloads_and_revenue_top_publishers"><span class="name">发行商排行榜</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/market-size/" data-name="market_intelligence_downloads_and_revenue_market_size"><span class="name">市场规模</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                            
                            <li><div class="secondary-title" data-name="market_intelligence_usage_and_engagement"><span class="name">使用模式和用户参与度</span></div></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/usage/top/" data-name="market_intelligence_usage_and_engagement_top_apps"><span class="name">App 排行榜</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/domain/top/" data-name="market_intelligence_usage_and_engagement_top_domains"><span class="name">热门移动网站</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/sdk/top/" data-name="market_intelligence_usage_and_engagement_top_sdks"><span class="name">热门SDK</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                            
                            <li><div class="secondary-title" data-name="market_intelligence_user_acquisition"><span class="name">用户获取</span></div></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/marketing/aso/ios/keyword-top/" data-name="market_intelligence_user_acquisition_keywords"><span class="name">关键词搜索</span></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/marketing/aso/keyword-compare/" data-name="market_intelligence_user_acquisition_keyword_compare"><span class="name">关键词对比</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/marketing/featured-apps/" data-name="market_intelligence_app_store_features"><span class="name">推荐应用</span></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/marketing/creatives/" data-name="market_intelligence_user_acquisition_creative"><span class="name">广告素材</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/marketing/advertisers/" data-name="market_intelligence_user_acquisition_advertisers"><span class="name">广告App</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/marketing/ad-monetization/" data-name="market_intelligence_user_acquisition_publishers"><span class="name">广告变现</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                                    <li><a class="secondary-item" href="/intelligence/marketing/ad-platforms/" data-name="market_intelligence_user_acquisition_ad_platofrom_overview"><span class="name">广告平台</span><i class="aaicon-aa-lock badge-lock"></i></a></li>
                                
                            
                        </ul>
                    </div>
                
            </div>

            <div class="min-menu">
                <div class="section logo-section">
                    <a href="/dashboard/home/" class="brand"><div class="logo-cycle non-int"><div class="min-aa-logo"></div></div></a>
                </div>
            </div>
        </div>

    </div>
</nav>


    </div>
    


  <div id="sub-container">
      
           

<div class="header-v2">
    <div class="navbar">
        <ul class="main-nav">
            <li class="nav-item">
                <div class="search-box-wrap">
                    <form action="/search/" name="search" class="ng-pristine ng-valid">
                        <div class="search-box ">
                            <input name="q" class="search-box-input" maxlength="100" placeholder="搜索" autocomplete="off" spellcheck="false" required="">
                            <span class="search-icon"><i class="icon-search fa fa-search"></i></span>
                            <div class="filter-dropdown">
                                <button class="btn-filter dropdown-toggle" type="button" data-toggle="dropdown"><span class="filter-name">所有</span><span class="caret"></span></button>
                                <div class="dropdown-menu">
                                <a class="dropdown-item current" data-value="all">所有</a>
                                <a class="dropdown-item" data-value="product">应用</a>
                                <a class="dropdown-item" data-value="company">公司</a>
                                <a class="dropdown-item" data-value="sdk">SDK</a>
                                <a class="dropdown-item" data-value="domain">网站</a>
                            </div>
                            </div>
                        </div>
                    </form>
                </div>
            </li>
        </ul>
        <div ng-controller="SaveReportCtrl" class="ng-scope"><!-- ngIf: isDisplayed() --></div>
        <ul class="right-nav">
            <li class="nav-item nav-item-learn">
                <a class="nav-link">
                    <i class="hi hi-learn"></i>

                    <span class="nav-link-text">资源</span>
                    <i class="fa fa-caret-down"></i>
                </a>
                
                    
<ul class="popup-menu popup-menu-learn">
    <li class="primary-title">
        <div>Market Intelligence</div>
    </li>
    

    
    <li class="primary-item-text">
        告别臆测，借助应用市场数据发掘新商机。
    </li>
    <li class="primary-item market">
        <a href="/tours/enterprise-market-data/" target="_blank">
            <span class="primary-info">了解更多</span>
            <i class="secondary-info aa-link-icon fa fa-external-link"></i>
        </a>
    </li>
    

    <li class="spacer-line"></li>
    <li class="primary-title">
        App Annie Connect
    </li>
    <li class="primary-item analytics">
        <a href="/explore/analytics">
            <span class="primary-info">向导演示</span>
        </a>
    </li>
    <li class="primary-item analytics">
        <a href="https://support.appannie.com/hc/en-us" target="_blank">
            <span class="primary-info">搜索知识库</span>
            <i class="secondary-info aa-link-icon fa fa-external-link"></i>
        </a>
    </li>
    <li class="primary-item analytics">
        <a href="https://www.appannie.com/support/requests" target="_blank">
            <span class="primary-info">联系我们的支持团队</span>
            <i class="secondary-info aa-link-icon fa fa-external-link"></i>
        </a>
    </li>
    <li class="primary-item analytics">
        <a href="/account/api/key/">
            <span class="primary-info">API - 批量访问您的应用数据</span>
        </a>
    </li>
    <li class="spacer-line"></li>
    <li class="primary-title">
        了解该产业
    </li>
    <li class="primary-item">
        <a href="/academy/" target="_blank">
            <span class="primary-info">Academy</span>
            <div class="secondary-info"><i class="aa-link-icon fa fa-external-link"></i><em class="badge badge-aa-new">NEW</em></div>
        </a>
    </li>
    <li class="primary-item know-the-industry">
        <a href="/insights/" target="_blank">
            <span class="primary-info">浏览行业报告</span>
            <i class="secondary-info aa-link-icon fa fa-external-link"></i>
        </a>
    </li>
    <li class="primary-item know-the-industry">
        <a href="/about" target="_blank">
            <span class="primary-info">了解App Annie</span>
            <i class="secondary-info aa-link-icon fa fa-external-link"></i>
        </a>
    </li>
</ul>

                
            </li>

            <li class="nav-item dropdown disabled nav-item-user-prefs">
                <a href="javascript:void(0)" class="aa-user-prefs-toggle dropdown-toggle disabled nav-link" data-toggle="dropdown" role="button" aria-expanded="false">



                    
                        <i class="hi hi-user-free"></i>
                    
                    <span class="nav-link-text">
                        <div class="user-display-name">Xia Weiliang</div>
                        <div class="user-email">583551648@qq.com</div>
                    </span>
                    <i class="fa fa-caret-down"></i>
                </a>
                <ul class="popup-menu" role="menu">
                    

    <li class="primary-title">
        App Annie Connect
    </li>
    
        <li class="primary-item">
            <a href="/account/list/">
                <span class="primary-info">
                    我的App连接
                </span>
                
            </a>
        </li>
    
        <li class="primary-item">
            <a href="/account/apps/">
                <span class="primary-info">
                    我的应用
                </span>
                
            </a>
        </li>
    
        <li class="primary-item">
            <a href="/account/sharing/">
                <span class="primary-info">
                    分享
                </span>
                
            </a>
        </li>
    
        <li class="primary-item">
            <a href="/account/export/">
                <span class="primary-info">
                    备份数据
                </span>
                
            </a>
        </li>
    
    <li class="spacer-line"></li>

    <li class="primary-title">
        App Annie 账号
    </li>
    
        <li class="primary-item">
            <a href="/account/keywords/management/">
                <span class="primary-info">
                    关键词管理
                </span>
                
            </a>
        </li>
    
        <li class="primary-item">
            <a href="/account/teams/">
                <span class="primary-info">
                    团队
                </span>
                
            </a>
        </li>
    
        <li class="primary-item">
            <a href="/account/settings/">
                <span class="primary-info">
                    用户设置
                </span>
                
            </a>
        </li>
    
        <li class="primary-item">
            <a href="/account/services/">
                <span class="primary-info">
                    已连接的服务
                </span>
                
            </a>
        </li>
    
        <li class="primary-item">
            <a href="/account/api/key/">
                <span class="primary-info">
                    API 密钥
                </span>
                
            </a>
        </li>
    
    <li class="spacer-line"></li>


                    <li class="primary-item logout"><a href="/account/logout/">退出</a></li>
                </ul>
            </li>
            
            <li class="nav-item">
                <paywall-trigger link="/landing/premium-upgrade" class="ng-isolate-scope"><!-- ngIf: !$ctrl.isToBeInvitedUser --><a href="/landing/premium-upgrade" target="_blank" ng-if="!$ctrl.isToBeInvitedUser" class="ng-scope">
    <ng-transclude>
                    <span class="header-btn btn-action btn-action-primary btn-action-mini ng-scope" title="升级至 Intelligence">
                        升级
                    </span>
                </ng-transclude></a><!-- end ngIf: !$ctrl.isToBeInvitedUser -->
<!-- ngIf: $ctrl.isToBeInvitedUser -->

</paywall-trigger>
            </li>
            

        </ul>
    </div>
</div>


 
      

  

    <div class="main storestats_wrapper page_app-reviews">
    
    
<div class="aa-top-banner breadcrumb-nav">
    <div class="inner">
        <div class="top-banner-content">
            <div class="bnav ng-scope" ng-controller="breadNavCtrl">
                <bread-navs data="nav_dna_info" class="ng-isolate-scope"><div class="menu-dropdown">
    <ul class="item-list">
        <!-- ngRepeat: nav in navs track by $index --><li id="1000200000064254" class="item nav-item company ng-scope active" ng-class="{'active': index === '0'}" ng-mouseenter="displaySubmenu($event)" ng-mouseleave="hiddenSubmenu($event)" ng-mousedown="clickSubmenu($event)">
    <!-- ngIf: !$parent.$last --><a class="link ng-scope ng-isolate-scope" ng-if="!$parent.$last" remember="/company/1000200000064254/reviews/">
            <i class="avatar aaicon-company-o" ng-class="nav.is_parent ? 'aaicon-parent-company-o' : 'aaicon-company-o'"></i>
            <div class="title ng-binding">DH Games</div>
            <!-- ngIf: !helper.isDead(nav) --><i class="fa fa-caret-down action ng-scope" ng-if="!helper.isDead(nav)"></i><!-- end ngIf: !helper.isDead(nav) -->
    </a><!-- end ngIf: !$parent.$last -->

    <!-- ngIf: $parent.$last -->

    <!-- ngIf: !helper.isDead(nav) --><dropdown-submenu class="dropdown-container obj-selector-container ng-scope ng-isolate-scope ng-hide" ng-show="show" ng-if="!helper.isDead(nav)" type="objSelector" query-obj="helper.getQueryObj(nav)">
    <div class="submenu obj-selector-menu ng-scope" ng-class="{'loading': isLoading}" style="">
    <div class="help-section">
        <div class="section-btn invisible" ng-click="prevSection($event)">
            <i class="fa fa-chevron-up"></i>
        </div>
        <div class="section-btn invisible" ng-click="nextSection($event)">
            <i class="fa fa-chevron-down"></i>
        </div>
    </div>

    <ul class="item-list">
        <li class="item head ng-isolate-scope" menu-item="" type="text" value="{linkId: dataSet.data.objSubsidiaries[0].id, name: dataSet.data.objSubsidiaries.length === 1 ? '公司': '公司'}"><!-- ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' --><div class="text ng-binding ng-scope" ng-if="type === 'text'" company-id="1000200000064254">
    公司
</div><!-- end ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li>

        <!-- ngRepeat: item in dataSet.data.objSubsidiaries --><li class="item company-section ng-scope ng-isolate-scope" ng-repeat="item in dataSet.data.objSubsidiaries" menu-item="" type="company" value="{ url: item.url, name: item.name }" options="{isParent: $first &amp;&amp; dataSet.data.objSubsidiaries.length != 1}" ng-attr-title="{{ $first ? item.name : tooltip({ type: 'company', companyName: item.name, parentCompanyName: dataSet.data.objSubsidiaries[0].name}) }}" ng-class="{'related': item.is_related, 'current': item.is_current, 'no-link': item.is_current, 'indent': !$first }" title="DH Games" style=""><!-- ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' --><a class="company ng-scope ng-isolate-scope" ng-if="type === 'company'" remember="/company/1000200000064254/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="">
    <div class="info">
        <i class="avatar aaicon-company-o" ng-class="options.isParent ? 'aaicon-parent-company-o' : 'aaicon-company-o'"></i>
        <div class="title ng-binding">DH Games</div>
    </div>
</a><!-- end ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objSubsidiaries -->

        <!-- ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope sep head" ng-repeat="item in dataSet.data.objApps" menu-item="" type="text" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="DH Games 的产品" style=""><!-- ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' --><div class="text ng-binding ng-scope" ng-if="type === 'text'" company-id="1000200000064254-app">
    DH Games 的产品
</div><!-- end ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="Avenger Legends" style=""><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600006984035/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600006984035/4EMzGixNBovtRa6to8AUzBkXD4z3A4Wt5keEDP4kj-cOAqdJFqz4tKwtqEQFsrt8DVOn=w300" ng-class="value.market">
        <div class="title ng-binding">Avenger Legends</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="Dungeon Rush"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600004439163/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600004439163/WnFPrDWCyyd_4Z4EDESaGcXZ1UHycw15UwtgXcgOGwyftbrrmbCmgDiWrKst5TqTOxx1=w300" ng-class="value.market">
        <div class="title ng-binding">Dungeon Rush</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="Dungeon Rush: Evolved"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600004987647/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600004987647/5t2LEsPnrgH1TWycScJf5zYcyKOXLdPtK8MIiiM_NJoIYwPh-eXHZjvN-IPC3MiH_55f=w300" ng-class="value.market">
        <div class="title ng-binding">Dungeon Rush: Evolved</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="Elite Heroes GToken"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/ios/app/977114553/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="itc">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload itc" data-src="https://static-s.aa-cdn.net/img/ios/977114553/3eb97426f10eefb08d3b3642718c9d88" ng-class="value.market">
        <div class="title ng-binding">Elite Heroes GToken</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">iOS</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope related indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="unified" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" style=""><!-- ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' --><a class="unified ng-scope ng-isolate-scope" ng-class="{ 'with-company': options.hasCompany }" ng-if="type === 'unified'" remember="/apps/all-stores/app/1000600000552041/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="">
    <div class="info">
        <img class="icon lazyload" data-src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a">
        <div class="title ng-binding">Idle Heroes</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasCompany -->
    </div>
    <!-- ngIf: options.hasCaret --><span class="caret-indicator ng-scope" ng-if="options.hasCaret"><i class="fa fa-caret-right"></i></span><!-- end ngIf: options.hasCaret -->
</a><!-- end ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="Piggy Bank Hero"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/ios/app/1020618249/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="itc">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload itc" data-src="https://static-s.aa-cdn.net/img/ios/1020618249/8fecea8f5461db310b8feb796902dd91" ng-class="value.market">
        <div class="title ng-binding">Piggy Bank Hero</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">iOS</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="Take me Home Lite"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/ios/app/466780103/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="itc">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload itc" data-src="https://static-s.aa-cdn.net/img/ios/466780103/aaae648c242971e14bda4c1ed60d40dc" ng-class="value.market">
        <div class="title ng-binding">Take me Home Lite</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">iOS</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="别动我的宝石"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600004649017/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600004649017/gbbi165MU1P_APndpjaFvEpk_4IWJgjcqm54XY2DIwPR9DK1KICbdowMtyT43R5foQ=s300" ng-class="value.market">
        <div class="title ng-binding">别动我的宝石</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="城堡突袭2"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600004689958/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600004689958/2uArwgK7Tdb0zWZQI0xKrQQNbTexlE7RndVEhOS2M07Ry6RGIRGxypsIyw8QXTfk5Q=s300" ng-class="value.market">
        <div class="title ng-binding">城堡突袭2</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="战神传说"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600004877345/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600004877345/aJyckXsQ_ysZ0OZIDTK1-snWkrO4h67EK_Y8nyd7l24YvOWMAhNVnIBBa5krddvsEg=w300" ng-class="value.market">
        <div class="title ng-binding">战神传说</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="星河防线（英文版）"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600001529607/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600001529607/hP-R-qihKFCfImDaBFiKAVabPnIJVliSoCOgOWW1aDApwNp1pJfuaz0S8AeIUzeHjJgz=w300" ng-class="value.market">
        <div class="title ng-binding">星河防线（英文版）</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="玩具塔防: 恐怖乐园"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600006908033/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600006908033/x3XkgIDAM-NtuaGAg-PEBGvrSredRPhfwegu7ys3cm8cZef4xQr7E9QwJf4XyT2PuA=s300" ng-class="value.market">
        <div class="title ng-binding">玩具塔防: 恐怖乐园</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">Google Play</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="连连看对战"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/ios/app/548909890/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="itc">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload itc" data-src="https://static-s.aa-cdn.net/img/ios/548909890/b68fbb660c760b5ad58f5e8f89aaa896" ng-class="value.market">
        <div class="title ng-binding">连连看对战</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">iOS</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps --><li class="item ng-scope ng-isolate-scope indent" ng-repeat="item in dataSet.data.objApps" menu-item="" type="app" value="{ linkId: item.linkId, url: item.url, stores: item.stores, icon: item.icon, name: item.name, allAppCount: item.app_num, appCount: item.own_num, market: item.market_cssid, marketName: item.market_fullname, companyName: item.type === 'partnership'? item.primaryCompanyName : item.parentCompanyName}" options="{ hasAllAppCount: item.type === 'partnership' || item.type === 'joint', hasPrice: false, hasMarketIcon: false, hasMarketName: true, hasCompany: item.type === 'partnership' || item.type === 'joint', hasCaret: item.menuItemType === 'unified' }" ng-class="{'sep': item.menuItemType === 'text', 'current': item.is_current || isCurrentItem(item.id), 'no-link': item.is_current, 'related': item.is_related, 'head': item.menuItemType === 'text', 'indent': item.menuItemType !== 'text'}" ng-attr-title="{{ item.menuItemType !== 'unified' ? tooltip({type: item.type, name: item.name, companyName: item.companyName, allAppCount: item.app_num, appCount: item.own_num, parentCompanyName: item.parentCompanyName, primaryCompanyName: item.primaryCompanyName }) : undefined }}" ng-mouseenter="item.menuItemType === 'unified' &amp;&amp; selectCurrentItem($event, item.id, item.app_num)" ng-mouseleave="item.menuItemType === 'unified' &amp;&amp; unSelectCurrentItem($event, item.id)" title="龙域守卫: 地下城 Lair Defense"><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/ios/app/517684333/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="itc">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload itc" data-src="https://static-s.aa-cdn.net/img/ios/517684333/4a7c176030ef4ce78385cdb1be535125" ng-class="value.market">
        <div class="title ng-binding">龙域守卫: 地下城 Lair Defense</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName --><span ng-if="options.hasMarketName" class="ng-binding ng-scope">iOS</span><!-- end ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</li><!-- end ngRepeat: item in dataSet.data.objApps -->

        <li class="item last-section" company-id="1000200000064254-bottom"></li>

        <!-- ngIf: dataSet.hasMore -->
    </ul>
    <!-- ngIf: isLoading -->
</div>

<!-- ngRepeat: item in unifiedList --></dropdown-submenu><!-- end ngIf: !helper.isDead(nav) -->
</li><!-- end ngRepeat: nav in navs track by $index --><!-- ngIf: nav.page_type === 'universal_product' -->

<!-- ngIf: nav.page_type !== 'universal_product' --><li class="item nav-item ng-scope" ng-class="{'active': index === '0'}" ng-if="nav.page_type !== 'universal_product'">
    <a class="link ng-isolate-scope" remember="/apps/all-stores/app/1000600000552041/reviews/">
            <!-- ngIf: nav.icon --><img class="icon ng-scope" ng-src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a" ng-if="nav.icon" src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a"><!-- end ngIf: nav.icon -->
            <div class="title ng-binding">Idle Heroes</div>
    </a>
</li><!-- end ngIf: nav.page_type !== 'universal_product' --><!-- end ngRepeat: nav in navs track by $index --><!-- ngIf: appInUA(nav) --><li class="item nav-item ng-scope" ng-class="{'active': index === '0'}" ng-if="appInUA(nav)" ng-mouseenter="displaySubmenu($event)" ng-mouseleave="hiddenSubmenu($event)" ng-mousedown="clickSubmenu($event)">
    <span class="no-link">
        <!-- ngIf: nav.market --><span class="store ng-scope" ng-if="nav.market">
            <i class="aa-icon itc market"></i>
        </span><!-- end ngIf: nav.market -->
        <!-- ngIf: nav.icon --><img class="icon app-avatar size-22 ng-scope ios" ng-src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a" ng-if="nav.icon" ng-class="nav.market" src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a"><!-- end ngIf: nav.icon -->
        <div class="title ng-binding" ng-class="{'dead': helper.isDead(nav)}">放置奇兵 -全球同服放置类游戏</div>
        <!-- ngIf: nav.ua_edition_count > 1 --><i class="fa fa-caret-down action ng-scope" ng-if="nav.ua_edition_count > 1"></i><!-- end ngIf: nav.ua_edition_count > 1 -->
    </span>
    <!-- ngIf: nav.ua_edition_count > 1 --><dropdown-submenu type="editionApp" ng-if="nav.ua_edition_count > 1" ng-show="show" class="dropdown-container ng-scope ng-isolate-scope ng-hide" query-obj="helper.getQueryObj(nav)">
    <div class="submenu edition-app-menu ng-scope" ng-class="{'loading': isLoading}" style="">
    <div class="item-list">
        <div class="section">
            <div class="section-title">Unified Product</div>
            <div class="item head ng-isolate-scope" ng-class="{'current': queryObj.page_type === 'universal_product', 'no-link': queryObj.page_type === 'universal_product'}" menu-item="" type="link" value="{ url: dataSet.unified_app.url, name: UICOPY.appApps.format(dataSet.unified_app.name), stores: dataSet.unified_app.stores, icon: dataSet.apps[0] ? dataSet.apps[0].icon : ndivl, stackIcon: dataSet.apps[1] ? dataSet.apps[1].icon : null }" options="{hasStores: dataSet.unified_app.stores.length > 0}"><!-- ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' --><a class="link ng-scope ng-isolate-scope" ng-if="type === 'link'" remember="/apps/all-stores/app/1000600000552041/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="">
    <span class="info">
        <!-- ngIf: options.hasStores --><div ng-if="options.hasStores" ng-class="{'no-store': storeNum == 0, 'store': storeNum == 1, 'stores': storeNum > 1 }" ng-init="size = value.stores.length === 1 ? 'size-16' : 'size-10'; storeNum = value.stores.length" class="ng-scope stores" style="">
            <!-- ngRepeat: store in value.stores | limitTo: 4 --><i class="aa-icon ng-scope size-10 itc" ng-class="[size, store]" ng-repeat="store in value.stores | limitTo: 4"></i><!-- end ngRepeat: store in value.stores | limitTo: 4 --><i class="aa-icon ng-scope size-10 gp" ng-class="[size, store]" ng-repeat="store in value.stores | limitTo: 4"></i><!-- end ngRepeat: store in value.stores | limitTo: 4 -->
        </div><!-- end ngIf: options.hasStores -->
        <!-- ngIf: !value.stackIcon && value.icon -->
        <!-- ngIf: value.stackIcon && value.icon --><div class="stack-icon ng-scope" ng-if="value.stackIcon &amp;&amp; value.icon" style="">
            <img class="icon-front img-bg" ng-src="https://static-s.aa-cdn.net/img/gp/20600005832657/m1bGvQ1JMuiYAOMA37H92YOVE3TNU4d8duKLyastAUQq1MvL7yx0YVFKg_Tz32erkw=s300" src="https://static-s.aa-cdn.net/img/gp/20600005832657/m1bGvQ1JMuiYAOMA37H92YOVE3TNU4d8duKLyastAUQq1MvL7yx0YVFKg_Tz32erkw=s300">
            <img class="img-bg" ng-src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a" src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a">
        </div><!-- end ngIf: value.stackIcon && value.icon -->
        <div class="title ng-binding">所有 Idle Heroes 产品</div>
    </span>
</a><!-- end ngIf: type === 'link' -->
</div>
        </div>
        <div class="section">
            <div class="section-title">应用</div>
            <!-- ngRepeat: app in dataSet.apps --><div class="item sub-item ng-scope ng-isolate-scope" ng-repeat="app in dataSet.apps" menu-item="" type="app" value="{ market: app.market_cssid, icon: app.icon, name: app.name, price: app.price, url: app.url }" options="{ hasPrice: app.status !== 'dead' &amp;&amp; app.price, hasMarketIcon: true, hasMarketName: false }" ng-class="{ 'current': app.is_current, 'no-link': app.is_current, 'dead': app.status === 'dead' }" ng-attr-title="{{ app.name }}" title="Idle Heroes" style=""><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/google-play/app/20600005832657/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="gp">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon --><div class="store ng-scope" ng-if="options.hasMarketIcon">
            <i class="aa-icon market gp" ng-class="value.market"></i>
        </div><!-- end ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload gp" data-src="https://static-s.aa-cdn.net/img/gp/20600005832657/m1bGvQ1JMuiYAOMA37H92YOVE3TNU4d8duKLyastAUQq1MvL7yx0YVFKg_Tz32erkw=s300" ng-class="value.market">
        <div class="title ng-binding">Idle Heroes</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</div><!-- end ngRepeat: app in dataSet.apps --><div class="item sub-item ng-scope ng-isolate-scope current no-link" ng-repeat="app in dataSet.apps" menu-item="" type="app" value="{ market: app.market_cssid, icon: app.icon, name: app.name, price: app.price, url: app.url }" options="{ hasPrice: app.status !== 'dead' &amp;&amp; app.price, hasMarketIcon: true, hasMarketName: false }" ng-class="{ 'current': app.is_current, 'no-link': app.is_current, 'dead': app.status === 'dead' }" ng-attr-title="{{ app.name }}" title="放置奇兵 -全球同服放置类游戏" style=""><!-- ngIf: type === 'app' --><a class="app ng-scope ng-isolate-scope" ng-if="type === 'app'" remember="/apps/ios/app/1153461915/reviews/" tracking="" tracking-category="" tracking-action="" tracking-label="" data-market="itc">
    <div class="info">
        <!-- ngIf: options.hasMarketIcon --><div class="store ng-scope" ng-if="options.hasMarketIcon">
            <i class="aa-icon market itc" ng-class="value.market"></i>
        </div><!-- end ngIf: options.hasMarketIcon -->
        <img class="icon app-avatar size-22 lazyload itc" data-src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a" ng-class="value.market">
        <div class="title ng-binding">放置奇兵 -全球同服放置类游戏</div>
    </div>
    <div class="aside">
        <!-- ngIf: options.hasPrice && +value.price > 0 -->
        <!-- ngIf: options.hasMarketName -->
    </div>
</a><!-- end ngIf: type === 'app' -->

<!-- ngIf: type ==='domain' -->

<!-- ngIf: type ==='sdk' -->

<!-- ngIf: type === 'unifiedWithStore' -->

<!-- ngIf: type === 'unified' -->

<!-- ngIf: type === 'publisher' -->

<!-- ngIf: type === 'company' -->

<!-- ngIf: type === 'text' -->

<!-- ngIf: type === 'link' -->
</div><!-- end ngRepeat: app in dataSet.apps -->
        </div>
        <!-- ngIf: dataSet.domains && dataSet.domains.length > 0 -->
    </div>
    <!-- ngIf: isLoading -->
</div></dropdown-submenu><!-- end ngIf: nav.ua_edition_count > 1 -->
</li><!-- end ngIf: appInUA(nav) -->

<!-- ngIf: !appInUA(nav) --><!-- end ngRepeat: nav in navs track by $index -->
    </ul>
</div>
</bread-navs>
            </div>
        </div>
    </div>
</div>


    <div class="inner inner-full" itemscope="" itemtype="http://schema.org/MobileSoftwareApplication">
      

<script>
    var pageVal = pageVal || {};
    pageVal.app_show_mode = 'public'; 
    pageVal.app_market = 'itc';
    pageVal.market_langid = '';
    pageVal.app_device = ''; 
    
        pageVal.obj_nav = {"product": {"is_sensitive": false, "id": 1153461915, "market": "ios", "icon": "https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a", "name": "\u653e\u7f6e\u5947\u5175 -\u5168\u7403\u540c\u670d\u653e\u7f6e\u7c7b\u6e38\u620f", "url": "/apps/ios/app/1153461915/reviews/", "universal_product_id": 1000600000552041, "is_dead": false, "ua_edition_count": 2, "source": null, "page_type": "product", "root": false}, "company": {"name": "DH Games", "has_subsidiary": false, "url": "/company/1000200000064254/reviews/", "is_dead": false, "id": 1000200000064254, "page_type": "product", "root": true, "slug": 1000200000064254}, "universal_product": {"name": "Idle Heroes", "url": "/apps/all-stores/app/1000600000552041/reviews/", "is_sensitive": false, "id": 1000600000552041, "page_type": "product", "root": false, "slug": "idle-heroes", "icon": "https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a"}}
    

    
        pageVal.meta_data = {"status": "Alive", "required_device": "\u901a\u7528", "app_market_cssid": "itc", "name": "\u653e\u7f6e\u5947\u5175 -\u5168\u7403\u540c\u670d\u653e\u7f6e\u7c7b\u6e38\u620f", "allow_add_to_groups": true, "universal_company_info": {}, "price": 0.0, "is_int_user": false, "universal_company_name": "DH Games", "current_url": "/apps/ios/app/idle-heroes/reviews/", "app_market_url": "https://itunes.apple.com/app/id1153461915", "is_show_device": false, "sharing_url": "", "franchise_info": {"count": "0 \u6b3eApp", "is_sensitive": false, "id": "app_franchise", "url": null, "name": "N/A"}, "app_market_name": "iOS Store", "category_name": "\u6e38\u620f", "type": "APP", "id": 1153461915, "market": "ios", "icon": "https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a"}
    
</script>

<!-- app picker -->
<!--  -->
<!-- app picker end -->
<div class="frame frame-app">
    <div class="aa-sidebar aa-sidebar-large">
        <div class="sidebar-inner" style="position: relative; top: 0px; transition-duration: 0.14s; transition-timing-function: ease-out; transition-property: none;">
            
            <span itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">
                <span itemprop="price" content=""></span>
                <span itemprop="seller" itemscope="" itemtype="http://schema.org/Organization">
                  <span itemprop="name" content="iOS Store"></span>
                </span>
            </span>
            <span itemscope="" itemtype="http://schema.org/AggregateRating" itemprop="aggregateRating">
                <span itemprop="ratingValue" content=""></span>
                <span itemprop="ratingCount" content=""></span>
            </span>
            

            
<ul class="menu">
    
        
            <li class="primary-title">
                <div>
                    信息
                </div>
            </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/details/" target="">
                        <span class="primary-info">App详细信息</span>
                        
                        
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/1153461915/sdks/" target="">
                        <span class="primary-info">SDK</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/timeline/" target="">
                        <span class="primary-info">时间线</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
        
        <li class="spacer"></li>
    
        
            <li class="primary-title">
                <div>
                    我的已连接应用
                </div>
            </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/1153461915/analytics/" target="">
                        <span class="primary-info">连接</span>
                        
                        
                        
                        
                            <i class="right-icon aaicon-aa-connections"></i>
                        
                    </a>
                </li>
            
        
        <li class="spacer"></li>
    
        
            <li class="primary-title">
                <div>
                    应用商店排名
                </div>
            </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/app-ranking/" target="">
                        <span class="primary-info">每日排名</span>
                        
                        
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/rank-history/" target="">
                        <span class="primary-info">历史排名</span>
                        
                        
                        
                        
                    </a>
                </li>
            
        
        <li class="spacer"></li>
    
        
            <li class="primary-title">
                <div>
                    下载量和收入
                </div>
            </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/intelligence/" target="">
                        <span class="primary-info">下载量和收入</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
        
        <li class="spacer"></li>
    
        
            <li class="primary-title">
                <div>
                    使用模式和用户参与度
                </div>
            </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/usage/" target="">
                        <span class="primary-info">使用量</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/user-retention/" target="">
                        <span class="primary-info">用户留存率</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/intelligence/cross-app-usage/" target="">
                        <span class="primary-info">跨应用/网页使用情况</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/intelligence/demographics/" target="">
                        <span class="primary-info">用户特征</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
                <li class="primary-item current ">
                    <a href="/apps/ios/app/idle-heroes/reviews/" target="">
                        <span class="primary-info">评价</span>
                        
                        
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/ratings/" target="">
                        <span class="primary-info">评级</span>
                        
                        
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/ratings-over-time/" target="">
                        <span class="primary-info">随时间评级</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
        
        <li class="spacer"></li>
    
        
            <li class="primary-title">
                <div>
                    用户获取
                </div>
            </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/keywords/" target="">
                        <span class="primary-info">关键词 (ASO)</span>
                        
                        
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/featured/" target="">
                        <span class="primary-info">推荐</span>
                        
                        
                        
                        
                    </a>
                </li>
            
                <li class="primary-item  ">
                    <a href="/apps/ios/app/idle-heroes/intelligence/marketing/" target="">
                        <span class="primary-info">广告</span>
                        
                        
                        
                            <i class="right-icon aaicon-aa-lock"></i>
                        
                        
                    </a>
                </li>
            
        
        <li class="spacer"></li>
    
</ul>

            <img class="sidebar-logo" src="https://static-s.aa-cdn.net/media/pictures/logo/sidebar_stencil.v-6b37ae6b.png" alt="AppAnnie.com" width="141" height="97">
        </div>
    </div>

    <div class="content content-app app-reviews">

        <div class="  content-container aa-popup-container">
            
                

                
                

<div class="app-info-top aa-info-columns aa-info-columns-app">
    <div class="app-info-header-section ng-scope" ng-controller="appInfoHeaderCtrl">
    <app-header type="metaData.type" obj="metaData" class="ng-isolate-scope"><div class="app-info-header-container" ng-switch="type">

    <!-- ngSwitchWhen: APP --><div class="app-info-header ng-scope" ng-switch-when="APP">
        <div class="avatar" ng-switch="obj.status">
            <!-- ngSwitchWhen: Dead -->
            <!-- ngSwitchWhen: Collecting -->
            <!-- ngSwitchDefault:  --><img ng-src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a" class="app-avatar size-64 ng-scope itc" ng-class="obj.app_market_cssid" ng-switch-default="" src="https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a"><!-- end ngSwitchWhen:  -->
        </div>
        <!-- ngIf: obj.status !== 'Collecting' --><div class="info ng-scope" ng-if="obj.status !== 'Collecting'">
            <div class="space-between">
                <div class="name ng-binding" ng-attr-title="{{ obj.name }}" title="放置奇兵 -全球同服放置类游戏">放置奇兵 -全球同服放置类游戏</div>
                <div class="buttons-container">
                    <alert-btn class="buttons-container__button ng-isolate-scope" params="{productId: obj.id, market: obj.market}"><!-- ngIf: !$ctrl.isLocked -->
<!-- ngIf: $ctrl.isLocked --><a class="btn-action btn-action-mini btn-action-secondary save--locked ng-scope" ng-click="$ctrl.showModal()" ng-if="$ctrl.isLocked"><span>创建提醒</span><i class="aaicon-aa-lock"></i></a><!-- end ngIf: $ctrl.isLocked -->
</alert-btn>
                    <!-- ngIf: obj.allow_add_to_groups && (obj.app_market_cssid === 'itc' || obj.app_market_cssid === 'gp') --><add-to-groups-button class="buttons-container__button ng-scope ng-isolate-scope" obj="{market: obj.app_market_name, id: obj.id}" ng-if="obj.allow_add_to_groups &amp;&amp; (obj.app_market_cssid === 'itc' || obj.app_market_cssid === 'gp')"><!-- ngIf: isVisible -->
</add-to-groups-button><!-- end ngIf: obj.allow_add_to_groups && (obj.app_market_cssid === 'itc' || obj.app_market_cssid === 'gp') -->
                </div>
            </div>
            <app-group-dialog></app-group-dialog>
            <div class="space-between wrap">
                <div class="data-section">
                    <!-- ngIf: obj.app_market_fullname -->
                    <span class="item ng-binding">免费</span>
                    <!-- ngIf: obj.category_name --><span class="item ng-scope" ng-if="obj.category_name">
                        <span data-helptip=" 应用分类。这是由发行商选择的应用商店中的类别。 该应用将会显示在相应类别的热门排行榜中。" class="ng-binding">
                            游戏
                        </span>
                    </span><!-- end ngIf: obj.category_name -->
                    <!-- ngIf: obj.app_note -->
                    <!-- ngIf: obj.is_show_device -->
                    <!-- ngIf: hasCompany() -->
                    <span class="item status ng-binding"></span>
                </div>
                <div class="link-section">
                    <!-- ngIf: obj.sharing_url -->
                    <!-- ngIf: obj.franchise_info.url && obj.status === 'Alive' -->
                    <!-- ngIf: obj.app_market_url && !isDead() --><a class="item link ng-binding ng-scope" ng-if="obj.app_market_url &amp;&amp; !isDead()" ng-attr-title="{{ obj.app_market_name }}" target="_blank" app-confirm="https://itunes.apple.com/app/id1153461915" title="iOS Store">在iOS Store中打开<i class="fa fa-external-link"></i></a><!-- end ngIf: obj.app_market_url && !isDead() -->
                </div>
            </div>
        </div><!-- end ngIf: obj.status !== 'Collecting' -->
        <!-- ngIf: obj.status === 'Collecting' -->
    </div><!-- end ngSwitchWhen:  -->

    <!-- ngSwitchWhen: BUNDLE_APP -->

    <!-- ngSwitchWhen: UNIFIED_APP -->

    <!-- ngSwitchWhen: PUBLISHER -->

    <!-- ngSwitchWhen: COMPANY -->

    <!-- ngSwitchWhen: APP_FRANCHISE -->
</div>
</app-header>
</div>

</div>

                <div class="main-app-content">
                

                

    <div ng-controller="AppReviewsCtrl" class="ng-scope">
        <!-- ngInclude: maintpl --><div ng-include="maintpl" class="ng-scope" style=""><div class="aa-dashboard-container ng-scope">
    <div class="dashboard-meta">
        <div class="dashboard-header clearfix">
            <h1 class="dashboard-header__title pull-left">
              评价
              <a target="_blank" href="http://support.appannie.com/entries/49761574-How-to-use-the-Reviews-Ratings-Report-">
                关于该报告
              </a>
            </h1>
            <div class="dashboard-header__actions pull-right">
                <save-report-btn class="ng-isolate-scope"><!-- ngIf: !$ctrl.isLocked -->
<!-- ngIf: $ctrl.isLocked --><a class="btn-action btn-action-mini btn-action-secondary save--locked ng-scope" ng-click="$ctrl.showModal()" ng-if="$ctrl.isLocked"><span>保存</span><i class="aaicon-aa-lock"></i></a><!-- end ngIf: $ctrl.isLocked -->
</save-report-btn>
                <send-report report-info="评价" class="ng-isolate-scope"><!-- ngIf: !$ctrl.isLocked -->
<!-- ngIf: $ctrl.isLocked --><a class="btn-action btn-action-mini btn-action-secondary save--locked ng-scope" ng-click="$ctrl.showModal()" ng-if="$ctrl.isLocked"><span>订阅&amp;分享</span><i class="aaicon-aa-lock"></i></a><!-- end ngIf: $ctrl.isLocked -->
</send-report>
                <export-report class="ng-isolate-scope"><!-- ngIf: !$ctrl.isLocked && $ctrl.isDisabled --><!-- ngIf: $ctrl.isLocked --><a class="btn-action btn-action-mini btn-action-secondary export--locked ng-scope" ng-if="$ctrl.isLocked" ng-click="$ctrl.paywallDialog()">
    <span>导出</span>
    <i class="aaicon-aa-lock"></i>
</a><!-- end ngIf: $ctrl.isLocked --><!-- ngIf: !$ctrl.isLocked && !$ctrl.isDisabled -->
</export-report>
                <span class="date-range-check-pop-up" review-count-and-date-range-check=""></span>
            </div>
        </div>

        <div class="filter-container clearfix">
            <div ng-show="market !== 'kindle-store'" class="filter-item ng-isolate-scope" control-filter="list-picker" data-title="版本" data-icon="fa fa-code-fork" aa-filter="filter.version"><a class="current">所有版本</a><a class="more"><i class="fa fa-caret-down"></i></a><a class="title"><span class="fa fa-code-fork"></span><span class="filter-name">版本</span></a></div>

            <div ng-show="market !== 'google-play'" class="filter-item ng-isolate-scope" control-filter="tab-picker" data-title="国家/地区" data-icon="fa fa-globe" aa-filter="filter.country"><a class="current">全部</a><a class="more"><i class="fa fa-caret-down"></i></a><a class="title"><span class="fa fa-globe"></span><span class="filter-name">国家/地区</span></a></div>

            <div ng-show="market === 'google-play'" class="filter-item item-languages ng-isolate-scope ng-hide" control-filter="list-picker" data-title="语言" data-icon="fa fa-globe" aa-filter="filter.language">
            </div>

            <div class="filter-item ng-isolate-scope" control-filter="list-picker" data-title="评级" data-icon="fa fa-star-half-empty" aa-filter="filter.rating"><a class="current">所有评级</a><a class="more"><i class="fa fa-caret-down"></i></a><a class="title"><span class="fa fa-star-half-empty"></span><span class="filter-name">评级</span></a></div>

            <div class="filter-item review-search-wrapper">
                <div class="aa-search-box inline-block ng-isolate-scope" aa-search-box="search" aa-search-box-max-length="25" aa-search-box-placeholder="查看搜索" aa-search-box-search-by-fe="true" aa-search-box-on-search="filter.search.value = search">    <i class="fa fa-search"></i>
    <input class="item-filter" type="text" placeholder="查看搜索" value="" maxlength="25">
    <i class="ui-icon clear-button btn-clear" style="display: none;"></i>


</div>
            </div>

            <div class="filter-item date pull-right ng-isolate-scope" control-filter="date_range_picker" data-title="时间段" data-icon="fa fa-calendar" aa-filter="filter.date"><a class="current"><span class="start_date">2019年4月29日</span> - <span class="end_date">2019年5月29日</span></a><a class="more"><i class=" fa fa-caret-down"></i></a><a class="title"><span class="fa fa-calendar"></span><span class="filter-name">时间段</span></a></div>
        </div>

        <div class="dashboard-meta-sub">
            <h3 aa-bind-html="resultTitle" class="dashboard-sub-header ng-binding">所有版本 - 全部 - 所有评级 - 2019年4月29日 - 2019年5月29日</h3>
        </div>
    </div>

    <!-- ngIf: !anonymous --><div ng-if="!anonymous" class="dashboard-view-container ng-scope">
        <!-- ngInclude: 'app/tpl/ng_app_review_chart.tpl' --><div ng-include="'app/tpl/ng_app_review_chart.tpl'" class="ng-scope"><div ng-controller="AppReviewsChartCtrl" class="ng-scope">
    <div aa-loading="status === 'loading'" class="ng-isolate-scope"><!-- ngIf: loading() --></div>
    <div aa-show="status === 'fail'" class="ng-hide">
        加载表格数据失败
    </div>
    <historical-data-limit-alert aa-show="exceedDateLimit" to-be-invited="isToBeInvitedUser" class="ng-isolate-scope ng-hide"><!-- ngIf: !toBeInvited --><div ng-if="!toBeInvited" class="alert alert-warning ng-scope">
   您的账户可以访问最近90天的历史数据。使用App Annie Connect<a href="/account/list/#!/choose-store/" target="_blank">连接一个账户</a>来免费访问您已连接的应用。或者，您可以升级至高级<a href="/landing/premium-upgrade" target="_blank">App Annie Intelligence订阅</a>，以获取完整访问权限。
</div><!-- end ngIf: !toBeInvited -->

<!-- ngIf: toBeInvited -->
</historical-data-limit-alert>
    <div aa-show="status !== 'loading' &amp;&amp; status != 'fail'" class="">
        <div class="chart-container">
            <div class="left-chart-container">
                <div class="row-control-group aa-chart-options">
                    <div class="right-align-controls" style="padding-bottom: 10px;">
                        <span class="btn-group">
                            <!-- ngRepeat: item in granularities --><a class="btn btn-mini ng-binding ng-scope" ng-repeat="item in granularities" ng-class="{active: meta.granularity === item.key}" ng-click="clickGranularity(item.key)">天</a><!-- end ngRepeat: item in granularities --><a class="btn btn-mini ng-binding ng-scope active" ng-repeat="item in granularities" ng-class="{active: meta.granularity === item.key}" ng-click="clickGranularity(item.key)">周</a><!-- end ngRepeat: item in granularities --><a class="btn btn-mini ng-binding ng-scope" ng-repeat="item in granularities" ng-class="{active: meta.granularity === item.key}" ng-click="clickGranularity(item.key)">月</a><!-- end ngRepeat: item in granularities --><a class="btn btn-mini ng-binding ng-scope" ng-repeat="item in granularities" ng-class="{active: meta.granularity === item.key}" ng-click="clickGranularity(item.key)">年</a><!-- end ngRepeat: item in granularities -->
                        </span>
                    </div>
                </div>

                <div class="aa-line-sep-a"></div>

                <div aa-loading="chart_status === 'loading'" class="ng-isolate-scope"><!-- ngIf: loading() --></div>
                <div aa-show="chart_status === 'fail'" class="ng-hide">
                    加载表格数据失败
                </div>

                <div aa-chart="data" aa-chart-stack="meta.stack" aa-chart-percent="meta.percent" aa-chart-visible-series="meta.series" aa-chart-options="chartOptions" aa-show="chart_status !== 'loading' &amp;&amp; chart_status != 'fail'" class="ng-isolate-scope"><div class="inject-chart"><div class="aa-chart-toolbar"><span class="chart-zoomer"><span class="chart-btn hc-reset-btn"><span class="btn btn-mini disabled" title="重置"><i class="fa fa-undo"></i></span></span><span class="chart-btn hc-zoom-btn"><span class="btn btn-mini" title="Zoom"><i class="fa fa-search-plus"></i></span></span></span><span class="aa-chart-switch ng-scope"><!-- ngIf: type.custom -->
<!-- ngIf: stack.custom --><span ng-if="stack.custom" class="ng-scope" style="">
    <span class="chart-series-switch" aa-checkbox="stack.value" on-checkbox-change="clickStack()"><i class="ui-icon tcheckbox checkall"></i>
        <label>堆积</label>
    </span>
</span><!-- end ngIf: stack.custom -->
<!-- ngIf: percent.custom --><span ng-if="percent.custom" class="ng-scope">
    <span class="chart-series-switch" aa-checkbox="percent.value" on-checkbox-change="clickPercent()"><i class="ui-icon tcheckbox"></i>
        <label>百分比</label>
    </span>
</span><!-- end ngIf: percent.custom -->
</span></div><div class="chart-render" data-highcharts-chart="0"><div class="highcharts-container" id="highcharts-0" style="position: relative; overflow: hidden; width: 686px; height: 205px; text-align: left; line-height: normal; z-index: 0; font-family: inherit;"><svg version="1.1" style="font-family:inherit;font-size:12px;" xmlns="http://www.w3.org/2000/svg" width="686" height="205"><desc>Created with Highcharts 4.2.7</desc><defs><clipPath id="highcharts-1"><rect x="0" y="0" width="630" height="159"></rect></clipPath></defs><rect x="0" y="0" width="686" height="205" fill="#FFFFFF" class=" highcharts-background"></rect><image preserveAspectRatio="none" x="54" y="16" width="120" height="40" NS1:href="data:image/svg+xml;charset=utf8,%3Csvg%20width%3D%22355px%22%20height%3D%22111px%22%20viewBox%3D%220%200%20355%20111%22%20version%3D%221.1%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20xmlns%3Axlink%3D%22http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink%22%3E%0A%20%20%20%20%3Ctitle%3Eannie-solid-logo%3C%2Ftitle%3E%0A%20%20%20%20%3Cdefs%3E%3C%2Fdefs%3E%0A%20%20%20%20%3Cg%20id%3D%22Page-1%22%20stroke%3D%22none%22%20stroke-width%3D%221%22%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%20opacity%3D%220.99000001%22%3E%0A%20%20%20%20%20%20%20%20%3Cg%20id%3D%22annie-logo%22%20fill%3D%22%2322323F%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cpath%20d%3D%22M190.825%2C45.885%20C189.491%2C44.27%20183.679%2C45.281%20180.933%2C45.516%20C179.381%2C45.638%20177.365%2C45.887%20175.091%2C46.34%20C181.779%2C30.356%20188.639%2C20.146%20193.385%2C13.822%20C193.385%2C13.822%20191.306%2C33.953%20190.825%2C45.885%20Z%20M204.693%2C3.954%20C204.693%2C1.361%20197.776%2C0.617%20195.837%2C0.617%20C192.7%2C0.617%20184.169%2C10.8%20178.443%2C19.948%20C173.264%2C28.22%20168.28%2C38.26%20163.856%2C48.865%20C160.16%2C49.933%20157.055%2C51.007%20155.863%2C51.971%20C154.184%2C53.284%20156.703%2C58.73%20159.566%2C58.965%20C155.519%2C70.416%20152.992%2C79.326%20152.2%2C87.258%20C152.142%2C87.832%20152.459%2C88.381%20152.991%2C88.606%20C155.521%2C89.674%20162.516%2C90.578%20162.927%2C87.646%20C164.826%2C74.391%20167.32%2C67.221%20171.028%2C56.45%20C177.116%2C55.269%20184.406%2C54.068%20190.498%2C53.824%20C190.245%2C60.162%20190.131%2C83.539%20191.312%2C86.751%20C192.102%2C88.898%20201.391%2C90.499%20201.391%2C88.113%20C201.391%2C83.299%20200.298%2C66.012%20200.621%2C46.763%20C201.001%2C24.125%20204.693%2C6.312%20204.693%2C3.954%20L204.693%2C3.954%20Z%22%20id%3D%22Fill-1%22%3E%3C%2Fpath%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cpath%20d%3D%22M312.32%2C18.995%20C318.26%2C18.995%20320.242%2C13.431%20320.242%2C10.414%20C320.242%2C7.854%20318.281%2C3.542%20314.293%2C3.542%20C309.568%2C3.542%20308.352%2C10.414%20308.352%2C13.055%20C308.352%2C17.293%20310.807%2C18.995%20312.32%2C18.995%22%20id%3D%22Fill-2%22%3E%3C%2Fpath%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cpath%20d%3D%22M339.64%2C32.744%20C347.002%2C32.744%20345.612%2C55.479%20329.346%2C55.479%20C329.179%2C55.479%20328.894%2C55.496%20328.543%2C55.527%20C330.596%2C43.8%20335.147%2C32.744%20339.64%2C32.744%20Z%20M348.502%2C69.445%20C346.545%2C73.506%20342.628%2C82.87%20334.828%2C82.87%20C328.58%2C82.87%20326.815%2C73.669%20327.587%2C63.152%20C328.044%2C63.199%20328.449%2C63.224%20328.74%2C63.224%20C356.292%2C63.224%20359.705%2C26.027%20338.711%2C26.027%20C324.506%2C26.027%20313.945%2C57.455%20318.851%2C76.412%20C317.254%2C79.327%20314.517%2C82.985%20311.912%2C82.985%20C309.99%2C82.985%20308.317%2C80.11%20308.317%2C75.685%20C308.194%2C66.371%20311.277%2C43.204%20314.854%2C30.061%20C315.939%2C26.017%20306.261%2C25.659%20306.493%2C25.659%20C305.655%2C25.659%20304.713%2C25.879%20304.354%2C27.193%20C302.112%2C35.193%20298.464%2C59.364%20298.464%2C72.637%20C298.464%2C73.641%20298.488%2C74.585%20298.531%2C75.484%20C297.288%2C77.74%20296.304%2C79.707%20294.127%2C79.707%20C283.99%2C79.707%20292.659%2C46.356%20292.659%2C30.794%20C292.659%2C26.959%20287.516%2C24.843%20284.28%2C24.843%20C276.653%2C24.843%20265.257%2C49.719%20262.029%2C61.744%20C262.029%2C61.744%20264.905%2C39.214%20266.325%2C27.737%20C266.692%2C24.767%20259.189%2C24.713%20257.759%2C24.713%20C255.2%2C24.713%20253.081%2C55.44%20252.381%2C75.817%20C251.272%2C77.832%20250.278%2C79.489%20248.281%2C79.489%20C244.937%2C79.489%20243.388%2C76.516%20243.388%2C70.418%20C243.388%2C49.984%20246.813%2C40.523%20246.813%2C30.575%20C246.813%2C26.74%20241.67%2C24.624%20238.434%2C24.624%20C231.747%2C24.624%20219.411%2C49.5%20216.183%2C61.525%20C216.183%2C61.525%20219.06%2C38.995%20220.478%2C27.518%20C220.846%2C24.548%20213.343%2C24.494%20211.913%2C24.494%20C208.768%2C24.494%20206.288%2C71.633%20206.288%2C88.202%20C206.288%2C91.255%20217.113%2C90.603%20217.113%2C88.081%20C217.113%2C64.376%20234.408%2C36.277%20236.424%2C36.277%20C236.908%2C36.277%20234.307%2C58.127%20234.307%2C68.305%20C234.307%2C77.968%20236.593%2C87.093%20244.697%2C87.093%20C247.931%2C87.093%20250.175%2C85.873%20252.168%2C83.95%20C252.146%2C85.317%20252.134%2C86.576%20252.134%2C87.695%20C252.134%2C90.748%20262.959%2C90.096%20262.959%2C87.574%20C262.959%2C63.869%20280.291%2C36.496%20282.27%2C36.496%20C283.184%2C36.496%20280.152%2C58.346%20280.152%2C68.524%20C280.152%2C78.187%20282.439%2C87.311%20290.543%2C87.311%20C294.084%2C87.311%20297.43%2C85.564%20299.755%2C83.258%20C301.392%2C88.272%20304.512%2C89.897%20308.669%2C89.897%20C314.357%2C89.897%20318.384%2C86.01%20321.191%2C82.423%20C323.923%2C87.317%20328.335%2C90.461%20334.807%2C90.461%20C343.777%2C90.461%20354.444%2C79.342%20354.444%2C71.189%20C354.444%2C69.269%20349.141%2C68.119%20348.502%2C69.445%20L348.502%2C69.445%20Z%22%20id%3D%22Fill-4%22%3E%3C%2Fpath%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cpath%20d%3D%22M46.304%2C90.885%20L46.305%2C90.885%20L46.304%2C90.885%20Z%20M46.304%2C90.885%20L46.305%2C90.885%20L46.304%2C90.885%20Z%20M41.739%2C15.657%20L41.495%2C17.071%20C39.677%2C27.589%2038.245%2C36.415%2037.736%2C46.244%20L37.682%2C47.301%20L37.064%2C47.106%20L36.672%2C46.982%20C34.934%2C46.432%2032.492%2C46.35%2031.19%2C46.35%20C30.383%2C46.35%2029.607%2C46.381%2028.944%2C46.439%20C28.087%2C46.506%2026.713%2C46.642%2025.005%2C46.914%20L24.437%2C47.004%20L23.537%2C47.148%20L24.125%2C45.782%20C30.119%2C31.844%2036.075%2C22.147%2040.015%2C16.465%20L42.124%2C13.426%20L41.739%2C15.657%20Z%20M52.273%2C4.751%20C51.251%2C2.197%2048.677%2C1.834%2045.696%2C1.414%20L45.192%2C1.344%20L44.896%2C1.398%20L44.877%2C1.406%20C34.534%2C7.217%2021.5%2C26.091%2011.661%2C49.507%20L11.51%2C49.863%20L11.141%2C49.974%20C8.066%2C50.896%206.097%2C51.792%204.756%2C52.879%20C3.691%2C53.713%203.699%2C56.02%204.253%2C57.87%20C4.707%2C59.39%205.466%2C60.514%206.388%2C61.035%20L6.62%2C61.166%20L6.987%2C61.373%20L6.757%2C62.021%20C3.044%2C72.543%200.731%2C79.414%200%2C87.71%20C-0.002%2C88.247%200.264%2C88.797%200.815%2C89.352%20C2.23%2C90.773%205.483%2C91.973%207.919%2C91.973%20C10.37%2C91.973%2010.943%2C90.84%2011.066%2C90.164%20C13.113%2C78.845%2015.494%2C69.593%2019.026%2C59.227%20L19.179%2C58.777%20L19.464%2C58.722%20L19.645%2C58.687%20C25.164%2C57.621%2031.011%2C56.553%2036.502%2C56.228%20L36.846%2C56.207%20L37.389%2C56.175%20L37.369%2C57.063%20C37.16%2C66.158%2037.334%2C85.246%2038.683%2C88.161%20C39.527%2C90.031%2043.215%2C91.186%2046.149%2C91.186%20C47.94%2C91.186%2049.149%2C90.74%2049.553%2C89.93%20L49.591%2C89.854%20L49.583%2C89.77%20C48.771%2C81.765%2045.091%2C40.097%2052.339%2C5.355%20C52.307%2C4.875%2052.275%2C4.756%2052.273%2C4.751%20L52.273%2C4.751%20Z%22%20id%3D%22Fill-5%22%3E%3C%2Fpath%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cpath%20d%3D%22M124.872%2C67.333%20C123.39%2C72.265%20120.349%2C80.539%20116.626%2C80.539%20C113.311%2C80.539%20111.169%2C75.18%20111.169%2C66.887%20C111.169%2C59.234%20116.919%2C34.224%20124.66%2C34.224%20C126.034%2C34.224%20127.065%2C35.211%20127.727%2C37.157%20C128.295%2C38.833%20128.583%2C41.197%20128.583%2C44.183%20C128.583%2C50.842%20127.161%2C59.712%20124.872%2C67.333%20Z%20M135.939%2C32.69%20C133.875%2C28.751%20130.721%2C26.669%20126.818%2C26.669%20C121.684%2C26.669%20116.745%2C31.957%20114.075%2C36.484%20L112.032%2C39.948%20L113.324%2C30.532%20C113.366%2C30.09%20113.261%2C29.129%20113.07%2C28.921%20C112.252%2C28.027%20109.545%2C27.449%20106.173%2C27.449%20C105.774%2C27.449%20105.381%2C27.881%20104.76%2C29.986%20C102.251%2C38.499%2098.611%2C65.721%2097.555%2C73.861%20C96.415%2C82.646%2095.421%2C91.099%2094.757%2C97.663%20C93.858%2C106.558%2093.879%2C108.368%2094.232%2C108.597%20C96.24%2C109.92%20100.755%2C111%20101.689%2C111%20C101.757%2C111%20101.816%2C110.993%20101.92%2C110.979%20C102.87%2C110.831%20103.201%2C110.549%20103.408%2C109.074%20C103.727%2C106.862%20104.084%2C102.923%20104.498%2C98.361%20C104.642%2C96.768%20104.79%2C95.013%20104.941%2C93.192%20L104.953%2C93.048%20C105.229%2C89.758%20105.572%2C85.664%20105.924%2C82.532%20L106.2%2C80.078%20L106.962%2C81.408%20L107.427%2C82.221%20C109.186%2C85.289%20112.21%2C88.946%20116.631%2C88.946%20C122.602%2C88.946%20128.277%2C84.023%20132.613%2C75.083%20C136.506%2C67.054%20138.83%2C56.726%20138.83%2C47.454%20C138.83%2C41.404%20137.831%2C36.299%20135.939%2C32.69%20L135.939%2C32.69%20Z%22%20id%3D%22Fill-7%22%3E%3C%2Fpath%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cpath%20d%3D%22M82.552%2C67.333%20C81.071%2C72.265%2078.03%2C80.539%2074.307%2C80.539%20C70.992%2C80.539%2068.85%2C75.18%2068.85%2C66.887%20C68.85%2C59.234%2074.6%2C34.224%2082.341%2C34.224%20C83.715%2C34.224%2084.746%2C35.211%2085.408%2C37.157%20C85.976%2C38.833%2086.264%2C41.197%2086.264%2C44.183%20C86.264%2C50.841%2084.842%2C59.712%2082.552%2C67.333%20Z%20M92.816%2C32.762%20C90.779%2C28.776%2087.666%2C26.669%2083.816%2C26.669%20C78.521%2C26.669%2073.966%2C32.957%2071.723%2C36.705%20L69.691%2C40.098%20L71.005%2C30.532%20C71.047%2C30.091%2070.942%2C29.129%2070.751%2C28.921%20C69.933%2C28.027%2067.226%2C27.449%2063.854%2C27.449%20C63.455%2C27.449%2063.062%2C27.881%2062.441%2C29.986%20C59.932%2C38.496%2056.292%2C65.721%2055.235%2C73.861%20C54.097%2C82.641%2053.103%2C91.093%2052.437%2C97.663%20C51.539%2C106.558%2051.56%2C108.368%2051.912%2C108.597%20C53.921%2C109.92%2058.436%2C111%2059.369%2C111%20C59.438%2C111%2059.496%2C110.993%2059.601%2C110.979%20C60.551%2C110.831%2060.882%2C110.549%2061.089%2C109.074%20C61.407%2C106.869%2061.767%2C102.891%2062.185%2C98.286%20L62.201%2C98.112%20L62.209%2C98.024%20C62.621%2C93.498%2063.089%2C88.369%2063.605%2C84.017%20L63.879%2C81.704%20L65.096%2C83.69%20C67.203%2C87.129%2070.389%2C88.946%2074.312%2C88.946%20C80.049%2C88.946%2085.506%2C84.06%2089.677%2C75.188%20C93.429%2C67.205%2095.67%2C56.921%2095.67%2C47.68%20C95.67%2C41.572%2094.683%2C36.413%2092.816%2C32.762%20L92.816%2C32.762%20Z%22%20id%3D%22Fill-8%22%3E%3C%2Fpath%3E%0A%20%20%20%20%20%20%20%20%3C%2Fg%3E%0A%20%20%20%20%3C%2Fg%3E%0A%3C%2Fsvg%3E" style="opacity: 0.2"></image><g class="highcharts-grid"><path fill="none" d="M 108.5 10 L 108.5 169" stroke="#D8D8D8" stroke-width="1" opacity="1"></path><path fill="none" d="M 234.5 10 L 234.5 169" stroke="#D8D8D8" stroke-width="1" opacity="1"></path><path fill="none" d="M 360.5 10 L 360.5 169" stroke="#D8D8D8" stroke-width="1" opacity="1"></path><path fill="none" d="M 486.5 10 L 486.5 169" stroke="#D8D8D8" stroke-width="1" opacity="1"></path></g><g class="highcharts-grid"><path fill="none" d="M 46 169.5 L 676 169.5" stroke="#D8D8D8" stroke-width="1" opacity="1"></path><path fill="none" d="M 46 116.5 L 676 116.5" stroke="#D8D8D8" stroke-width="1" opacity="1"></path><path fill="none" d="M 46 63.5 L 676 63.5" stroke="#D8D8D8" stroke-width="1" opacity="1"></path><path fill="none" d="M 46 9.5 L 676 9.5" stroke="#D8D8D8" stroke-width="1" opacity="1"></path></g><g class="highcharts-axis"><path fill="none" d="M 46 169.5 L 676 169.5" stroke="#C0D0E0" stroke-width="1"></path></g><g class="highcharts-axis"></g><path fill="none" d="M 486.5 10 L 486.5 169" pointer-events="none" stroke="#C0C0C0" stroke-width="1" visibility="hidden"></path><path fill="none" d="M 46 30.5 L 676 30.5" pointer-events="none" stroke="#000" stroke-width="1" visibility="hidden"></path><g class="highcharts-series-group"><g class="highcharts-series highcharts-series-0 highcharts-tracker" transform="translate(46,10) scale(1 1)" style="" clip-path="url(#highcharts-1)"><rect x="32.5" y="145.5" width="61" height="14" stroke="#DC4128" stroke-width="1" fill="rgba(220,65,40,0.4)" rx="0" ry="0"></rect><rect x="158.5" y="136.5" width="61" height="23" stroke="#DC4128" stroke-width="1" fill="rgba(220,65,40,0.4)" rx="0" ry="0"></rect><rect x="284.5" y="136.5" width="61" height="23" stroke="#DC4128" stroke-width="1" fill="rgba(220,65,40,0.4)" rx="0" ry="0"></rect><rect x="410.5" y="135.5" width="61" height="24" stroke="#DC4128" stroke-width="1" fill="rgba(220,65,40,0.4)" rx="0" ry="0"></rect><rect x="536.5" y="146.5" width="61" height="13" stroke="#DC4128" stroke-width="1" fill="rgba(220,65,40,0.4)" rx="0" ry="0"></rect></g><g class="highcharts-markers highcharts-series-0" transform="translate(46,10) scale(1 1)" clip-path="none"></g><g class="highcharts-series highcharts-series-1 highcharts-tracker" transform="translate(46,10) scale(1 1)" style="" clip-path="url(#highcharts-1)"><rect x="32.5" y="142.5" width="61" height="3" stroke="#EF6C00" stroke-width="1" fill="rgba(239,108,0,0.4)" rx="0" ry="0"></rect><rect x="158.5" y="131.5" width="61" height="5" stroke="#EF6C00" stroke-width="1" fill="rgba(239,108,0,0.4)" rx="0" ry="0"></rect><rect x="284.5" y="132.5" width="61" height="4" stroke="#EF6C00" stroke-width="1" fill="rgba(239,108,0,0.4)" rx="0" ry="0"></rect><rect x="410.5" y="128.5" width="61" height="7" stroke="#EF6C00" stroke-width="1" fill="rgba(239,108,0,0.4)" rx="0" ry="0"></rect><rect x="536.5" y="145.5" width="61" height="1" stroke="#EF6C00" stroke-width="1" fill="rgba(239,108,0,0.4)" rx="0" ry="0"></rect></g><g class="highcharts-markers highcharts-series-1" transform="translate(46,10) scale(1 1)" clip-path="none"></g><g class="highcharts-series highcharts-series-2 highcharts-tracker" transform="translate(46,10) scale(1 1)" style="" clip-path="url(#highcharts-1)"><rect x="32.5" y="137.5" width="61" height="5" stroke="#F6A623" stroke-width="1" fill="rgba(246,166,35,0.4)" rx="0" ry="0"></rect><rect x="158.5" y="125.5" width="61" height="6" stroke="#F6A623" stroke-width="1" fill="rgba(246,166,35,0.4)" rx="0" ry="0"></rect><rect x="284.5" y="128.5" width="61" height="4" stroke="#F6A623" stroke-width="1" fill="rgba(246,166,35,0.4)" rx="0" ry="0"></rect><rect x="410.5" y="121.5" width="61" height="7" stroke="#F6A623" stroke-width="1" fill="rgba(246,166,35,0.4)" rx="0" ry="0"></rect><rect x="536.5" y="143.5" width="61" height="2" stroke="#F6A623" stroke-width="1" fill="rgba(246,166,35,0.4)" rx="0" ry="0"></rect></g><g class="highcharts-markers highcharts-series-2" transform="translate(46,10) scale(1 1)" clip-path="none"></g><g class="highcharts-series highcharts-series-3 highcharts-tracker" transform="translate(46,10) scale(1 1)" style="" clip-path="url(#highcharts-1)"><rect x="32.5" y="127.5" width="61" height="10" stroke="#91C848" stroke-width="1" fill="rgba(145,200,72,0.4)" rx="0" ry="0"></rect><rect x="158.5" y="117.5" width="61" height="8" stroke="#91C848" stroke-width="1" fill="rgba(145,200,72,0.4)" rx="0" ry="0"></rect><rect x="284.5" y="120.5" width="61" height="8" stroke="#91C848" stroke-width="1" fill="rgba(145,200,72,0.4)" rx="0" ry="0"></rect><rect x="410.5" y="109.5" width="61" height="12" stroke="#91C848" stroke-width="1" fill="rgba(145,200,72,0.4)" rx="0" ry="0"></rect><rect x="536.5" y="140.5" width="61" height="3" stroke="#91C848" stroke-width="1" fill="rgba(145,200,72,0.4)" rx="0" ry="0"></rect></g><g class="highcharts-markers highcharts-series-3" transform="translate(46,10) scale(1 1)" clip-path="none"></g><g class="highcharts-series highcharts-series-4 highcharts-tracker" transform="translate(46,10) scale(1 1)" style="" clip-path="url(#highcharts-1)"><rect x="32.5" y="76.5" width="61" height="51" stroke="#00A851" stroke-width="1" fill="rgba(0,168,81,0.4)" rx="0" ry="0"></rect><rect x="158.5" y="46.5" width="61" height="71" stroke="#00A851" stroke-width="1" fill="rgba(0,168,81,0.4)" rx="0" ry="0"></rect><rect x="284.5" y="51.5" width="61" height="69" stroke="#00A851" stroke-width="1" fill="rgba(0,168,81,0.4)" rx="0" ry="0"></rect><rect x="410.5" y="22.5" width="61" height="87" stroke="#00A851" stroke-width="1" fill="rgba(0,168,81,0.4)" rx="0" ry="0"></rect><rect x="536.5" y="102.5" width="61" height="38" stroke="#00A851" stroke-width="1" fill="rgba(0,168,81,0.4)" rx="0" ry="0"></rect></g><g class="highcharts-markers highcharts-series-4" transform="translate(46,10) scale(1 1)" clip-path="none"></g><g class="highcharts-series highcharts-series-5" transform="translate(46,10) scale(1 1)" clip-path="url(#highcharts-1)"><path fill="none" d="M 53 87.2115 L 63 87.2115 C 63 87.2115 138.6 87.2115 189 87.2115 C 239.4 87.2115 264.6 87.2115 315 87.2115 C 365.4 87.2115 390.6 87.2115 441 87.2115 C 491.4 87.2115 567 87.2115 567 87.2115 L 577 87.2115" stroke-linejoin="round" visibility="visible" stroke="rgba(192,192,192,0.0001)" stroke-width="20" class=" highcharts-tracker" style=""></path></g><g class="highcharts-markers highcharts-series-5 highcharts-tracker" transform="translate(46,10) scale(1 1)" style="" clip-path="none"></g></g><rect x="46" y="152.359375" width="171.015625" height="16.96875" fill="rgba(255, 255, 255, 0.7)"></rect><g class="highcharts-axis-labels highcharts-xaxis-labels"><text x="109" style="color:#606060;cursor:default;font-size:11px;white-space:nowrap;text-overflow:none;fill:#606060;width:200px;" text-anchor="middle" transform="translate(0,0)" y="188" opacity="1"><tspan>4月28日</tspan></text><text x="235" style="color:#606060;cursor:default;font-size:11px;white-space:nowrap;text-overflow:none;fill:#606060;width:200px;" text-anchor="middle" transform="translate(0,0)" y="188" opacity="1"><tspan>5月5日</tspan></text><text x="361" style="color:#606060;cursor:default;font-size:11px;white-space:nowrap;text-overflow:none;fill:#606060;width:200px;" text-anchor="middle" transform="translate(0,0)" y="188" opacity="1"><tspan>5月12日</tspan></text><text x="487" style="color:#606060;cursor:default;font-size:11px;white-space:nowrap;text-overflow:none;fill:#606060;width:200px;" text-anchor="middle" transform="translate(0,0)" y="188" opacity="1"><tspan>5月19日</tspan></text></g><text x="51" y="165"><tspan style="font-size: 11px; fill: #102235; font: Proxima Nova Soft, normal;">©2019 App Annie Intelligence</tspan></text><g class="highcharts-axis-labels highcharts-yaxis-labels"><text x="31" style="color:#606060;cursor:default;font-size:11px;fill:#606060;width:216px;text-overflow:clip;" text-anchor="end" transform="translate(0,0)" y="174" opacity="1"><tspan>0</tspan></text><text x="31" style="color:#606060;cursor:default;font-size:11px;fill:#606060;width:216px;text-overflow:clip;" text-anchor="end" transform="translate(0,0)" y="121" opacity="1"><tspan>100</tspan></text><text x="31" style="color:#606060;cursor:default;font-size:11px;fill:#606060;width:216px;text-overflow:clip;" text-anchor="end" transform="translate(0,0)" y="68" opacity="1"><tspan>200</tspan></text><text x="31" style="color:#606060;cursor:default;font-size:11px;fill:#606060;width:216px;text-overflow:clip;" text-anchor="end" transform="translate(0,0)" y="15" opacity="1"><tspan>300</tspan></text></g><g class="event-group"><image preserveAspectRatio="none" x="487" y="169" width="14" height="14" NS2:href="data:image/svg+xml;charset=utf8,%3Csvg%20width%3D'119'%20height%3D'119'%20viewBox%3D'0%200%20119%20119'%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20xmlns%3Axlink%3D'http%3A%2F%2Fwww.w3.org%2F1999%2Fxlink'%3E%3Cdefs%3E%3Cpath%20id%3D'a'%20d%3D'M118.75%20118.9998V.25H0v118.7498h118.75z'%2F%3E%3C%2Fdefs%3E%3Cg%20fill%3D'none'%20fill-rule%3D'evenodd'%3E%3Cg%20transform%3D'translate(0%20-.25)'%3E%3Cmask%20id%3D'b'%20fill%3D'%23fff'%3E%3Cuse%20xlink%3Ahref%3D'%23a'%2F%3E%3C%2Fmask%3E%3Cpath%20d%3D'M63.3125%2091.7178c1.081%200%202.125.412%202.916%201.158.852.803%201.334%201.922%201.334%203.092v9.089c9.637-8.869%2025.856-23.771%2028.439-25.959%209.188-7.79%2014.249-18.02%2014.249-28.806%200-22.906-22.823-41.542-50.876-41.542-28.052%200-50.875%2018.636-50.875%2041.542%200%2022.906%2022.823%2041.542%2050.875%2041.542%201.214%200%202.455-.037%203.69-.109.083-.005.166-.007.248-.007m-.001%2027.282c-.576%200-1.156-.117-1.704-.357-1.546-.677-2.545-2.205-2.545-3.893v-14.417c-32.597-.141-59.063-22.535-59.063-50.041%200-27.593%2026.636-50.042%2059.375-50.042%2032.74%200%2059.376%2022.449%2059.376%2050.042%200%2013.325-6.127%2025.858-17.252%2035.289-3.499%202.967-34.987%2032-35.305%2032.293-.8.739-1.834%201.126-2.882%201.126'%20fill%3D'%23797979'%20mask%3D'url(%23b)'%2F%3E%3Cpath%20d%3D'M63.3125%2091.7178c1.081%200%202.125.412%202.916%201.158.852.803%201.334%201.922%201.334%203.092v9.089c9.637-8.869%2025.856-23.771%2028.439-25.959%209.188-7.79%2014.249-18.02%2014.249-28.806%200-22.906-22.823-41.542-50.876-41.542-28.052%200-50.875%2018.636-50.875%2041.542%200%2022.906%2022.823%2041.542%2050.875%2041.542%201.214%200%202.455-.037%203.69-.109.083-.005.166-.007.248-.007'%20fill%3D'%23FFF'%20mask%3D'url(%23b)'%2F%3E%3C%2Fg%3E%3Cpath%20d%3D'M87.9609%2049.9912c-1.887%200-3.61-1.266-4.109-3.177-.876-3.353-2.644-6.431-5.112-8.899-2.227-2.227-4.863-3.842-7.834-4.801-2.234-.721-3.461-3.116-2.74-5.35.722-2.234%203.117-3.46%205.35-2.739%204.206%201.357%208.091%203.736%2011.234%206.879%203.536%203.536%206.069%207.949%207.326%2012.762.593%202.271-.767%204.594-3.038%205.186-.36.094-.722.139-1.077.139'%20fill%3D'%23797979'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E" cursor="pointer" transform="translate(-7 -4)"></image></g><g class="highcharts-tooltip" display="block" style="cursor:default;padding:0;pointer-events:none;white-space:nowrap;" transform="translate(333,-9999)" visibility="visible" opacity="0"><path fill="none" d="M 2.5 0.5 L 146.5 0.5 C 148.5 0.5 148.5 0.5 148.5 2.5 L 148.5 145.5 C 148.5 147.5 148.5 147.5 146.5 147.5 L 2.5 147.5 C 0.5 147.5 0.5 147.5 0.5 145.5 L 0.5 2.5 C 0.5 0.5 0.5 0.5 2.5 0.5" isShadow="true" stroke="black" stroke-opacity="0.049999999999999996" stroke-width="5" transform="translate(1, 1)"></path><path fill="none" d="M 2.5 0.5 L 146.5 0.5 C 148.5 0.5 148.5 0.5 148.5 2.5 L 148.5 145.5 C 148.5 147.5 148.5 147.5 146.5 147.5 L 2.5 147.5 C 0.5 147.5 0.5 147.5 0.5 145.5 L 0.5 2.5 C 0.5 0.5 0.5 0.5 2.5 0.5" isShadow="true" stroke="black" stroke-opacity="0.09999999999999999" stroke-width="3" transform="translate(1, 1)"></path><path fill="none" d="M 2.5 0.5 L 146.5 0.5 C 148.5 0.5 148.5 0.5 148.5 2.5 L 148.5 145.5 C 148.5 147.5 148.5 147.5 146.5 147.5 L 2.5 147.5 C 0.5 147.5 0.5 147.5 0.5 145.5 L 0.5 2.5 C 0.5 0.5 0.5 0.5 2.5 0.5" isShadow="true" stroke="black" stroke-opacity="0.15" stroke-width="1" transform="translate(1, 1)"></path><path fill="rgba(255, 255, 255, 0.9)" d="M 2.5 0.5 L 146.5 0.5 C 148.5 0.5 148.5 0.5 148.5 2.5 L 148.5 145.5 C 148.5 147.5 148.5 147.5 146.5 147.5 L 2.5 147.5 C 0.5 147.5 0.5 147.5 0.5 145.5 L 0.5 2.5 C 0.5 0.5 0.5 0.5 2.5 0.5" stroke="#666666" stroke-width="1"></path></g></svg><div class="highcharts-tooltip" style="position: absolute; left: 333px; top: -9999px; display: block; opacity: 0; pointer-events: none; visibility: visible;"><span style="position: absolute; font-family: inherit; font-size: 12px; white-space: nowrap; color: rgb(51, 51, 51); margin-left: 0px; margin-top: 0px; left: 8px; top: 8px;"><div class="chart-hover-tip" style="opacity: 1; position: static; border: none; padding: 0; line-height: 20px; background: none;"><table cellspacing="0">
    <thead class="chart-tip-head">
        <tr class="time-info">
            <td colspan="2">
                <i class="fa fa-globe"></i>
                <span class="label">5月 19-25, 2019</span>
                            </td>
        </tr>
    </thead>
    <tbody class="chart-tip-body">
        <tr>
            <td class="legend"><i class="label-dot" style="background-color: rgb(0,168,81)"></i><span class="label">5星 </span></td>
            <td class="value "><b>
                <!--
             -->163<!--
             -->
            </b></td>
            
        </tr>
        <tr>
            <td class="legend"><i class="label-dot" style="background-color: rgb(145,200,72)"></i><span class="label">4星 </span></td>
            <td class="value "><b>
                <!--
             -->24<!--
             -->
            </b></td>
            
        </tr>
        <tr>
            <td class="legend"><i class="label-dot" style="background-color: rgb(246,166,35)"></i><span class="label">3星 </span></td>
            <td class="value "><b>
                <!--
             -->12<!--
             -->
            </b></td>
            
        </tr>
        <tr>
            <td class="legend"><i class="label-dot" style="background-color: rgb(239,108,0)"></i><span class="label">2星 </span></td>
            <td class="value "><b>
                <!--
             -->14<!--
             -->
            </b></td>
            
        </tr>
        <tr>
            <td class="legend"><i class="label-dot" style="background-color: rgb(220,65,40)"></i><span class="label">1星 </span></td>
            <td class="value "><b>
                <!--
             -->45<!--
             -->
            </b></td>
            
        </tr>
    </tbody>
</table>
</div></span></div></div><div class="chart-event-wrap" style="transform: translate(14px, -10px);">
    <div class="chart-event-tooltip" data-event-key="1558224000000" style="right: 126px">
        <ul class="chart-event-tooltip-content">
            <li class="event-block">
                <div class="time-info">周一 2019年5月20日</div>
                <div class="event-content">
                    <strong>Idle Heroes: </strong>应用版本已升级至1.22.0。<br>
                </div>
            </li>
        </ul>
    </div>
</div></div><div class="data-notice"></div><div class="chart-legend-container"></div></div><aa-legend primary-object-type="primaryObjectType" primary-object-name="primaryObjectName" secondary-object-type="secondaryObjectType" items="items" class="ng-isolate-scope"><div class="Legend">    <!-- ngIf: $ctrl.primaryObjectType -->    <!-- ngIf: $ctrl.secondaryObjectType -->    <!-- ngRepeat: item in $ctrl.items --><aa-legend-item ng-repeat="item in $ctrl.items" name="item.name" locked="item.locked" checked="item.checked" color="item.color" on-click="$ctrl.toggleItem(item)" class="ng-scope ng-isolate-scope" style=""><div class="LegendItem ng-binding" ng-click="$ctrl.onClick()" tabindex="0">    <!-- ngIf: $ctrl.locked -->    <!-- ngIf: !$ctrl.locked --><span class="LegendItem-color LegendItem-marker ng-scope" ng-style="$ctrl.colorStyle" ng-if="!$ctrl.locked" style="background-color: rgb(220, 65, 40);"></span><!-- end ngIf: !$ctrl.locked -->    1星 </div></aa-legend-item><!-- end ngRepeat: item in $ctrl.items --><aa-legend-item ng-repeat="item in $ctrl.items" name="item.name" locked="item.locked" checked="item.checked" color="item.color" on-click="$ctrl.toggleItem(item)" class="ng-scope ng-isolate-scope"><div class="LegendItem ng-binding" ng-click="$ctrl.onClick()" tabindex="0">    <!-- ngIf: $ctrl.locked -->    <!-- ngIf: !$ctrl.locked --><span class="LegendItem-color LegendItem-marker ng-scope" ng-style="$ctrl.colorStyle" ng-if="!$ctrl.locked" style="background-color: rgb(239, 108, 0);"></span><!-- end ngIf: !$ctrl.locked -->    2星 </div></aa-legend-item><!-- end ngRepeat: item in $ctrl.items --><aa-legend-item ng-repeat="item in $ctrl.items" name="item.name" locked="item.locked" checked="item.checked" color="item.color" on-click="$ctrl.toggleItem(item)" class="ng-scope ng-isolate-scope"><div class="LegendItem ng-binding" ng-click="$ctrl.onClick()" tabindex="0">    <!-- ngIf: $ctrl.locked -->    <!-- ngIf: !$ctrl.locked --><span class="LegendItem-color LegendItem-marker ng-scope" ng-style="$ctrl.colorStyle" ng-if="!$ctrl.locked" style="background-color: rgb(246, 166, 35);"></span><!-- end ngIf: !$ctrl.locked -->    3星 </div></aa-legend-item><!-- end ngRepeat: item in $ctrl.items --><aa-legend-item ng-repeat="item in $ctrl.items" name="item.name" locked="item.locked" checked="item.checked" color="item.color" on-click="$ctrl.toggleItem(item)" class="ng-scope ng-isolate-scope"><div class="LegendItem ng-binding" ng-click="$ctrl.onClick()" tabindex="0">    <!-- ngIf: $ctrl.locked -->    <!-- ngIf: !$ctrl.locked --><span class="LegendItem-color LegendItem-marker ng-scope" ng-style="$ctrl.colorStyle" ng-if="!$ctrl.locked" style="background-color: rgb(145, 200, 72);"></span><!-- end ngIf: !$ctrl.locked -->    4星 </div></aa-legend-item><!-- end ngRepeat: item in $ctrl.items --><aa-legend-item ng-repeat="item in $ctrl.items" name="item.name" locked="item.locked" checked="item.checked" color="item.color" on-click="$ctrl.toggleItem(item)" class="ng-scope ng-isolate-scope"><div class="LegendItem ng-binding" ng-click="$ctrl.onClick()" tabindex="0">    <!-- ngIf: $ctrl.locked -->    <!-- ngIf: !$ctrl.locked --><span class="LegendItem-color LegendItem-marker ng-scope" ng-style="$ctrl.colorStyle" ng-if="!$ctrl.locked" style="background-color: rgb(0, 168, 81);"></span><!-- end ngIf: !$ctrl.locked -->    5星 </div></aa-legend-item><!-- end ngRepeat: item in $ctrl.items --></div></aa-legend></div>
            </div>

            <div class="right-chart-container">
                <app-rating-summary reviews-summary="reviewsSummary" class="ng-isolate-scope"><div class="ratings-container">
    <div class="ratings-summary">
        <div class="summary-section">
            <div class="rating-number ng-binding">3.9</div>
            <div aa-stars="" stars="reviewsSummary.averageRatings | number: 1"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width: 3.9em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div></div>
            <div class="rating-count ng-binding">
                938 评论
            </div>
        </div>
    </div>

    <table class="aa-rating-bars" cellspacing="0" cellpadding="0">
        <tbody>
            <!-- ngRepeat: item in reviewsSummary.items --><tr ng-repeat="item in reviewsSummary.items" class="rating-bar ng-scope" style="">
                <td class="stars">
                    <i class="fa fa-star"></i>
                    <span class="star-count ng-binding">5</span>
                </td>

                <td class="bar">
                    <div class="bar-bg">
                        <div class="rating-bar-5 bar-fg" ng-style="getStyle(reviewsSummary.totalReviews, item.reviews)" style="width: 63.32622601279318%;"></div>
                    </div>
                </td>

                <td class="rating-count ng-binding">594</td>
            </tr><!-- end ngRepeat: item in reviewsSummary.items --><tr ng-repeat="item in reviewsSummary.items" class="rating-bar ng-scope">
                <td class="stars">
                    <i class="fa fa-star"></i>
                    <span class="star-count ng-binding">4</span>
                </td>

                <td class="bar">
                    <div class="bar-bg">
                        <div class="rating-bar-4 bar-fg" ng-style="getStyle(reviewsSummary.totalReviews, item.reviews)" style="width: 8.315565031982942%;"></div>
                    </div>
                </td>

                <td class="rating-count ng-binding">78</td>
            </tr><!-- end ngRepeat: item in reviewsSummary.items --><tr ng-repeat="item in reviewsSummary.items" class="rating-bar ng-scope">
                <td class="stars">
                    <i class="fa fa-star"></i>
                    <span class="star-count ng-binding">3</span>
                </td>

                <td class="bar">
                    <div class="bar-bg">
                        <div class="rating-bar-3 bar-fg" ng-style="getStyle(reviewsSummary.totalReviews, item.reviews)" style="width: 4.797441364605544%;"></div>
                    </div>
                </td>

                <td class="rating-count ng-binding">45</td>
            </tr><!-- end ngRepeat: item in reviewsSummary.items --><tr ng-repeat="item in reviewsSummary.items" class="rating-bar ng-scope">
                <td class="stars">
                    <i class="fa fa-star"></i>
                    <span class="star-count ng-binding">2</span>
                </td>

                <td class="bar">
                    <div class="bar-bg">
                        <div class="rating-bar-2 bar-fg" ng-style="getStyle(reviewsSummary.totalReviews, item.reviews)" style="width: 4.051172707889126%;"></div>
                    </div>
                </td>

                <td class="rating-count ng-binding">38</td>
            </tr><!-- end ngRepeat: item in reviewsSummary.items --><tr ng-repeat="item in reviewsSummary.items" class="rating-bar ng-scope">
                <td class="stars">
                    <i class="fa fa-star"></i>
                    <span class="star-count ng-binding">1</span>
                </td>

                <td class="bar">
                    <div class="bar-bg">
                        <div class="rating-bar-1 bar-fg" ng-style="getStyle(reviewsSummary.totalReviews, item.reviews)" style="width: 19.50959488272921%;"></div>
                    </div>
                </td>

                <td class="rating-count ng-binding">183</td>
            </tr><!-- end ngRepeat: item in reviewsSummary.items -->
        </tbody>
    </table>

    <div class="all-time-rating ng-binding">
        All ratings average: 3.9 for
        <span class="total-reviews ng-binding">
            40,326
        </span>
        total reviews
    </div>
</div>
</app-rating-summary>
            </div>
            <div class="clearfix"></div>
        </div>
    </div>
</div>
</div>
        <!-- ngInclude: 'app/tpl/ng_app_review_table.tpl' --><div ng-include="'app/tpl/ng_app_review_table.tpl'" class="ng-scope"><div ng-controller="AppReviewsTableCtrl" class="review-table ng-scope">
    <div aa-loading="status === 'loading'" class="ng-isolate-scope"><!-- ngIf: loading() --></div>
    <div aa-show="status === 'fail'" class="ng-hide">
        加载表格数据失败
    </div>

    <div aa-show="status !== 'loading' &amp;&amp; status !== 'fail'" class="">
        <aa-float-top class="ng-isolate-scope"><div class="float-top-wrapper"><div class="float-top-content" ng-style="$ctrl.style" ng-class="$ctrl.className" ng-transclude="" style="width: 100%; height: 30px;">
            <div class="translate-control-bar ng-scope">
                <!-- ngIf: !isLocked -->

                <!-- ngIf: isLocked --><span ng-if="isLocked" class="no-permission ng-scope">
                    翻译评价
                    <i class="aaicon-aa-lock icon" ng-click="limitedAccessTrigger()" data-helptip="单击即可使用App Annie Intelligence解锁该功能" data-helptip-width="300"></i>
                </span><!-- end ngIf: isLocked -->
            </div>
        </div></div></aa-float-top>

        <div class="table-container">
            <div aa-dashboard-table="table.data.table" aa-dashboard-table-desc="meta.order_type" aa-dashboard-table-page-index="meta.page" aa-dashboard-table-page-size="meta.interval" aa-dashboard-table-page-limit="limit" aa-dashboard-table-orderby="meta.order_by" aa-dashboard-table-controller-actions="positioningHandler()" dashboard-limited-access="" class="ng-isolate-scope"><div class="aa-dashboard-table-container ng-isolate-scope" aa-table="data" aa-table-orderby="tableOrderby" aa-table-desc="tableDesc" aa-table-page-index="pageIndex" aa-table-page-size="pageSize" aa-table-page-limit="pageLimit"><div class="floating-header" style="position: fixed; top: 30px; display: none; z-index: 10; left: 250px;"><table cellspacing="0" cellpadding=""><colgroup><col weight="1" data-index="1" style="width: 12.5%;"><col weight="4" data-index="2" style="width: 50%;"><col weight="1" data-index="3" style="width: 12.5%;"><col weight="1" data-index="4" style="width: 12.5%;"><col weight="1" data-index="5" style="width: 12.5%;"></colgroup><thead><tr><th rowspan="2" class="star_rating col-rating click-to-sort fixed-index-0 tbl-col-star-rating" data-colidx="0" colspan="1"><div><span class="column-header-container">评级</span><b class="sort-btn sort-status-none"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th><th rowspan="2" class="review col-reviews fixed-index-1 tbl-col-review" data-colidx="1" colspan="1"><div><span class="column-header-container">评价</span></div></th><th rowspan="2" class="text_short col-date click-to-sort row-sorted fixed-index-2 tbl-col-text-short" data-colidx="2" colspan="1"><div><span class="column-header-container">日期</span><b class="sort-btn sort-status-desc"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th><th rowspan="2" class="country_flag_with_text col-country click-to-sort fixed-index-3 tbl-col-country-flag-with-text" data-colidx="3" colspan="1"><div><span class="column-header-container">国家/地区</span><b class="sort-btn sort-status-none"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th><th rowspan="2" class="text_short col-version click-to-sort fixed-index-4 tbl-col-text-short" data-colidx="4" colspan="1"><div><span class="column-header-container">版本</span><b class="sort-btn sort-status-none"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th></tr><tr></tr></thead></table></div><div class="dashboard-table"><div><table cellspacing="0" cellpadding=""><colgroup><col weight="1" data-index="1" style="width: 12.5%;"><col weight="4" data-index="2" style="width: 50%;"><col weight="1" data-index="3" style="width: 12.5%;"><col weight="1" data-index="4" style="width: 12.5%;"><col weight="1" data-index="5" style="width: 12.5%;"></colgroup><thead><tr><th rowspan="2" class="star_rating col-rating click-to-sort fixed-index-0 tbl-col-star-rating" data-colidx="0" colspan="1"><div><span class="column-header-container">评级</span><b class="sort-btn sort-status-none"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th><th rowspan="2" class="review col-reviews fixed-index-1 tbl-col-review" data-colidx="1" colspan="1"><div><span class="column-header-container">评价</span></div></th><th rowspan="2" class="text_short col-date click-to-sort row-sorted fixed-index-2 tbl-col-text-short" data-colidx="2" colspan="1"><div><span class="column-header-container">日期</span><b class="sort-btn sort-status-desc"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th><th rowspan="2" class="country_flag_with_text col-country click-to-sort fixed-index-3 tbl-col-country-flag-with-text" data-colidx="3" colspan="1"><div><span class="column-header-container">国家/地区</span><b class="sort-btn sort-status-none"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th><th rowspan="2" class="text_short col-version click-to-sort fixed-index-4 tbl-col-text-short" data-colidx="4" colspan="1"><div><span class="column-header-container">版本</span><b class="sort-btn sort-status-none"><i class="fa fa-sort-asc"></i><i class="fa fa-sort-desc"></i></b></div></th></tr><tr></tr></thead><tbody data-ref="main"><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:5em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">5.0</div></div></td><td class="text tbl-col-review" id="4230292243" data-id="4230292243">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>So good</strong>
            </div>
            <div>I got it yesterday and it gave me free stuff</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/gb.gif" width="17" height="11">GB</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:5em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">5.0</div></div></td><td class="text tbl-col-review" id="4229616386" data-id="4229616386">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>Bel gioco</strong>
            </div>
            <div>Questo gioco credo sia la miglior app per cellulare perché non serve nemmeno spendere soldi perchè c'è l'auto-farming che ti da molte cose che ti servono, lo consiglio a tutti questa app passatempo!</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/it.gif" width="17" height="11">IT</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:1em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">1.0</div></div></td><td class="text tbl-col-review" id="4229314853" data-id="4229314853">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>Terrible servers</strong>
            </div>
            <div>I get it there’s a lot of servers so it tends to be hard to keep up however don’t keep making servers if it’s gunna slow down every single server you cannot go 2 minutes without having to force close the app so much so actually that i had to delete this game despite spending so much money on it if i could get a refund i would this is probably the worst game in the App Store to date don’t download this game and if you put yourself through that torture atleast don’t give them your money they really don’t deserve it thanks for being a piece of trash and taking my money and in return giving me terrible servers 🖕</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/us.gif" width="17" height="11">US</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:5em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">5.0</div></div></td><td class="text tbl-col-review" id="4231370561" data-id="4231370561">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>Addicted</strong>
            </div>
            <div>Addicting took me a few worlds but pretty even based and ADDICTING... anyone need help look me up....</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/us.gif" width="17" height="11">US</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:1em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">1.0</div></div></td><td class="text tbl-col-review" id="4228223701" data-id="4228223701">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>Great Game bad advertising</strong>
            </div>
            <div>Game is great but after seeing its newest advertisement kind of shocked you guys were that dumb. In your advertisement when talking about all the times you can upgrade and play your game and one was “Upgrade while driving”. ?!? Nobody should be doing anything like this “While driving”. So your new advertisement I gotta say...that ain’t it chief.</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/us.gif" width="17" height="11">US</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:1em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">1.0</div></div></td><td class="text tbl-col-review" id="4230343837" data-id="4230343837">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>I can’t even 🙄</strong>
            </div>
            <div>Yeah the game looks cool, but when I got it. HOLY COW was I wrong, don’t play this game!</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/us.gif" width="17" height="11">US</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:5em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">5.0</div></div></td><td class="text tbl-col-review" id="4229446105" data-id="4229446105">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>Good</strong>
            </div>
            <div>Good game</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/us.gif" width="17" height="11">US</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:2em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">2.0</div></div></td><td class="text tbl-col-review" id="4230381757" data-id="4230381757">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>面白いけど…</strong>
            </div>
            <div>面白いと思うが、広告の詐欺が酷すぎる</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/jp.gif" width="17" height="11">JP</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:5em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">5.0</div></div></td><td class="text tbl-col-review" id="4228096629" data-id="4228096629">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>Idle Hero</strong>
            </div>
            <div>Superb</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/sg.gif" width="17" height="11">SG</td><td class="text  tbl-col-text-short">1.22.0</td></tr><tr class="main-row table-row"><td class="star-rating tbl-col-star-rating"><div class="aa-stars"><div class="rating-star"><div class="bg"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div><div class="fg" style="width:5em;"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div></div><div class="rating-value">5.0</div></div></td><td class="text tbl-col-review" id="4229685227" data-id="4229685227">
    
        <div class="original-review">
            <div class="review-cell-header">
                    <strong>能够退订吗？我一直每个星期扣钱</strong>
            </div>
            <div>能退订吗？没个星期都扣钱。很烦</div>
        </div>

</td>
<td class="text row-sorted  tbl-col-text-short">2019年5月29日</td><td class="country_flag_with_text   tbl-col-country-flag-with-text"><img class="flag" src="/media/pictures/flags/gif/cn.gif" width="17" height="11">CN</td><td class="text  tbl-col-text-short">1.22.0</td></tr></tbody></table></div></div>
<!-- ngIf: footNoteMsg -->
<div class="paginator aa-paginator ng-isolate-scope" aa-paginator="data.pagination" aa-paginator-index="pageIndex" aa-paginator-size="pageSize" aa-paginator-limit="pageLimit" style="display: block;">显示行数：<select><option value="10" selected="">10</option><option value="50">50</option><option value="100">100</option></select>跳转到第<form class="paginator-content"><input type="text" value="1"></form>页，共94页<button data-id="prev" class="btn fa fa-angle-left turn-page disabled" disabled=""></button><button data-id="next" class="btn fa fa-angle-right turn-page"></button></div>
</div></div>
        </div>
    </div>
</div>
</div>
    </div><!-- end ngIf: !anonymous -->
</div>
</div>
    </div>


                </div>

                
<div>
    
    

    

</div>

                
            
        </div>
    </div>

    <div class="left-sidebar-bg"></div>
</div>

    <div class="aa-backtop-box"><div class="aa-backtop-box-i"><b title="跳到页面顶部" style="opacity: 0; display: none;"><i class="fa fa-chevron-up"></i></b></div></div></div><!-- .inner -->
    

    

</div><!-- .main -->
    
         
<div class="footer-v2">
    <div class="inner">
        <div class="ft-navs">
            <ul class="ft-links ft-lang-switch">
                
                    <li data-lang="en">
                        <a>English</a>
                    </li>
                
                    <li data-lang="jp">
                        <a>日本語</a>
                    </li>
                
                    <li data-lang="kr">
                        <a>한국어</a>
                    </li>
                
                    <li data-lang="cn" class="current">
                        <a>中文(简体)</a>
                    </li>
                
                    <li data-lang="ru">
                        <a>Русский</a>
                    </li>
                
                    <li data-lang="fr">
                        <a>Français</a>
                    </li>
                
                    <li data-lang="de">
                        <a>Deutsch</a>
                    </li>
                </ul>
        </div>

        <div class="ft-misc clearfix">
            <div class="pull-left">
                <ul class="ft-links">
                    <li>© 2019 App Annie</li>
                    <li><a href="/">About App Annie</a></li>
                    <li><a href="https://support.appannie.com/">Support</a></li>
                    <li><a href="https://support.appannie.com/hc/en-us/categories/360000842233-API-V1-3?_ref=footer">API</a></li>
                    <li><a href="/legal/security/?_ref=footer">安全</a></li>
                    <li><a href="/legal/data-usage-policy/?_ref=footer">数据使用政策</a></li>
                    <li><a href="/legal/copyright/?_ref=footer">版权声明</a></li>
                    <li><a href="/legal/terms/?_ref=footer">使用条款</a></li>
                    <li><a href="/legal/privacy/?_ref=footer">隐私政策</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>
 
    
</div><!-- #sub-container -->

<div id="overlay" style="display: none;"></div>

<script>
    var pageVal = pageVal || {};
    pageVal.user = pageVal.user || {};
    
        pageVal.user.id = '1664130';
        pageVal.user.eid = '57cb3405996e76601f8c07d0c055b1ac';
        pageVal.user.email = '583551648@qq.com';
        pageVal.user.flags = {"is_connect_user": false, "is_int_user": false, "has_accounts": false, "is_WalkMe1": false};
        pageVal.user.flags.is_safe_domain = false;
        pageVal.user.flags.has_historical_ss_data = false;
        pageVal.user.date_joined = '2019-05-29';
        pageVal.user.flags.is_snsBeta = false;
        pageVal.user.is_send_report_whitelist_user = false;

        pageVal.user_info = {"company_super_admin_info": {}, "has_historical_ss_data": false, "whitelist": {"labs_aql_explorer": true, "ss_timeline": false, "connect_universal_dashboard": true, "CONNECT_NEW_WORKFLOW": true, "city_level_usage_p2": true, "insights_generator": true, "google_prompt_curl_api": false, "labs_headlines": false, "SPARK_ALERTS_REDUCE_NOISE": true, "downloads_attribution": true, "INT_MKT_FB_CREATIVES_ONLY": true, "labs_monetization_metrics": true, "homepage_alerts": false, "scheduled_emails_v2": true, "INT_MKT_INSTAGRAM": false, "labs_correlated_metrics": true, "donut_chart": true, "sdk_reports": true, "test_new_pricing_model": true, "connect_ad_migration": false, "labs_quadrant": true, "Creative_Countries_Seen_In": true, "connect_plus": true, "labs_auto_alerts": true, "store_single_app_new": true, "mobile_web": true, "IW_ADVERTISERS_CPI_WHITE_LIST": false, "iw_advertisers_cpi": false, "city_level_usage": true, "non_app_install_ads": true, "platform_benchmark": false, "ratings_over_time": true, "PAUSE_SENDING_DELETE_USER_EMAIL": false, "table_heatmap": true, "comparator_v1": false, "comparator_v2": true, "lab_advance_search": true, "SPARK_ALERTS_INSIGHTS_FEED_DETAILS": false, "Cross_App_Usage_Android_Countries": true, "city_user_info_call": false, "internal-show-appid": false, "lab_city_level_usage": false, "lab_country_comparator": true, "report_export_skip_limit_check": false, "NEWPRICING_FREE_PRODUCT": false, "labs_new_homepage": false, "walkme_resource_menu": false, "alerts_insights_feed_details": false, "SPARK_LIVE_SEARCH": true, "branding_v2": false, "featured_games_reports": true, "labs": true, "table_multibreakdown": false, "lab_attribute_search": true, "IOS11_FEATURED_STORY": true, "sso": true, "chart_multimetrics": false, "labs_paid_organic_downloads": false, "INT Hourly Rank API": false, "SPARK_ALERTS_AQL": true, "ASO Parallelism": false, "comparator_country_breakdown": false, "SS_Supernova": true}, "is_int_user": false, "is_int_api_user": false, "is_an_user": false, "is_to_be_invited_user": false, "free_customer_profile": {"category_gp": [{"is_locked": true, "name": "\u6240\u6709\u7c7b\u522b", "value": 400000, "legacy_value": 1}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "5 \u5c81\u53ca\u4ee5\u4e0b", "value": 400063, "legacy_value": 57}, {"is_locked": true, "name": "6-8 \u5c81", "value": 400064, "legacy_value": 58}, {"is_locked": true, "name": "9 \u5c81\u53ca\u4ee5\u4e0a", "value": 400065, "legacy_value": 59}, {"is_locked": true, "name": "\u521b\u610f\u6e38\u620f", "value": 400067, "legacy_value": 62}, {"is_locked": true, "name": "\u52a8\u4f5c\u4e0e\u5192\u9669", "value": 400062, "legacy_value": 60}, {"is_locked": true, "name": "\u89d2\u8272\u626e\u6f14", "value": 400070, "legacy_value": 65}, {"is_locked": true, "name": "\u6559\u80b2", "value": 400068, "legacy_value": 63}, {"is_locked": true, "name": "\u97f3\u4e50\u548c\u89c6\u9891", "value": 400069, "legacy_value": 64}, {"is_locked": true, "name": "\u667a\u529b\u6e38\u620f", "value": 400066, "legacy_value": 61}], "name": "\u5bb6\u5ead\u6e38\u620f", "value": 400061, "legacy_value": 56}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "\u8d22\u52a1", "value": 400038, "legacy_value": 18}, {"is_locked": true, "name": "\u9910\u996e\u7f8e\u98df", "value": 400039, "legacy_value": 73}, {"is_locked": true, "name": "\u8f66\u8f86\u548c\u4ea4\u901a", "value": 400028, "legacy_value": 69}, {"is_locked": true, "name": "\u5730\u56fe\u548c\u5bfc\u822a", "value": 400045, "legacy_value": 34}, {"is_locked": true, "name": "\u52a8\u6f2b", "value": 400032, "legacy_value": 14}, {"is_locked": true, "name": "\u52a8\u6001\u58c1\u7eb8", "value": 400044, "legacy_value": 22}, {"is_locked": true, "name": "\u4e2a\u6027\u5316", "value": 400050, "legacy_value": 27}, {"is_locked": true, "name": "\u5de5\u5177", "value": 400056, "legacy_value": 33}, {"is_locked": true, "name": "\u8d2d\u7269", "value": 400053, "legacy_value": 30}, {"is_locked": true, "name": "\u6d3b\u52a8", "value": 400037, "legacy_value": 72}, {"is_locked": true, "name": "\u5bb6\u5c45\u88c5\u4fee", "value": 400041, "legacy_value": 68}, {"is_locked": true, "name": "\u5065\u5eb7\u4e0e\u5065\u8eab", "value": 400040, "legacy_value": 19}, {"is_locked": true, "name": "\u6559\u80b2", "value": 400035, "legacy_value": 16}, {"is_locked": true, "name": "\u65c5\u6e38\u4e0e\u672c\u5730\u51fa\u884c", "value": 400057, "legacy_value": 35}, {"is_locked": true, "name": "\u7f8e\u5bb9\u65f6\u5c1a", "value": 400029, "legacy_value": 70}, {"is_locked": true, "name": "\u8f6f\u4ef6\u4e0e\u6f14\u793a", "value": 400042, "legacy_value": 20}, {"is_locked": true, "name": "\u5546\u4e1a", "value": 400031, "legacy_value": 13}, {"is_locked": true, "name": "\u793e\u4ea4", "value": 400054, "legacy_value": 31}, {"is_locked": true, "name": "\u793e\u4ea4\u7ea6\u4f1a", "value": 400034, "legacy_value": 71}, {"is_locked": true, "name": "\u6444\u5f71", "value": 400051, "legacy_value": 28}, {"is_locked": true, "name": "\u751f\u6d3b", "value": 400043, "legacy_value": 21}, {"is_locked": true, "name": "\u89c6\u9891\u64ad\u653e\u548c\u7f16\u8f91", "value": 400058, "legacy_value": 23}, {"is_locked": true, "name": "\u4f53\u80b2", "value": 400055, "legacy_value": 32}, {"is_locked": true, "name": "\u5929\u6c14", "value": 400059, "legacy_value": 36}, {"is_locked": true, "name": "\u901a\u8baf", "value": 400033, "legacy_value": 15}, {"is_locked": true, "name": "\u56fe\u4e66\u4e0e\u5de5\u5177\u4e66", "value": 400030, "legacy_value": 12}, {"is_locked": true, "name": "\u5c0f\u90e8\u4ef6", "value": 400060, "legacy_value": 37}, {"is_locked": true, "name": "\u6548\u7387", "value": 400052, "legacy_value": 29}, {"is_locked": true, "name": "\u65b0\u95fb\u6742\u5fd7", "value": 400048, "legacy_value": 26}, {"is_locked": true, "name": "\u533b\u7597", "value": 400046, "legacy_value": 24}, {"is_locked": true, "name": "\u827a\u672f\u548c\u8bbe\u8ba1", "value": 400027, "legacy_value": 67}, {"is_locked": true, "name": "\u97f3\u4e50\u4e0e\u97f3\u9891", "value": 400047, "legacy_value": 25}, {"is_locked": true, "name": "\u5a31\u4e50", "value": 400036, "legacy_value": 17}, {"is_locked": true, "name": "\u80b2\u513f", "value": 400049, "legacy_value": 75}, {"is_locked": true, "name": "Android Wear", "value": 400026, "legacy_value": 66}], "name": "\u5e94\u7528", "value": 400025, "legacy_value": 11}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "\u7b56\u7565\u6e38\u620f", "value": 400018, "legacy_value": 54}, {"is_locked": true, "name": "\u52a8\u6001\u58c1\u7eb8", "value": 400011, "legacy_value": 7}, {"is_locked": true, "name": "\u52a8\u4f5c\u6e38\u620f", "value": 400002, "legacy_value": 38}, {"is_locked": true, "name": "\u5bb6\u5ead\u6e38\u620f", "value": 400010, "legacy_value": 47}, {"is_locked": true, "name": "\u89d2\u8272\u626e\u6f14\u6e38\u620f", "value": 400015, "legacy_value": 51}, {"is_locked": true, "name": "\u6559\u80b2", "value": 400009, "legacy_value": 46}, {"is_locked": true, "name": "\u8857\u673a\u548c\u52a8\u4f5c", "value": 400022, "legacy_value": 3}, {"is_locked": true, "name": "\u8857\u673a\u6e38\u620f", "value": 400004, "legacy_value": 41}, {"is_locked": true, "name": "\u6a21\u62df\u6e38\u620f", "value": 400016, "legacy_value": 52}, {"is_locked": true, "name": "\u6251\u514b\u724c\u6e38\u620f ", "value": 400006, "legacy_value": 43}, {"is_locked": true, "name": "\u8d5b\u8f66\u6e38\u620f", "value": 400014, "legacy_value": 8}, {"is_locked": true, "name": "\u63a2\u9669\u6e38\u620f", "value": 400003, "legacy_value": 39}, {"is_locked": true, "name": "\u4f53\u80b2", "value": 400017, "legacy_value": 9}, {"is_locked": true, "name": "\u6587\u5b57\u6e38\u620f", "value": 400021, "legacy_value": 40}, {"is_locked": true, "name": "\u5c0f\u90e8\u4ef6", "value": 400020, "legacy_value": 10}, {"is_locked": true, "name": "\u5c0f\u6e38\u620f", "value": 400019, "legacy_value": 55}, {"is_locked": true, "name": "\u4f11\u95f2", "value": 400008, "legacy_value": 6}, {"is_locked": true, "name": "\u76ca\u667a\u548c\u89e3\u8c1c", "value": 400023, "legacy_value": 4}, {"is_locked": true, "name": "\u97f3\u4e50", "value": 400012, "legacy_value": 48}, {"is_locked": true, "name": "\u5a31\u4e50\u573a\u6e38\u620f", "value": 400007, "legacy_value": 44}, {"is_locked": true, "name": "\u7eb8\u724c\u548c\u8d4c\u535a", "value": 400024, "legacy_value": 5}, {"is_locked": true, "name": "\u667a\u529b\u6e38\u620f", "value": 400013, "legacy_value": 49}, {"is_locked": true, "name": "\u684c\u9762\u6e38\u620f", "value": 400005, "legacy_value": 42}], "name": "\u6e38\u620f", "value": 400001, "legacy_value": 2}], "category_ios": [{"is_locked": true, "name": "\u6240\u6709\u7c7b\u522b", "value": 100000, "legacy_value": 36}, {"is_locked": true, "name": "\u62a5\u520a\u6742\u5fd7", "value": 100035, "legacy_value": 6021}, {"is_locked": true, "name": "\u8d22\u52a1", "value": 100027, "legacy_value": 6015}, {"is_locked": true, "name": "\u53c2\u8003", "value": 100070, "legacy_value": 6006}, {"is_locked": true, "name": "\u5bfc\u822a", "value": 100066, "legacy_value": 6010}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "5 \u5c81\u53ca\u4ee5\u4e0b", "value": 100031, "legacy_value": 361}, {"is_locked": true, "name": "6-8 \u5c81", "value": 100032, "legacy_value": 362}, {"is_locked": true, "name": "9-11 \u5c81", "value": 100033, "legacy_value": 363}], "name": "\u513f\u7ae5", "value": 100030, "legacy_value": 360}, {"is_locked": true, "name": "\u5de5\u5177", "value": 100076, "legacy_value": 6002}, {"is_locked": true, "name": "\u8d2d\u7269", "value": 100071, "legacy_value": 6024}, {"is_locked": true, "name": "\u5065\u5eb7\u5065\u7f8e", "value": 100029, "legacy_value": 6013}, {"is_locked": true, "name": "\u6559\u80b2", "value": 100025, "legacy_value": 6017}, {"is_locked": true, "name": "\u65c5\u884c", "value": 100075, "legacy_value": 6003}, {"is_locked": true, "name": "\u7f8e\u98df\u4f73\u996e", "value": 100028, "legacy_value": 6023}, {"is_locked": true, "name": "\u5546\u54c1\u6307\u5357", "value": 100024, "legacy_value": 6022}, {"is_locked": true, "name": "\u5546\u4e1a", "value": 100023, "legacy_value": 6000}, {"is_locked": true, "name": "\u793e\u4ea4", "value": 100072, "legacy_value": 6005}, {"is_locked": true, "name": "\u6444\u5f71\u4e0e\u5f55\u50cf", "value": 100068, "legacy_value": 6008}, {"is_locked": true, "name": "\u751f\u6d3b", "value": 100034, "legacy_value": 6012}, {"is_locked": true, "name": "\u4f53\u80b2", "value": 100073, "legacy_value": 6004}, {"is_locked": true, "name": "\u5929\u6c14", "value": 100077, "legacy_value": 6001}, {"is_locked": true, "name": "\u56fe\u4e66", "value": 100022, "legacy_value": 6018}, {"is_locked": true, "name": "\u6548\u7387", "value": 100069, "legacy_value": 6007}, {"is_locked": true, "name": "\u65b0\u95fb", "value": 100067, "legacy_value": 6009}, {"is_locked": true, "name": "\u533b\u7597", "value": 100064, "legacy_value": 6020}, {"is_locked": true, "name": "\u97f3\u4e50", "value": 100065, "legacy_value": 6011}, {"is_locked": true, "name": "\u5e94\u7528", "value": 100021, "legacy_value": 100}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "\u7b56\u7565\u6e38\u620f", "value": 100018, "legacy_value": 7017}, {"is_locked": true, "name": "\u52a8\u4f5c\u6e38\u620f", "value": 100002, "legacy_value": 7001}, {"is_locked": true, "name": "\u513f\u7ae5", "value": 100011, "legacy_value": 7010}, {"is_locked": true, "name": "\u5bb6\u5ead\u6e38\u620f", "value": 100010, "legacy_value": 7009}, {"is_locked": true, "name": "\u89d2\u8272\u626e\u6f14\u6e38\u620f", "value": 100015, "legacy_value": 7014}, {"is_locked": true, "name": "\u6559\u80b2", "value": 100009, "legacy_value": 7008}, {"is_locked": true, "name": "\u8857\u673a\u6e38\u620f", "value": 100004, "legacy_value": 7003}, {"is_locked": true, "name": "\u6a21\u62df\u6e38\u620f", "value": 100016, "legacy_value": 7015}, {"is_locked": true, "name": "\u6251\u514b\u724c\u6e38\u620f ", "value": 100006, "legacy_value": 7005}, {"is_locked": true, "name": "\u8d5b\u8f66\u6e38\u620f", "value": 100014, "legacy_value": 7013}, {"is_locked": true, "name": "\u63a2\u9669\u6e38\u620f", "value": 100003, "legacy_value": 7002}, {"is_locked": true, "name": "\u4f53\u80b2", "value": 100017, "legacy_value": 7016}, {"is_locked": true, "name": "\u9ab0\u5b50\u6e38\u620f", "value": 100008, "legacy_value": 7007}, {"is_locked": true, "name": "\u6587\u5b57\u6e38\u620f", "value": 100020, "legacy_value": 7019}, {"is_locked": true, "name": "\u5c0f\u6e38\u620f", "value": 100019, "legacy_value": 7018}, {"is_locked": true, "name": "\u97f3\u4e50", "value": 100012, "legacy_value": 7011}, {"is_locked": true, "name": "\u5a31\u4e50\u573a\u6e38\u620f", "value": 100007, "legacy_value": 7006}, {"is_locked": true, "name": "\u667a\u529b\u6e38\u620f", "value": 100013, "legacy_value": 7012}, {"is_locked": true, "name": "\u684c\u9762\u6e38\u620f", "value": 100005, "legacy_value": 7004}], "name": "\u6e38\u620f", "value": 100001, "legacy_value": 6014}, {"is_locked": true, "name": "\u5a31\u4e50", "value": 100026, "legacy_value": 6016}], "category_unified": [{"is_locked": true, "name": "\u6240\u6709\u7c7b\u522b", "value": 800000, "legacy_value": 600}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "5 \u5c81\u53ca\u4ee5\u4e0b", "value": 800042, "legacy_value": 901}, {"is_locked": true, "name": "6-8 \u5c81", "value": 800043, "legacy_value": 902}, {"is_locked": true, "name": "9 \u5c81\u53ca\u4ee5\u4e0a", "value": 800044, "legacy_value": 903}], "name": "\u513f\u7ae5\u4e0e\u5bb6\u5ead", "value": 800041, "legacy_value": 707}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "\u8d22\u52a1", "value": 800023, "legacy_value": 705}, {"is_locked": true, "name": "\u9910\u996e\u7f8e\u98df", "value": 800024, "legacy_value": 721}, {"is_locked": true, "name": "\u52a8\u6001\u58c1\u7eb8", "value": 800027, "legacy_value": 722}, {"is_locked": true, "name": "\u5de5\u5177", "value": 800036, "legacy_value": 718}, {"is_locked": true, "name": "\u8d2d\u7269", "value": 800033, "legacy_value": 715}, {"is_locked": true, "name": "\u5065\u5eb7\u4e0e\u5065\u8eab", "value": 800025, "legacy_value": 706}, {"is_locked": true, "name": "\u6559\u80b2", "value": 800021, "legacy_value": 703}, {"is_locked": true, "name": "\u53ef\u7a7f\u6234\u5f0f\u8bbe\u5907", "value": 800039, "legacy_value": 711}, {"is_locked": true, "name": "\u65c5\u6e38\u53ca\u5bfc\u822a", "value": 800037, "legacy_value": 719}, {"is_locked": true, "name": "\u5546\u4e1a", "value": 800020, "legacy_value": 702}, {"is_locked": true, "name": "\u793e\u4ea4", "value": 800034, "legacy_value": 716}, {"is_locked": true, "name": "\u751f\u6d3b", "value": 800026, "legacy_value": 708}, {"is_locked": true, "name": "\u4f53\u80b2", "value": 800035, "legacy_value": 717}, {"is_locked": true, "name": "\u5929\u6c14", "value": 800038, "legacy_value": 720}, {"is_locked": true, "name": "\u56fe\u4e66\u4e0e\u5de5\u5177\u4e66", "value": 800019, "legacy_value": 701}, {"is_locked": true, "name": "\u5c0f\u90e8\u4ef6", "value": 800040, "legacy_value": 723}, {"is_locked": true, "name": "\u6548\u7387", "value": 800032, "legacy_value": 714}, {"is_locked": true, "name": "\u65b0\u95fb\u6742\u5fd7", "value": 800030, "legacy_value": 712}, {"is_locked": true, "name": "\u533b\u7597", "value": 800028, "legacy_value": 709}, {"is_locked": true, "name": "\u97f3\u4e50", "value": 800029, "legacy_value": 710}, {"is_locked": true, "name": "\u5a31\u4e50", "value": 800022, "legacy_value": 704}, {"is_locked": true, "name": "\u7167\u7247\u4e0e\u89c6\u9891", "value": 800031, "legacy_value": 713}], "name": "\u5e94\u7528", "value": 800018, "legacy_value": 602}, {"is_locked": true, "sub_categories": [{"is_locked": true, "name": "\u52a8\u6001\u58c1\u7eb8", "value": 800009, "legacy_value": 816}, {"is_locked": true, "name": "\u513f\u7ae5\u4e0e\u5bb6\u5ead", "value": 800008, "legacy_value": 806}, {"is_locked": true, "name": "\u89d2\u8272\u626e\u6f14\u53ca\u7b56\u7565\u6e38\u620f", "value": 800012, "legacy_value": 810}, {"is_locked": true, "name": "\u6559\u80b2", "value": 800007, "legacy_value": 805}, {"is_locked": true, "name": "\u8857\u673a\u548c\u52a8\u4f5c", "value": 800002, "legacy_value": 801}, {"is_locked": true, "name": "\u6a21\u62df\u6e38\u620f", "value": 800013, "legacy_value": 811}, {"is_locked": true, "name": "\u8d5b\u8f66\u6e38\u620f", "value": 800011, "legacy_value": 809}, {"is_locked": true, "name": "\u63a2\u9669\u6e38\u620f", "value": 800003, "legacy_value": 802}, {"is_locked": true, "name": "\u4f53\u80b2", "value": 800014, "legacy_value": 812}, {"is_locked": true, "name": "\u6587\u5b57\u6e38\u620f", "value": 800016, "legacy_value": 814}, {"is_locked": true, "name": "\u5c0f\u90e8\u4ef6", "value": 800017, "legacy_value": 815}, {"is_locked": true, "name": "\u5c0f\u6e38\u620f", "value": 800015, "legacy_value": 813}, {"is_locked": true, "name": "\u76ca\u667a\u548c\u89e3\u8c1c", "value": 800005, "legacy_value": 808}, {"is_locked": true, "name": "\u97f3\u4e50", "value": 800010, "legacy_value": 807}, {"is_locked": true, "name": "\u7eb8\u724c\u548c\u8d4c\u535a", "value": 800006, "legacy_value": 804}, {"is_locked": true, "name": "\u684c\u9762\u6e38\u620f", "value": 800004, "legacy_value": 803}], "name": "\u6e38\u620f", "value": 800001, "legacy_value": 601}]}, "is_free_user": true, "is_ip_from_china": false, "is_int_web_user": false};

    
</script>



<script>
aaTrack=function(){var e={},f=[],k=0,h=function(){if(arguments[0]){var a=arguments[0],g=[].slice.call(arguments,1);500>k?(f.push([a,g]),k++):(f.shift(),f.push([a,g]));if(e[a])for(var a=e[a],b=a.length,c=0;c<b;c++)a[c].apply(null,g)}};h.register=function(a,g){a:if("object"==typeof a)for(var b in a){var c=a[b];if(e[b])for(var d=e[b],k=d.length,l=0;l<k;l++){if(d[l]==c)break a}else e[b]=[];e[b].push(c)}if(g)for(var h in a)for(b=a[h],c=f.length,d=0;d<c;d++)f[d][0]==h&&b.apply(null,f[d][1])};return h}();
</script>
<script type="text/javascript" data-tk="pre_install">
  var _mkto = _mkto || [];

  aaTrack('set', {
      'env': 'production',
      'pageType': 'product'
  });

  (function() {
    var _tracker = [];
    tracker = function(item) { _tracker.push(item); }; tracker.pool = _tracker;
  })();
</script>


    <!-- Google Tag Manager -->
<noscript>&lt;iframe src="//www.googletagmanager.com/ns.html?id=GTM-D44H" height="0" width="0" style="display:none;visibility:hidden"&gt;&lt;/iframe&gt;</noscript>
<script>
!function(w,d,l,i){function go(){!function(w,d,s,l,i){w[l]=w[l]||[],w[l].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl="dataLayer"!=l?"&l="+l:"";j.async=!0,j.src="//www.googletagmanager.com/gtm.js?id="+i+dl,f.parentNode.insertBefore(j,f)}(window,document,"script",l,i)}l="dataLayer_"+i.replace("GTM-",""),lo=w[l]||(w[l]=[]),aaTrack.register({set:function(obj){lo.push(obj)}},!0),w.addEventListener?w.addEventListener("load",go,!1):w.attachEvent?w.attachEvent("onload",go):setTimeout(go,100)}(window,document,"","GTM-D44H");
</script>

    
    


<script type="text/javascript" data-tk="track_on_every_page" data-tk-com="gp">
    aaTrack('set', {
        'Interface Language': 'cn',
        'Page Type': 'Web Prod'
    });

    
        
        aaTrack('set', {
            'displayName': 'Xia Weiliang',
            'email': '583551648@qq.com',
            'eid': '57cb3405996e76601f8c07d0c055b1ac',
            'uid': '1664130',
            'is_int_user':  'no' ,
            'is_connect_user':  'no' ,
            'account_type':  'basic' ,
            'admin_status':   'user'  ,
            'activation_time': '2019-05-29 19:28:01.224562',
            'job_function': 'Other',
            'registration_date': '2019-05-29 19:27:12.064903',
            'days_since_registered': 0,
            'first_name': 'Xia',
            'walkme_resource_menu':  false ,
        });
    

    
        try {
            tracker(['identify', 1664130, {
                email: '583551648@qq.com',
                $mktoHash: 'bf82b64b00c5eaaae522779ffc11246f329b2617'
            }]);
        } catch (ex) {
        }
        
    
    // set all logs to ga
    
    try {
        tracker(['page']);
    } catch (ex) {
    }
</script>


</div>

<script>
/* quick $ step 2/3 */
window.$ = window.jQuery = undefined;
</script>
<script src="https://static-s.aa-cdn.net/media/javascript/_lang/zh-cn/django/all.v-00467e-20e038.js"></script>


    
        <!--[if lt IE 9]>
        <script type="text/javascript" src="https://static-s.aa-cdn.net/media/javascript/lib/browser-support/excanvas.canvas.text.js" crossorigin="anonymous"></script>
        <![endif]-->
        <script src="https://static-s.aa-cdn.net/media/javascript/c/prod.min.v-3b6e96ba.js" crossorigin="anonymous"></script><div class="live-search-list header-live-search" style="display: none;"><div class="loading-container"><i class="icon-loading fa fa-spinner fa-spin"></i></div><div class="content"></div></div>
<script src="https://static-s.aa-cdn.net/media/lib/ng-v1.5.5/i18n/angular-locale_zh-cn.v-9dcded23.js" crossorigin="anonymous"></script>
        
    


<script>
/* quick $ step 3/3 */
(function(fns, $) {
  if (!fns || fns.length < 1) { return; }
  var i = 0, l = fns.length;
  for (; i < l; ++i) {
    $(fns[i]);
  }
  fns.length = 0;
})(__aa_fns, jQuery);


</script>

<script>/* JIRA:XP-793 */
(function(a,e,n,r){try{if(!a||!e)return;n=e.host;if(n.match(/localhost|\.appannie\.(dev|com)/))return;r=n.replace(/www\./,"blog.");if(n===r)return;a('a[href*="blog.appannie.com"]').each(function(e,n){var o=a(n).attr("href").replace(/blog\.appannie\.com($|[?\/])/,r+"$1");a(n).attr("href",o)})}catch(o){}})(window.jQuery,window.location);
</script>


    
    <script>
        var pageVal = $.extend(pageVal || {}, {
        vertical: 'apps',
        market: 'ios',
        filters: ["version", "country", "rating", "date"],
        page: 'Reviews',
        canDownloadCSV: false,
        product_slug: 'idle-heroes',
        review_translate_lang: '',

        
        filterSettings: {
            
            'version': {"context": [["", "\u6240\u6709\u7248\u672c"], ["1.22.0", "1.22.0"], ["1.21.0", "1.21.0"], ["1.20.0", "1.20.0"], ["1.19.0", "1.19.0"], ["1.18.0", "1.18.0"], ["1.16.299", "1.16.299"], ["1.16.0", "1.16.0"], ["1.15.0", "1.15.0"], ["1.14.0", "1.14.0"], ["1.13.0", "1.13.0"], ["1.9.0", "1.9.0"], ["1.8.0", "1.8.0"], ["1.6.0", "1.6.0"], ["1.5.0", "1.5.0"], ["1.4.0", "1.4.0"], ["1.2.0", "1.2.0"], ["1.1.0", "1.1.0"], ["1.0.0", "1.0.0"], ["Unknown", "Unknown"]], "defaults": ""},
            
            
            'country': {"context": {"items": [[null, "\u5168\u90e8", [["", "\u5168\u90e8"], ["CN", "\u4e2d\u56fd"], ["DK", "\u4e39\u9ea6"], ["UA", "\u4e4c\u514b\u5170"], ["UZ", "\u4e4c\u5179\u522b\u514b\u65af\u5766"], ["UY", "\u4e4c\u62c9\u572d"], ["AM", "\u4e9a\u7f8e\u5c3c\u4e9a"], ["IL", "\u4ee5\u8272\u5217"], ["RU", "\u4fc4\u7f57\u65af"], ["BG", "\u4fdd\u52a0\u5229\u4e9a"], ["HR", "\u514b\u7f57\u5730\u4e9a"], ["IS", "\u51b0\u5c9b"], ["CA", "\u52a0\u62ff\u5927"], ["GH", "\u52a0\u7eb3"], ["HU", "\u5308\u7259\u5229"], ["ZA", "\u5357\u975e"], ["QA", "\u5361\u5854\u5c14"], ["LU", "\u5362\u68ee\u5821"], ["IN", "\u5370\u5ea6"], ["ID", "\u5370\u5ea6\u5c3c\u897f\u4e9a"], ["GT", "\u5371\u5730\u9a6c\u62c9"], ["EC", "\u5384\u74dc\u591a\u5c14"], ["TW", "\u53f0\u6e7e"], ["KZ", "\u54c8\u8428\u514b\u65af\u5766"], ["CO", "\u54e5\u4f26\u6bd4\u4e9a"], ["CR", "\u54e5\u65af\u8fbe\u9ece\u52a0"], ["TR", "\u571f\u8033\u5176"], ["LC", "\u5723\u5362\u897f\u4e9a"], ["GY", "\u572d\u4e9a\u90a3"], ["EG", "\u57c3\u53ca"], ["CY", "\u585e\u6d66\u8def\u65af"], ["MX", "\u58a8\u897f\u54e5"], ["DO", "\u591a\u7c73\u5c3c\u52a0\u5171\u548c\u56fd"], ["AT", "\u5965\u5730\u5229"], ["VE", "\u59d4\u5185\u745e\u62c9"], ["AO", "\u5b89\u54e5\u62c9"], ["NP", "\u5c3c\u6cca\u5c14"], ["PK", "\u5df4\u57fa\u65af\u5766"], ["BB", "\u5df4\u5df4\u591a\u65af"], ["PY", "\u5df4\u62c9\u572d"], ["PA", "\u5df4\u62ff\u9a6c"], ["BH", "\u5df4\u6797"], ["BR", "\u5df4\u897f"], ["GR", "\u5e0c\u814a"], ["DE", "\u5fb7\u56fd"], ["IT", "\u610f\u5927\u5229"], ["LV", "\u62c9\u8131\u7ef4\u4e9a"], ["NO", "\u632a\u5a01"], ["CZ", "\u6377\u514b\u5171\u548c\u56fd"], ["MD", "\u6469\u5c14\u591a\u74e6"], ["BN", "\u6587\u83b1"], ["SK", "\u65af\u6d1b\u4f10\u514b"], ["SI", "\u65af\u6d1b\u6587\u5c3c\u4e9a"], ["LK", "\u65af\u91cc\u5170\u5361"], ["SG", "\u65b0\u52a0\u5761"], ["NZ", "\u65b0\u897f\u5170"], ["JP", "\u65e5\u672c"], ["CL", "\u667a\u5229"], ["KH", "\u67ec\u57d4\u5be8"], ["BE", "\u6bd4\u5229\u65f6"], ["SA", "\u6c99\u7279\u963f\u62c9\u4f2f"], ["FR", "\u6cd5\u56fd"], ["PL", "\u6ce2\u5170"], ["TH", "\u6cf0\u56fd"], ["AU", "\u6fb3\u5927\u5229\u4e9a"], ["MO", "\u6fb3\u95e8"], ["IE", "\u7231\u5c14\u5170"], ["EE", "\u7231\u6c99\u5c3c\u4e9a"], ["SE", "\u745e\u5178"], ["CH", "\u745e\u58eb"], ["BY", "\u767d\u4fc4\u7f57\u65af"], ["KW", "\u79d1\u5a01\u7279"], ["PE", "\u79d8\u9c81"], ["TN", "\u7a81\u5c3c\u65af"], ["LT", "\u7acb\u9676\u5b9b"], ["JO", "\u7ea6\u65e6"], ["NA", "\u7eb3\u7c73\u6bd4\u4e9a"], ["RO", "\u7f57\u9a6c\u5c3c\u4e9a"], ["US", "\u7f8e\u56fd"], ["LA", "\u8001\u631d"], ["FI", "\u82ac\u5170"], ["GB", "\u82f1\u56fd"], ["NL", "\u8377\u5170"], ["PH", "\u83f2\u5f8b\u5bbe"], ["SV", "\u8428\u5c14\u74e6\u591a"], ["PT", "\u8461\u8404\u7259"], ["MN", "\u8499\u53e4"], ["ES", "\u897f\u73ed\u7259"], ["VN", "\u8d8a\u5357"], ["AZ", "\u963f\u585e\u62dc\u7586"], ["AL", "\u963f\u5c14\u5df4\u5c3c\u4e9a"], ["AR", "\u963f\u6839\u5ef7"], ["AE", "\u963f\u8054\u914b"], ["KR", "\u97e9\u56fd"], ["HK", "\u9999\u6e2f"], ["MK", "\u9a6c\u5176\u987f"], ["MY", "\u9a6c\u6765\u897f\u4e9a"], ["LB", "\u9ece\u5df4\u5ae9"]]]]}, "defaults": ""},
            
            
            'rating': {"context": [["", "\u6240\u6709\u8bc4\u7ea7"], ["GOOD", "\u597d\u8bc4"], ["BAD", "\u5dee\u8bc4"], [5, "5\u661f "], [4, "4\u661f "], [3, "3\u661f "], [2, "2\u661f "], [1, "1\u661f "]], "defaults": ""},
            'date': {"context": {"max_date": "2019-05-30", "min_date": "2016-11-10"}, "defaults": "2019-04-29~2019-05-29"},
            'search': {
                'value': ''
            }
        },
        'permission_check_code': "PERMISSION_NOT_PASS"
    });
    </script>
    


<script>
    var pageVal = pageVal || {};
    pageVal.account_id = '';
    pageVal.market_name = 'ios'
    pageVal.app_id =  '1153461915' 
    pageVal.is_shared = true;
    pageVal.vertical = 'apps';
    pageVal.is_demo = false;
    
        pageVal.meta_data = {"status": "Alive", "required_device": "\u901a\u7528", "app_market_cssid": "itc", "name": "\u653e\u7f6e\u5947\u5175 -\u5168\u7403\u540c\u670d\u653e\u7f6e\u7c7b\u6e38\u620f", "allow_add_to_groups": true, "universal_company_info": {}, "price": 0.0, "is_int_user": false, "universal_company_name": "DH Games", "current_url": "/apps/ios/app/idle-heroes/reviews/", "app_market_url": "https://itunes.apple.com/app/id1153461915", "is_show_device": false, "sharing_url": "", "franchise_info": {"count": "0 \u6b3eApp", "is_sensitive": false, "id": "app_franchise", "url": null, "name": "N/A"}, "app_market_name": "iOS Store", "category_name": "\u6e38\u620f", "type": "APP", "id": 1153461915, "market": "ios", "icon": "https://static-s.aa-cdn.net/img/ios/1153461915/aa30950d6ed749535d6b39dad5447d7a"};
    
    pageVal.sideBarMenus = [{"is_new": false, "is_current": false, "id": "basic", "icon": "", "target": "", "is_locked": false, "items": [{"is_new": false, "is_current": false, "id": "details", "icon": "", "target": "", "is_locked": false, "items": [], "label": "App\u8be6\u7ec6\u4fe1\u606f", "url": "/apps/ios/app/idle-heroes/details/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "intelligence-sdks", "icon": "", "target": "", "is_locked": true, "items": [], "label": "SDK", "url": "/apps/ios/app/1153461915/sdks/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "app-timeline", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u65f6\u95f4\u7ebf", "url": "/apps/ios/app/idle-heroes/timeline/", "connection": false, "is_beta": false, "cls": ""}], "label": "\u4fe1\u606f", "url": "", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "landing", "icon": "", "target": "", "is_locked": false, "items": [{"is_new": false, "is_current": false, "id": "landing", "icon": "", "target": "", "is_locked": false, "items": [], "label": "\u8fde\u63a5", "url": "/apps/ios/app/1153461915/analytics/", "connection": true, "is_beta": false, "cls": ""}], "label": "\u6211\u7684\u5df2\u8fde\u63a5\u5e94\u7528", "url": "", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "rankings", "icon": "", "target": "", "is_locked": false, "items": [{"is_new": false, "is_current": false, "id": "ranks", "icon": "", "target": "", "is_locked": false, "items": [], "label": "\u6bcf\u65e5\u6392\u540d", "url": "/apps/ios/app/idle-heroes/app-ranking/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "rank-history", "icon": "", "target": "", "is_locked": false, "items": [], "label": "\u5386\u53f2\u6392\u540d", "url": "/apps/ios/app/idle-heroes/rank-history/", "connection": false, "is_beta": false, "cls": ""}], "label": "\u5e94\u7528\u5546\u5e97\u6392\u540d", "url": "", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "store_int", "icon": "", "target": "", "is_locked": false, "items": [{"is_new": false, "is_current": false, "id": "store-intelligence", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u4e0b\u8f7d\u91cf\u548c\u6536\u5165", "url": "/apps/ios/app/idle-heroes/intelligence/", "connection": false, "is_beta": false, "cls": ""}], "label": "\u4e0b\u8f7d\u91cf\u548c\u6536\u5165", "url": "", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "usage_int", "icon": "", "target": "", "is_locked": false, "items": [{"is_new": false, "is_current": false, "id": "usage", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u4f7f\u7528\u91cf", "url": "/apps/ios/app/idle-heroes/usage/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "user-retention-app", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u7528\u6237\u7559\u5b58\u7387", "url": "/apps/ios/app/idle-heroes/user-retention/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "intelligence-cross-app-usage", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u8de8\u5e94\u7528/\u7f51\u9875\u4f7f\u7528\u60c5\u51b5", "url": "/apps/ios/app/idle-heroes/intelligence/cross-app-usage/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "intelligence-demographics", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u7528\u6237\u7279\u5f81", "url": "/apps/ios/app/idle-heroes/intelligence/demographics/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": true, "id": "reviews", "icon": "", "target": "", "is_locked": false, "items": [], "label": "\u8bc4\u4ef7", "url": "/apps/ios/app/idle-heroes/reviews/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "ratings", "icon": "", "target": "", "is_locked": false, "items": [], "label": "\u8bc4\u7ea7", "url": "/apps/ios/app/idle-heroes/ratings/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "ratings-over-time", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u968f\u65f6\u95f4\u8bc4\u7ea7", "url": "/apps/ios/app/idle-heroes/ratings-over-time/", "connection": false, "is_beta": false, "cls": ""}], "label": "\u4f7f\u7528\u6a21\u5f0f\u548c\u7528\u6237\u53c2\u4e0e\u5ea6", "url": "", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "user_acq", "icon": "", "target": "", "is_locked": false, "items": [{"is_new": false, "is_current": false, "id": "keywords", "icon": "", "target": "", "is_locked": false, "items": [], "label": "\u5173\u952e\u8bcd (ASO)", "url": "/apps/ios/app/idle-heroes/keywords/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "advanced-app-feature", "icon": "", "target": "", "is_locked": false, "items": [], "label": "\u63a8\u8350", "url": "/apps/ios/app/idle-heroes/featured/", "connection": false, "is_beta": false, "cls": ""}, {"is_new": false, "is_current": false, "id": "marketing-intelligence-app", "icon": "", "target": "", "is_locked": true, "items": [], "label": "\u5e7f\u544a", "url": "/apps/ios/app/idle-heroes/intelligence/marketing/", "connection": false, "is_beta": false, "cls": ""}], "label": "\u7528\u6237\u83b7\u53d6", "url": "", "connection": false, "is_beta": false, "cls": ""}];

pageVal.user_prefer_country = "US";
pageVal.user_prefer_tzone = "PST8PDT";


 pageVal.countries = [{"name": "\u963f\u5c14\u5df4\u5c3c\u4e9a", "code": "AL", "slug": "albania", "tzone": "Europe/Tirane", "sid": 143575}, {"name": "\u963f\u5c14\u53ca\u5229\u4e9a", "code": "DZ", "slug": "algeria", "tzone": "Africa/Algiers", "sid": 143563}, {"name": "\u5b89\u54e5\u62c9", "code": "AO", "slug": "angola", "tzone": "Africa/Luanda", "sid": 143564}, {"name": "\u5b89\u572d\u62c9", "code": "AI", "slug": "anguilla", "tzone": "America/Anguilla", "sid": 143538}, {"name": "\u5b89\u63d0\u74dc\u548c\u5df4\u5e03\u8fbe", "code": "AG", "slug": "antigua-and-barbuda", "tzone": "America/Antigua", "sid": 143540}, {"name": "\u963f\u6839\u5ef7", "code": "AR", "slug": "argentina", "tzone": "America/Argentina/Buenos_Aires", "sid": 143505}, {"name": "\u4e9a\u7f8e\u5c3c\u4e9a", "code": "AM", "slug": "armenia", "tzone": "Asia/Yerevan", "sid": 143524}, {"name": "\u6fb3\u5927\u5229\u4e9a", "code": "AU", "slug": "australia", "tzone": "Australia/Sydney", "sid": 143460}, {"name": "\u5965\u5730\u5229", "code": "AT", "slug": "austria", "tzone": "Europe/Vienna", "sid": 143445}, {"name": "\u963f\u585e\u62dc\u7586", "code": "AZ", "slug": "azerbaijan", "tzone": "Asia/Baku", "sid": 143568}, {"name": "\u5df4\u54c8\u9a6c", "code": "BS", "slug": "bahamas", "tzone": "America/Nassau", "sid": 143539}, {"name": "\u5df4\u6797", "code": "BH", "slug": "bahrain", "tzone": "Asia/Bahrain", "sid": 143559}, {"name": "\u5df4\u5df4\u591a\u65af", "code": "BB", "slug": "barbados", "tzone": "America/Barbados", "sid": 143541}, {"name": "\u767d\u4fc4\u7f57\u65af", "code": "BY", "slug": "belarus", "tzone": "Europe/Minsk", "sid": 143565}, {"name": "\u6bd4\u5229\u65f6", "code": "BE", "slug": "belgium", "tzone": "Europe/Brussels", "sid": 143446}, {"name": "\u4f2f\u5229\u5179", "code": "BZ", "slug": "belize", "tzone": "America/Belize", "sid": 143555}, {"name": "\u8d1d\u5b81", "code": "BJ", "slug": "benin", "tzone": "Africa/Porto-Novo", "sid": 143576}, {"name": "\u767e\u6155\u5927", "code": "BM", "slug": "bermuda", "tzone": "Atlantic/Bermuda", "sid": 143542}, {"name": "\u4e0d\u4e39", "code": "BT", "slug": "Bhutan", "tzone": "Asia/Thimphu", "sid": 143577}, {"name": "\u73bb\u5229\u7ef4\u4e9a", "code": "BO", "slug": "bolivia", "tzone": "America/La_Paz", "sid": 143556}, {"name": "\u535a\u8328\u74e6\u7eb3", "code": "BW", "slug": "botswana", "tzone": "Africa/Gaborone", "sid": 143525}, {"name": "\u5df4\u897f", "code": "BR", "slug": "brazil", "tzone": "America/Sao_Paulo", "sid": 143503}, {"name": "\u82f1\u5c5e\u7ef4\u5c14\u4eac\u7fa4\u5c9b", "code": "VG", "slug": "british-virgin-islands", "tzone": "America/Tortola", "sid": 143543}, {"name": "\u6587\u83b1", "code": "BN", "slug": "brunei", "tzone": "Asia/Brunei", "sid": 143560}, {"name": "\u4fdd\u52a0\u5229\u4e9a", "code": "BG", "slug": "bulgaria", "tzone": "Europe/Sofia", "sid": 143526}, {"name": "\u5e03\u57fa\u7eb3\u6cd5\u7d22", "code": "BF", "slug": "burkina-faso", "tzone": "Africa/Ouagadougou", "sid": 143578}, {"name": "\u67ec\u57d4\u5be8", "code": "KH", "slug": "cambodia", "tzone": "Asia/Phnom_Penh", "sid": 143579}, {"name": "\u52a0\u62ff\u5927", "code": "CA", "slug": "canada", "tzone": "America/Toronto", "sid": 143455}, {"name": "\u4f5b\u5f97\u89d2", "code": "CV", "slug": "cape-verde", "tzone": "Atlantic/Cape_Verde", "sid": 143580}, {"name": "\u5f00\u66fc\u7fa4\u5c9b", "code": "KY", "slug": "cayman-islands", "tzone": "America/Cayman", "sid": 143544}, {"name": "\u4e4d\u5f97", "code": "TD", "slug": "chad", "tzone": "Africa/Ndjamena", "sid": 143581}, {"name": "\u667a\u5229", "code": "CL", "slug": "chile", "tzone": "America/Santiago", "sid": 143483}, {"name": "\u4e2d\u56fd", "code": "CN", "slug": "china", "tzone": "Asia/Shanghai", "sid": 143465}, {"name": "\u54e5\u4f26\u6bd4\u4e9a", "code": "CO", "slug": "colombia", "tzone": "America/Bogota", "sid": 143501}, {"name": "\u521a\u679c", "code": "CG", "slug": "congo", "tzone": "Africa/Brazzaville", "sid": 143582}, {"name": "\u54e5\u65af\u8fbe\u9ece\u52a0", "code": "CR", "slug": "costa-rica", "tzone": "America/Costa_Rica", "sid": 143495}, {"name": "\u514b\u7f57\u5730\u4e9a", "code": "HR", "slug": "croatia", "tzone": "Europe/Zagreb", "sid": 143494}, {"name": "\u585e\u6d66\u8def\u65af", "code": "CY", "slug": "cyprus", "tzone": "Asia/Nicosia", "sid": 143557}, {"name": "\u6377\u514b\u5171\u548c\u56fd", "code": "CZ", "slug": "czech-republic", "tzone": "Europe/Prague", "sid": 143489}, {"name": "\u4e39\u9ea6", "code": "DK", "slug": "denmark", "tzone": "Europe/Copenhagen", "sid": 143458}, {"name": "\u591a\u7c73\u5c3c\u514b", "code": "DM", "slug": "dominica", "tzone": "America/Dominica", "sid": 143545}, {"name": "\u591a\u7c73\u5c3c\u52a0\u5171\u548c\u56fd", "code": "DO", "slug": "dominican-republic", "tzone": "America/Santo_Domingo", "sid": 143508}, {"name": "\u5384\u74dc\u591a\u5c14", "code": "EC", "slug": "ecuador", "tzone": "America/Guayaquil", "sid": 143509}, {"name": "\u57c3\u53ca", "code": "EG", "slug": "egypt", "tzone": "Africa/Cairo", "sid": 143516}, {"name": "\u8428\u5c14\u74e6\u591a", "code": "SV", "slug": "el-salvador", "tzone": "America/El_Salvador", "sid": 143506}, {"name": "\u7231\u6c99\u5c3c\u4e9a", "code": "EE", "slug": "estonia", "tzone": "Europe/Tallinn", "sid": 143518}, {"name": "\u6590\u6d4e", "code": "FJ", "slug": "fiji", "tzone": "Pacific/Fiji", "sid": 143583}, {"name": "\u82ac\u5170", "code": "FI", "slug": "finland", "tzone": "Europe/Helsinki", "sid": 143447}, {"name": "\u6cd5\u56fd", "code": "FR", "slug": "france", "tzone": "Europe/Paris", "sid": 143442}, {"name": "\u5188\u6bd4\u4e9a", "code": "GM", "slug": "gambia", "tzone": "Africa/Banjul", "sid": 143584}, {"name": "\u5fb7\u56fd", "code": "DE", "slug": "germany", "tzone": "Europe/Berlin", "sid": 143443}, {"name": "\u52a0\u7eb3", "code": "GH", "slug": "ghana", "tzone": "Africa/Accra", "sid": 143573}, {"name": "\u5e0c\u814a", "code": "GR", "slug": "greece", "tzone": "Europe/Athens", "sid": 143448}, {"name": "\u683c\u6797\u7eb3\u8fbe", "code": "GD", "slug": "grenada", "tzone": "America/Grenada", "sid": 143546}, {"name": "\u5371\u5730\u9a6c\u62c9", "code": "GT", "slug": "guatemala", "tzone": "America/Guatemala", "sid": 143504}, {"name": "\u51e0\u5185\u4e9a\u6bd4\u7ecd", "code": "GW", "slug": "guinea-bissau", "tzone": "Africa/Bissau", "sid": 143585}, {"name": "\u572d\u4e9a\u90a3", "code": "GY", "slug": "guyana", "tzone": "America/Guyana", "sid": 143553}, {"name": "\u6d2a\u90fd\u62c9\u65af", "code": "HN", "slug": "honduras", "tzone": "America/Tegucigalpa", "sid": 143510}, {"name": "\u9999\u6e2f", "code": "HK", "slug": "hong-kong", "tzone": "Asia/Hong_Kong", "sid": 143463}, {"name": "\u5308\u7259\u5229", "code": "HU", "slug": "hungary", "tzone": "Europe/Budapest", "sid": 143482}, {"name": "\u51b0\u5c9b", "code": "IS", "slug": "iceland", "tzone": "Atlantic/Reykjavik", "sid": 143558}, {"name": "\u5370\u5ea6", "code": "IN", "slug": "india", "tzone": "Asia/Kolkata", "sid": 143467}, {"name": "\u5370\u5ea6\u5c3c\u897f\u4e9a", "code": "ID", "slug": "indonesia", "tzone": "Asia/Jakarta", "sid": 143476}, {"name": "\u7231\u5c14\u5170", "code": "IE", "slug": "ireland", "tzone": "Europe/Dublin", "sid": 143449}, {"name": "\u4ee5\u8272\u5217", "code": "IL", "slug": "israel", "tzone": "Asia/Jerusalem", "sid": 143491}, {"name": "\u610f\u5927\u5229", "code": "IT", "slug": "italy", "tzone": "Europe/Rome", "sid": 143450}, {"name": "\u7259\u4e70\u52a0", "code": "JM", "slug": "jamaica", "tzone": "America/Jamaica", "sid": 143511}, {"name": "\u65e5\u672c", "code": "JP", "slug": "japan", "tzone": "Asia/Tokyo", "sid": 143462}, {"name": "\u7ea6\u65e6", "code": "JO", "slug": "jordan", "tzone": "Asia/Amman", "sid": 143528}, {"name": "\u54c8\u8428\u514b\u65af\u5766", "code": "KZ", "slug": "kazakhstan", "tzone": "Asia/Almaty", "sid": 143517}, {"name": "\u80af\u5c3c\u4e9a", "code": "KE", "slug": "kenya", "tzone": "Africa/Nairobi", "sid": 143529}, {"name": "\u79d1\u5a01\u7279", "code": "KW", "slug": "kuwait", "tzone": "Asia/Kuwait", "sid": 143493}, {"name": "\u5409\u5c14\u5409\u65af\u65af\u5766", "code": "KG", "slug": "kyrgyzstan", "tzone": "Asia/Bishkek", "sid": 143586}, {"name": "\u8001\u631d", "code": "LA", "slug": "laos", "tzone": "Asia/Vientiane", "sid": 143587}, {"name": "\u62c9\u8131\u7ef4\u4e9a", "code": "LV", "slug": "latvia", "tzone": "Europe/Riga", "sid": 143519}, {"name": "\u9ece\u5df4\u5ae9", "code": "LB", "slug": "lebanon", "tzone": "Asia/Beirut", "sid": 143497}, {"name": "\u5229\u6bd4\u91cc\u4e9a", "code": "LR", "slug": "liberia", "tzone": "Africa/Monrovia", "sid": 143588}, {"name": "\u7acb\u9676\u5b9b", "code": "LT", "slug": "lithuania", "tzone": "Europe/Vilnius", "sid": 143520}, {"name": "\u5362\u68ee\u5821", "code": "LU", "slug": "luxembourg", "tzone": "Europe/Luxembourg", "sid": 143451}, {"name": "\u6fb3\u95e8", "code": "MO", "slug": "macau", "tzone": "Asia/Macau", "sid": 143515}, {"name": "\u9a6c\u5176\u987f", "code": "MK", "slug": "macedonia", "tzone": "Europe/Skopje", "sid": 143530}, {"name": "\u9a6c\u8fbe\u52a0\u65af\u52a0", "code": "MG", "slug": "madagascar", "tzone": "Indian/Antananarivo", "sid": 143531}, {"name": "\u9a6c\u62c9\u7ef4", "code": "MW", "slug": "malawi", "tzone": "Africa/Blantyre", "sid": 143589}, {"name": "\u9a6c\u6765\u897f\u4e9a", "code": "MY", "slug": "malaysia", "tzone": "Asia/Kuala_Lumpur", "sid": 143473}, {"name": "\u9a6c\u91cc", "code": "ML", "slug": "mali", "tzone": "Africa/Bamako", "sid": 143532}, {"name": "\u9a6c\u8033\u4ed6", "code": "MT", "slug": "malta", "tzone": "Europe/Malta", "sid": 143521}, {"name": "\u6bdb\u91cc\u5854\u5c3c\u4e9a", "code": "MR", "slug": "mauritania", "tzone": "Africa/Nouakchott", "sid": 143590}, {"name": "\u6bdb\u91cc\u6c42\u65af", "code": "MU", "slug": "mauritius", "tzone": "Indian/Mauritius", "sid": 143533}, {"name": "\u58a8\u897f\u54e5", "code": "MX", "slug": "mexico", "tzone": "America/Mexico_City", "sid": 143468}, {"name": "\u5bc6\u514b\u7f57\u5c3c\u897f\u4e9a", "code": "FM", "slug": "micronesia", "tzone": "Pacific/Chuuk", "sid": 143591}, {"name": "\u6469\u5c14\u591a\u74e6", "code": "MD", "slug": "moldova", "tzone": "Europe/Chisinau", "sid": 143523}, {"name": "\u8499\u53e4", "code": "MN", "slug": "mongolia", "tzone": "Asia/Ulaanbaatar", "sid": 143592}, {"name": "\u8499\u7279\u585e\u62c9\u7279", "code": "MS", "slug": "montserrat", "tzone": "America/Montserrat", "sid": 143547}, {"name": "\u83ab\u6851\u6bd4\u514b", "code": "MZ", "slug": "mozambique", "tzone": "Africa/Maputo", "sid": 143593}, {"name": "\u7eb3\u7c73\u6bd4\u4e9a", "code": "NA", "slug": "namibia", "tzone": "Africa/Windhoek", "sid": 143594}, {"name": "\u5c3c\u6cca\u5c14", "code": "NP", "slug": "nepal", "tzone": "Asia/Kathmandu", "sid": 143484}, {"name": "\u8377\u5170", "code": "NL", "slug": "netherlands", "tzone": "Europe/Amsterdam", "sid": 143452}, {"name": "\u65b0\u897f\u5170", "code": "NZ", "slug": "new-zealand", "tzone": "Pacific/Auckland", "sid": 143461}, {"name": "\u5c3c\u52a0\u62c9\u74dc", "code": "NI", "slug": "nicaragua", "tzone": "America/Managua", "sid": 143512}, {"name": "\u5c3c\u65e5\u5c14", "code": "NE", "slug": "niger", "tzone": "Africa/Niamey", "sid": 143534}, {"name": "\u5c3c\u65e5\u5229\u4e9a", "code": "NG", "slug": "nigeria", "tzone": "Africa/Lagos", "sid": 143561}, {"name": "\u632a\u5a01", "code": "NO", "slug": "norway", "tzone": "Europe/Oslo", "sid": 143457}, {"name": "\u963f\u66fc", "code": "OM", "slug": "oman", "tzone": "Asia/Muscat", "sid": 143562}, {"name": "\u5df4\u57fa\u65af\u5766", "code": "PK", "slug": "pakistan", "tzone": "Asia/Karachi", "sid": 143477}, {"name": "\u5e15\u52b3", "code": "PW", "slug": "palau", "tzone": "Pacific/Palau", "sid": 143595}, {"name": "\u5df4\u62ff\u9a6c", "code": "PA", "slug": "panama", "tzone": "America/Panama", "sid": 143485}, {"name": "\u5df4\u5e03\u4e9a\u65b0\u51e0\u5185\u4e9a", "code": "PG", "slug": "papua-new-guinea", "tzone": "Pacific/Port_Moresby", "sid": 143597}, {"name": "\u5df4\u62c9\u572d", "code": "PY", "slug": "paraguay", "tzone": "America/Asuncion", "sid": 143513}, {"name": "\u79d8\u9c81", "code": "PE", "slug": "peru", "tzone": "America/Lima", "sid": 143507}, {"name": "\u83f2\u5f8b\u5bbe", "code": "PH", "slug": "philippines", "tzone": "Asia/Manila", "sid": 143474}, {"name": "\u6ce2\u5170", "code": "PL", "slug": "poland", "tzone": "Europe/Warsaw", "sid": 143478}, {"name": "\u8461\u8404\u7259", "code": "PT", "slug": "portugal", "tzone": "Europe/Lisbon", "sid": 143453}, {"name": "\u5361\u5854\u5c14", "code": "QA", "slug": "qatar", "tzone": "Asia/Qatar", "sid": 143498}, {"name": "\u7f57\u9a6c\u5c3c\u4e9a", "code": "RO", "slug": "romania", "tzone": "Europe/Bucharest", "sid": 143487}, {"name": "\u4fc4\u7f57\u65af", "code": "RU", "slug": "russia", "tzone": "Europe/Moscow", "sid": 143469}, {"name": "\u5723\u591a\u7f8e\u548c\u666e\u6797\u897f\u6bd4", "code": "ST", "slug": "sao-tome-and-principe", "tzone": "Africa/Sao_Tome", "sid": 143598}, {"name": "\u6c99\u7279\u963f\u62c9\u4f2f", "code": "SA", "slug": "saudi-arabia", "tzone": "Asia/Riyadh", "sid": 143479}, {"name": "\u585e\u5185\u52a0\u5c14", "code": "SN", "slug": "senegal", "tzone": "Africa/Dakar", "sid": 143535}, {"name": "\u585e\u820c\u5c14", "code": "SC", "slug": "seychelles", "tzone": "Indian/Mahe", "sid": 143599}, {"name": "\u585e\u62c9\u5229\u6602", "code": "SL", "slug": "sierra-leone", "tzone": "Africa/Freetown", "sid": 143600}, {"name": "\u65b0\u52a0\u5761", "code": "SG", "slug": "singapore", "tzone": "Asia/Singapore", "sid": 143464}, {"name": "\u65af\u6d1b\u4f10\u514b", "code": "SK", "slug": "slovakia", "tzone": "Europe/Bratislava", "sid": 143496}, {"name": "\u65af\u6d1b\u6587\u5c3c\u4e9a", "code": "SI", "slug": "slovenia", "tzone": "Europe/Ljubljana", "sid": 143499}, {"name": "\u6240\u7f57\u95e8\u7fa4\u5c9b", "code": "SB", "slug": "solomon-islands", "tzone": "Pacific/Guadalcanal", "sid": 143601}, {"name": "\u5357\u975e", "code": "ZA", "slug": "south-africa", "tzone": "Africa/Johannesburg", "sid": 143472}, {"name": "\u97e9\u56fd", "code": "KR", "slug": "south-korea", "tzone": "Asia/Seoul", "sid": 143466}, {"name": "\u897f\u73ed\u7259", "code": "ES", "slug": "spain", "tzone": "Europe/Madrid", "sid": 143454}, {"name": "\u65af\u91cc\u5170\u5361", "code": "LK", "slug": "sri-lanka", "tzone": "Asia/Colombo", "sid": 143486}, {"name": "\u5723\u57fa\u8328\u548c\u5c3c\u7ef4\u65af", "code": "KN", "slug": "st-kitts-and-nevis", "tzone": "America/St_Kitts", "sid": 143548}, {"name": "\u5723\u5362\u897f\u4e9a", "code": "LC", "slug": "st-lucia", "tzone": "America/St_Lucia", "sid": 143549}, {"name": "\u5723\u6587\u68ee\u7279\u548c\u683c\u6797\u7eb3\u4e01\u65af", "code": "VC", "slug": "st-vincent-and-the-grenadines", "tzone": "America/St_Vincent", "sid": 143550}, {"name": "\u82cf\u91cc\u5357", "code": "SR", "slug": "suriname", "tzone": "America/Paramaribo", "sid": 143554}, {"name": "\u65af\u5a01\u58eb\u5170", "code": "SZ", "slug": "swaziland", "tzone": "Africa/Mbabane", "sid": 143602}, {"name": "\u745e\u5178", "code": "SE", "slug": "sweden", "tzone": "Europe/Stockholm", "sid": 143456}, {"name": "\u745e\u58eb", "code": "CH", "slug": "switzerland", "tzone": "Europe/Zurich", "sid": 143459}, {"name": "\u53f0\u6e7e", "code": "TW", "slug": "taiwan", "tzone": "Asia/Taipei", "sid": 143470}, {"name": "\u5854\u5409\u514b\u65af\u5766", "code": "TJ", "slug": "tajikistan", "tzone": "Asia/Dushanbe", "sid": 143603}, {"name": "\u5766\u6851\u5c3c\u4e9a", "code": "TZ", "slug": "tanzania", "tzone": "Africa/Dar_es_Salaam", "sid": 143572}, {"name": "\u6cf0\u56fd", "code": "TH", "slug": "thailand", "tzone": "Asia/Bangkok", "sid": 143475}, {"name": "\u7279\u7acb\u5c3c\u8fbe\u548c\u591a\u5df4\u54e5", "code": "TT", "slug": "trinidad-and-tobago", "tzone": "America/Port_of_Spain", "sid": 143551}, {"name": "\u7a81\u5c3c\u65af", "code": "TN", "slug": "tunisia", "tzone": "Africa/Tunis", "sid": 143536}, {"name": "\u571f\u8033\u5176", "code": "TR", "slug": "turkey", "tzone": "Europe/Istanbul", "sid": 143480}, {"name": "\u571f\u5e93\u66fc\u65af\u5766", "code": "TM", "slug": "turkmenistan", "tzone": "Asia/Ashgabat", "sid": 143604}, {"name": "\u7279\u514b\u65af\u548c\u51ef\u79d1\u65af\u7fa4\u5c9b", "code": "TC", "slug": "turks-and-caicos", "tzone": "America/Grand_Turk", "sid": 143552}, {"name": "\u4e4c\u5e72\u8fbe", "code": "UG", "slug": "uganda", "tzone": "Africa/Kampala", "sid": 143537}, {"name": "\u4e4c\u514b\u5170", "code": "UA", "slug": "ukraine", "tzone": "Europe/Kiev", "sid": 143492}, {"name": "\u963f\u8054\u914b", "code": "AE", "slug": "united-arab-emirates", "tzone": "Asia/Dubai", "sid": 143481}, {"name": "\u82f1\u56fd", "code": "GB", "slug": "united-kingdom", "tzone": "Europe/London", "sid": 143444}, {"name": "\u7f8e\u56fd", "code": "US", "slug": "united-states", "tzone": "America/Los_Angeles", "sid": 143441}, {"name": "\u4e4c\u62c9\u572d", "code": "UY", "slug": "uruguay", "tzone": "America/Montevideo", "sid": 143514}, {"name": "\u4e4c\u5179\u522b\u514b\u65af\u5766", "code": "UZ", "slug": "uzbekistan", "tzone": "Asia/Tashkent", "sid": 143566}, {"name": "\u59d4\u5185\u745e\u62c9", "code": "VE", "slug": "venezuela", "tzone": "America/Caracas", "sid": 143502}, {"name": "\u8d8a\u5357", "code": "VN", "slug": "vietnam", "tzone": "Asia/Ho_Chi_Minh", "sid": 143471}, {"name": "\u4e5f\u95e8", "code": "YE", "slug": "yemen", "tzone": "Asia/Aden", "sid": 143571}, {"name": "\u6d25\u5df4\u5e03\u97e6", "code": "ZW", "slug": "zimbabwe", "tzone": "Africa/Harare", "sid": 143605}];



    __ng_boot_inject_module = 'item.all';
</script>
<script src="https://static-s.aa-cdn.net/media/javascript/_lang/zh-cn/sea/aa.v-2ba516-20e038.js" crossorigin="anonymous"></script>
<script src="https://static-s.aa-cdn.net/media/javascript/_lang/zh-cn/sea/app.v-1b162e-20e038.js" crossorigin="anonymous"></script>
<script src="https://static-s.aa-cdn.net/media/javascript/prod/aa.min.v-3adb7b40.js" crossorigin="anonymous"></script>
<script src="https://static-s.aa-cdn.net/media/javascript/prod/app.min.v-cd5eccb9.js" crossorigin="anonymous"></script>
<script> jQuery(function(){ require(["aa/aa", "app/app"], function() {  $('body').trigger('moduleloaded');  }); }); </script>

<script>
var pageVal = $.extend(pageVal || {}, {
    'GA': {
        'pageType': 'Asset',
        'vertical': 'apps',
        'pageName': 'Reviews',
        'label': 'Asset-apps-Reviews'
    }
});
</script>

<script>
    
var pageVal = $.extend({}, pageVal);

pageVal.lang =  __lang;





    

    if(!_.isEmpty(pageVal.user)) {
      // for the Usabilla API request
      var timer = setInterval(function() {
          if(pageVal && window.usabilla_live) {
              var nowDate = new Date();
              var over30Days;
              var registerDate;
              var userType;
              var lastDigitUserid;

              if (pageVal.user.date_joined) {
                  registerDate = pageVal.user.date_joined;
                  var regDate = new Date(registerDate.replace(/\-/g, '/'));
                  var regDuration = (nowDate - regDate) / (1000*60*60*24);

                  // if over than 30days, then set true
                  over30Days = regDuration > 30;
              }

              if (pageVal.user.flags) {
                  // for the user type
                  userType = 'SS';
                  if (pageVal.user.flags.is_int_user) {
                      userType = 'INT'
                  } else if(pageVal.user.flags.is_connect_user) {
                      userType = 'AN'
                  }
              }

              if (pageVal.user.id) {
                  lastDigitUserid = pageVal.user.id.slice(-1);
                  window._walkmeUid_X || (window._walkmeUid_X = lastDigitUserid);
              }

              window.usabilla_live("data", {
                  "custom": {
                      "user_id": pageVal.user.id,
                      "last_digit_userid": lastDigitUserid,
                      "user_type": userType,
                      "user_registration_date": registerDate,
                      "user_morethan_30days": over30Days,
                      "email": pageVal.user.email
                  }
              });

              clearInterval(timer);
          }
      }, 1000);
    }
</script>



<!-- www.appannie.com, http://www.appannie.com -->





<div class="aa_selector" style="width: 46.5em; display: none;"><div class="quick_selection"><a data-rel="364">最近 365 天</a><span class="sep"> - </span><a data-rel="89">最近 90 天</a><span class="sep"> - </span><a data-rel="29">最近 30 天</a><span class="sep"> - </span><a data-rel="13">最近 14 天</a><span class="sep"> - </span><a data-rel="6">最近 7 天</a></div><div class="selection_content"><div id="aa_ui_dp_1"></div></div><div class="tipbox-direction tipbox-right-up"><em>◆</em><span>◆</span></div></div><script type="text/javascript" id="">window.heap=window.heap||[];
heap.load=function(b,c){window.heap.appid=b;window.heap.config=c=c||{};var a=c.forceSSL||"https:"===document.location.protocol,d=document.createElement("script");d.type="text/javascript";d.async=!0;d.src=(a?"https:":"http:")+"//cdn.heapanalytics.com/js/heap-"+b+".js";a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(d,a);if(Array.isArray(window.heap)){d=function(a){return function(){heap.push([a].concat(Array.prototype.slice.call(arguments,0)))}};a="addEventProperties addUserProperties clearEventProperties identify removeEventProperty setEventProperties track unsetEventProperty".split(" ");
for(var e=0;e<a.length;e++)heap[a[e]]=d(a[e])}};heap.load("3646280627");(function(b,c){"undefined"==b&&(b=null);"undefined"==c&&(c=null);b&&(heap.identify(b),heap.addUserProperties({email:c}))})("1664130","583551648@qq.com");</script>
<script type="text/javascript" id="">(function(c,n){if(c){var f=window[n];f&&c.register({pageview:function(g,h){var k={event:"analyticsVPV",vpvName:g,vpvTitle:h};f.push(k)},event:function(g,h,k,c){var d={event:"analyticsEvent",eventCategory:g,eventAction:h},m=d,e=arguments,a=e[e.length-1];if(null!=a&&"object"==typeof a){for(var b in a)m["ga_"+b]=a[b];for(var l=0;9>=l;++l)b="hit_p"+l,a.hasOwnProperty(b)||(m["ga_"+b]="");e[e.length-1]=void 0}d.eventLabel=k;d.eventValue=c;f.push(d)}},!0)}})(window.aaTrack,"dataLayer_"+"GTM-D44H".replace("GTM-",
""));</script>
<script type="text/javascript" id="">var _gaq=_gaq||[];_gaq.push(["_setAccount","UA-2339266-6"]);_gaq.push(["_setDomainName","appannie.com"]);(function(){var a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src=("https:"==document.location.protocol?"https://":"http://")+"stats.g.doubleclick.net/dc.js";var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b)})();</script><div style="display: none; visibility: hidden;"><script type="text/javascript">(function(){function b(){!1===c&&(c=!0,Munchkin.init("071-QED-284",{asyncOnly:!0,disableClickDelay:!0}))}var c=!1,a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="//munchkin.marketo.net/munchkin.js";a.onreadystatechange=function(){"complete"!=this.readyState&&"loaded"!=this.readyState||b()};a.onload=b;document.getElementsByTagName("head")[0].appendChild(a)})();</script></div><script type="text/javascript" id="">(function(){var a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="https://cdn.walkme.com/users/440e9852f2724fafb2d968494f028e77/walkme_440e9852f2724fafb2d968494f028e77_https.js";var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b);window._walkmeConfig={smartLoad:!0};window._walkmeUid="1664130";window._walkmeUid_X=window._walkmeUid.substr(window._walkmeUid.length-1);window._walkmeUserInfo={is_int_user:"no",is_connect_user:"no",
account_type:"basic",admin_status:"user",activation_time:"2019-05-29 19:28:01.224562",job_function:"Other",registration_date:"2019-05-29 19:27:12.064903",days_since_registered:google_tag_manager["GTM-D44H"].macro(2),first_name:"Xia",walkme_resource_menu:google_tag_manager["GTM-D44H"].macro(3)}})();</script><script type="text/javascript" id="">window.lightningjs||function(c){function g(b,d){d&&(d+=(/\?/.test(d)?"\x26":"?")+"lv\x3d1");c[b]||function(){var k=window,h=document,l=b,g=h.location.protocol,n="load",m=0;(function(){function b(){a.P(n);a.w=1;c[l]("_load")}c[l]=function(){function p(){p.id=e;return c[l].apply(p,arguments)}var e=++m;var b=this&&this!=k?this.id||0:0;(a.s=a.s||[]).push([e,b,arguments]);p.then=function(b,c,h){var d=a.fh[e]=a.fh[e]||[],l=a.eh[e]=a.eh[e]||[],f=a.ph[e]=a.ph[e]||[];b&&d.push(b);c&&l.push(c);h&&f.push(h);
return p};return p};var a=c[l]._={};a.fh={};a.eh={};a.ph={};a.l=d?d.replace(/^\/\//,("https:"==g?g:"http:")+"//"):d;a.p={0:+new Date};a.P=function(b){a.p[b]=new Date-a.p[0]};a.w&&b();k.addEventListener?k.addEventListener(n,b,!1):k.attachEvent("on"+n,b);var t=function(){function b(){return["\x3chead\x3e\x3c/head\x3e\x3c",e,' onload\x3d"var d\x3d',q,";d.getElementsByTagName('head')[0].",d,"(d.",g,"('script')).",k,"\x3d'",a.l,"'\"\x3e\x3c/",e,"\x3e"].join("")}var e="body",c=h[e];if(!c)return setTimeout(t,
100);a.P(1);var d="appendChild",g="createElement",k="src",m=h[g]("div"),n=m[d](h[g]("div")),f=h[g]("iframe"),q="document";m.style.display="none";c.insertBefore(m,c.firstChild).id=r+"-"+l;f.frameBorder="0";f.id=r+"-frame-"+l;/MSIE[ ]+6/.test(navigator.userAgent)&&(f[k]="javascript:false");f.allowTransparency="true";n[d](f);try{f.contentWindow[q].open()}catch(w){a.domain=h.domain;var u="javascript:var d\x3d"+q+".open();d.domain\x3d'"+h.domain+"';";f[k]=u+"void(0);"}try{var v=f.contentWindow[q];v.write(b());
v.close()}catch(w){f[k]=u+'d.write("'+b().replace(/"/g,String.fromCharCode(92)+'"')+'");d.close();'}a.P(2)};a.l&&setTimeout(t,0)})()}();c[b].lv="1";return c[b]}var r="lightningjs",m=window[r]=g(r);m.require=g;m.modules=c}({});navigator.userAgent.match(/Android|BlackBerry|BB10|iPhone|iPad|iPod|Opera Mini|IEMobile/i)?window.usabilla_live=lightningjs.require("usabilla_live","//w.usabilla.com/ed7fd09d037a.js"):window.usabilla_live=lightningjs.require("usabilla_live","//w.usabilla.com/e981f512f6cb.js");
"en"==document.documentElement.lang?window.usabilla_live("setForm","default"):"de"==document.documentElement.lang?window.usabilla_live("setForm","DE"):"fr"==document.documentElement.lang?window.usabilla_live("setForm","FR"):"kr"==document.documentElement.lang?window.usabilla_live("setForm","KR"):"jp"==document.documentElement.lang?window.usabilla_live("setForm","JP"):"cn"==document.documentElement.lang?window.usabilla_live("setForm","CN"):"ru"==document.documentElement.lang&&window.usabilla_live("setForm",
"RU");var uid="1664130";window.usabilla_live("data",{custom:{user_id:uid,last_digit_userid:uid.substr(uid.length-1),is_int_user:"no",is_connect_user:"no",account_type:"basic",admin_status:"user",activation_time:"2019-05-29 19:28:01.224562",job_function:"Other",registration_date:"2019-05-29 19:27:12.064903",days_since_registered:google_tag_manager["GTM-D44H"].macro(4),first_name:"Xia"}});</script>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","680989378664200");fbq("track","PageView");</script>
<noscript>&lt;img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=680989378664200&amp;amp;ev=PageView&amp;amp;noscript=1"&gt;</noscript>
<script type="text/javascript" id="">_airpr={id:"685381",ga_dim:"92",ga_account_preset:"UA-2339266-6"};(function(c,d,a,b){a=c.createElement(d);a.async=1;a.src="//px.airpr.com/airpr.js";b=c.getElementsByTagName(d)[0];b.parentNode.insertBefore(a,b)})(document,"script");</script><script type="text/javascript" id="" src="//pixel.mathtag.com/event/js?mt_id=1135071&amp;mt_adid=181986&amp;v1=&amp;v2=&amp;v3=&amp;s1=&amp;s2=&amp;s3="></script><script type="text/javascript" id="">(function(){var a=encodeURIComponent(window.location.href),c=encodeURIComponent(document.title),b=document.createElement("script");b.type="text/javascript";b.async=!0;b.src=("https:"==document.location.protocol?"https://":"http://")+"pixel.mathtag.com/event/js?mt_id\x3d1135071\x26mt_adid\x3d181986\x26v1\x3d\x26v2\x3d\x26v3\x3d\x26s3\x3d\x26s1\x3d"+a+"\x26s2\x3d"+c;a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(b,a)})();</script>
<script type="text/javascript" id="">(function(b){var a=b.createElement("img");a.src="https://ml314.com/utsync.ashx?eid\x3d50215\x26et\x3d0\x26d\x3d1213700\x26dc\x3dwebpage\x26cb\x3d"+Date.now();a.style.display="none";b.body.appendChild(a)})(document);</script><img src="https://ml314.com/utsync.ashx?eid=50215&amp;et=0&amp;d=1213700&amp;dc=webpage&amp;cb=1559256391652" style="display: none;"><script type="text/javascript" id="">!function(c,d){var b="00c5cbfc076df6e2ef3b6938a0672ba6ac";if(!c.obApi){var a=c.obApi=function(){a.dispatch?a.dispatch.apply(a,arguments):a.queue.push(arguments)};a.version="1.0";a.loaded=!0;a.marketerId=b;a.queue=[];b=d.createElement("script");b.async=!0;b.src="//amplify.outbrain.com/cp/obtp.js";b.type="text/javascript";var e=d.getElementsByTagName("script")[0];e.parentNode.insertBefore(b,e)}}(window,document);obApi("track","PAGE_VIEW");</script><script type="text/javascript" id="">adroll_adv_id="4IJGT2ZDGJFZLAACNH4TVF";adroll_pix_id="PSAAGT4MFBB2ROIM33X7L2";
(function(){var a=function(){if(document.readyState&&!/loaded|complete/.test(document.readyState))setTimeout(a,10);else if(window.__adroll_loaded){var b=document.createElement("script"),c="https:"==document.location.protocol?"https://s.adroll.com":"http://a.adroll.com";b.setAttribute("async","true");b.type="text/javascript";b.src=c+"/j/roundtrip.js";((document.getElementsByTagName("head")||[null])[0]||document.getElementsByTagName("script")[0].parentNode).appendChild(b)}else __adroll_loaded=!0,setTimeout(a,
50)};window.addEventListener?window.addEventListener("load",a,!1):window.attachEvent("onload",a)})();</script><script src="https://px.ads.linkedin.com/collect/?time=1559256391754&amp;pid=6256&amp;url=https%3A%2F%2Fwww.appannie.com%2Fapps%2Fios%2Fapp%2Fidle-heroes%2Freviews%2F%3Forder_by%3Ddate%26order_type%3Ddesc%26date%3D2019-04-29~2019-05-29%26translate_selected%3Dfalse%26granularity%3Dweekly%26stack%26percent%3Dfalse%26series%3Drating_star_1%2Crating_star_2%2Crating_star_3%2Crating_star_4%2Crating_star_5&amp;fmt=js&amp;s=1" type="text/javascript"></script><iframe id="walkme-proxy-iframe" src="about:blank" style="display: none; visibility: hidden;"></iframe><div class="usabilla_live_button_container" tabindex="0" style="height:31px;z-index:999999;bottom:0px;right:2%;position:fixed;width:100px" aria-label="Usabilla Feedback Button"><iframe src="" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" data-tags="bottom" title="Usabilla Feedback Button" style="width: 100px; height: 31px; margin: 0px; padding: 0px; border: 0px; overflow: hidden; z-index: 9998; position: absolute; left: 0px; top: 0px; box-shadow: 0px 0px 0px; background-color: transparent;"></iframe></div></body></html>

'''

url = "https://www.appannie.com/apps/ios/app/idle-heroes/reviews/?order_by=date&order_type=desc&date=2019-04-29~2019-05-29&translate_selected=false&granularity=weekly&stack&percent=false&series=rating_star_1,rating_star_2,rating_star_3,rating_star_4,rating_star_5"

header ={'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
response = requests.get(url,headers = header)
htm0 = response.content
# re=response.content
#
#
#
# selector2=etree.HTML(re)
selector=etree.HTML(html)

#contents=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]')

# simple1=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/span[1]/a')
# print simple1
# print simple1

simple2=selector.xpath('//*[@id="4229616386"]/div/div[2]/text()')
print simple2
print simple2