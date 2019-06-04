#coding:utf8

import requests

from lxml import etree

html='''


<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-mac ua-webkit book-new-nav">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>百年孤独 (豆瓣)</title>
  
<script>!function(e){var o=function(o,n,t){var c,i,r=new Date;n=n||30,t=t||"/",r.setTime(r.getTime()+24*n*60*60*1e3),c="; expires="+r.toGMTString();for(i in o)e.cookie=i+"="+o[i]+c+"; path="+t},n=function(o){var n,t,c,i=o+"=",r=e.cookie.split(";");for(t=0,c=r.length;t<c;t++)if(n=r[t].replace(/^\s+|\s+$/g,""),0==n.indexOf(i))return n.substring(i.length,n.length).replace(/\"/g,"");return null},t=e.write,c={"douban.com":1,"douban.fm":1,"google.com":1,"google.cn":1,"googleapis.com":1,"gmaptiles.co.kr":1,"gstatic.com":1,"gstatic.cn":1,"google-analytics.com":1,"googleadservices.com":1},i=function(e,o){var n=new Image;n.onload=function(){},n.src="https://www.douban.com/j/except_report?kind=ra022&reason="+encodeURIComponent(e)+"&environment="+encodeURIComponent(o)},r=function(o){try{t.call(e,o)}catch(e){t(o)}},a=/<script.*?src\=["']?([^"'\s>]+)/gi,g=/http:\/\/(.+?)\.([^\/]+).+/i;e.writeln=e.write=function(e){var t,l=a.exec(e);return l&&(t=g.exec(l[1]))?c[t[2]]?void r(e):void("tqs"!==n("hj")&&(i(l[1],location.href),o({hj:"tqs"},1),setTimeout(function(){location.replace(location.href)},50))):void r(e)}}(document);
</script>

  
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
  
<meta http-equiv="mobile-agent" content="format=html5; url=https://m.douban.com/book/subject/6082808/">
<meta name="keywords" content="百年孤独,[哥伦比亚] 加西亚·马尔克斯,南海出版公司,2011-6,简介,作者,书评,论坛,推荐,二手">
<meta name="description" content="图书百年孤独 介绍、书评、论坛及推荐 ">

  <script>var _head_start = new Date();</script>
  
  <link href="https://img3.doubanio.com/f/book/7447c6dfeef0a88e2baaea2e4776bce9fd4cfb8e/css/book/master.css" rel="stylesheet" type="text/css">

  <link href="https://img3.doubanio.com/f/book/222a5c61e041638af8defc87cf97f4a863a77922/css/book/base/init.css" rel="stylesheet">
  <style type="text/css"></style>
  <script src="https://img3.doubanio.com/f/book/0495cb173e298c28593766009c7b0a953246c5b5/js/book/lib/jquery/jquery.js"></script>
  <script src="https://img3.doubanio.com/f/shire/1316664523258f7b8b536e4ce45afc9cb37b8963/js/douban.js"></script>
  <script src="https://img3.doubanio.com/f/book/165dc24cf2570e1b0d6294c948e46f3bc8259388/js/book/master.js"></script>
  

  
  <link rel="stylesheet" href="https://img3.doubanio.com/f/book/1eabe3f4e416e77dbafd2ef9bc830fa2ac7a8d4c/css/book/subject.css">
  <link href="https://img3.doubanio.com/f/book/5d301503fbbd8e09f3114583859789884e942f47/css/book/annotation/like.css" rel="stylesheet">
  <script src="https://img3.doubanio.com/f/shire/3c6f2946669cfb2fc9ee4a4d1dcc41fc181cad92/js/lib/jquery.snippet.js"></script>
  <script src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
  <script src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js"></script>
  <script src="https://img3.doubanio.com/f/book/2e421e5ec8f2869d31535206c0ac0322532be1f8/js/book/mod/hide.js"></script>
  <script src="https://img3.doubanio.com/f/book/cc6b1a77c3812c7dd20b0374332fade081e1c0b0/js/book/subject/unfold.js"></script>
    <link rel="alternate" href="https://book.douban.com/feed/subject/6082808/reviews" type="application/rss+xml" title="RSS">
  <style type="text/css"> h2 {color: #007722;} </style>
  <script type='text/javascript'>
    var _vds = _vds || [];
    (function(){ _vds.push(['setAccountId', '22c937bbd8ebd703f2d8e9445f7dfd03']);
        _vds.push(['setCS1','user_id','0']);
            (function() {var vds = document.createElement('script');
                vds.type='text/javascript';
                vds.async = true;
                vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
                var s = document.getElementsByTagName('script')[0];
                s.parentNode.insertBefore(vds, s);
            })();
    })();
</script>

  
  <script type='text/javascript'>
    var _vwo_code=(function(){
      var account_id=249272,
          settings_tolerance=2000,
          library_tolerance=2500,
          use_existing_jquery=false,
          // DO NOT EDIT BELOW THIS LINE
          f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());_vwo_settings_timer=_vwo_code.init();
  </script>

  


<script type="application/ld+json">
{
  "@context":"http://schema.org",
  "@type":"Book",
  "workExample": [],
  "name" : "百年孤独",
  "author": 
  [
    {
      "@type": "Person",
      "name": "[哥伦比亚] 加西亚·马尔克斯"
    }
  ]
,
  "url" : "https://book.douban.com/subject/6082808/",
  "isbn" : "9787544253994",
  "sameAs": "https://book.douban.com/subject/6082808/"
}
</script>


  <script>  </script>
  <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/5ef2a22fba637133.css">

  <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>
<body>
  
    <script>var _body_start = new Date();</script>
    
  



    <link href="//img3.doubanio.com/dae/accounts/resources/4bf727f/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://accounts.douban.com/passport/login?source=book" class="nav-login" rel="nofollow">登录/注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="on">
      <a href="https://book.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/4bf727f/shire/bundle.js" defer="defer"></script>




  



    <link href="//img3.doubanio.com/dae/accounts/resources/4bf727f/book/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-book" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;book.douban.com">豆瓣读书</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;book.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1001" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://book.douban.com/cart/"
     >购书单</a>
    </li>
    <li    ><a href="https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"
            target="_blank"
     >电子图书</a>
    </li>
    <li    ><a href="https://market.douban.com/book?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web"
     >豆瓣书店</a>
    </li>
    <li    ><a href="https://book.douban.com/annual/2018?source=navigation"
            target="_blank"
     >2018年度榜单</a>
    </li>
    <li    ><a href="https://www.douban.com/standbyme/2018?source=navigation"
            target="_blank"
     >2018书影音报告</a>
    </li>
    <li          class=" book-cart"
    ><a href="https://market.douban.com/cart/?biz_type=book&utm_campaign=book_nav_cart&utm_source=douban&utm_medium=pc_web"
            target="_blank"
     >购物车</a>
    </li>
  </ul>
</div>

    <a href="https://book.douban.com/annual/2018?source=book_navigation" class="bookannual2018"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'book_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= pic}}" width="40" />
            <div>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                <p>
                {{if type == "b"}}
                    {{= author_name}}
                {{else type == "a" }}
                    {{if en_name}}
                        {{= en_name}}
                    {{/if}}
                {{/if}}
                 </p>
            </div>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/4bf727f/book/bundle.js" defer="defer"></script>





    <div id="wrapper">
        
    <div id="dale_book_subject_top_icon"></div>
<h1>
    <span property="v:itemreviewed">百年孤独</span>
    <div class="clear"></div>
</h1>

        
  <div id="content">
    
    <div class="grid-16-8 clearfix">
      
      <div class="article">



<div class="indent">
  <div class="subjectwrap clearfix">
    



<div class="subject clearfix">
<div id="mainpic" class="">

  

  <a class="nbg"
      href="https://img3.doubanio.com/view/subject/l/public/s6384944.jpg" title="百年孤独">
    <img src="https://img3.doubanio.com/view/subject/l/public/s6384944.jpg" title="点击看大图" alt="百年孤独"
         rel="v:photo" style="width: 135px;max-height: 200px;">
  </a>



</div>





<div id="info" class="">



    
    
  

    <span class="pl">作者:</span>&nbsp;
        <a href="https://book.douban.com/author/1039386/">
                [哥伦比亚]
            加西亚·马尔克斯</a>
    <br>


    
    
  
    <span class="pl">出版社:</span> 南海出版公司<br/>

    
    
  
    <span class="pl">出品方:</span>&nbsp;<a href="https://book.douban.com/series/39059?brand=1">新经典文化</a><br>

    
    
  

    
    
  
    <span class="pl">原作名:</span> Cien años de soledad<br/>

    
    
  

    <span class="pl">译者:</span>&nbsp;
        <a href="https://book.douban.com/author/4608209/">
            范晔</a>
    <br>


    
    
  
    <span class="pl">出版年:</span> 2011-6<br/>

    
    
  
    <span class="pl">页数:</span> 360<br/>

    
    
  
    <span class="pl">定价:</span> 39.50元<br/>

    
    
  
    <span class="pl">装帧:</span> 精装<br/>

    
    
  
    <span class="pl">丛书:</span>&nbsp;<a href="https://book.douban.com/series/10489">新经典文库:加西亚·马尔克斯作品</a><br>

    
    
  
    
      
      <span class="pl">ISBN:</span> 9787544253994<br/>


</div>

</div>
























    





<div id="interest_sectl" class="">
  <div class="rating_wrap clearbox" rel="v:rating">
    <div class="rating_logo">豆瓣评分</div>
    <div class="rating_self clearfix" typeof="v:Rating">
      <strong class="ll rating_num " property="v:average"> 9.2 </strong>
      <span property="v:best" content="10.0"></span>
      <div class="rating_right ">
          <div class="ll bigstar45"></div>
            <div class="rating_sum">
                <span class="">
                    <a href="collections" class="rating_people"><span property="v:votes">197765</span>人评价</a>
                </span>
            </div>


      </div>
    </div>
          
            
            
<span class="stars5 starstop" title="力荐">
    5星
</span>

            
<div class="power" style="width:64px"></div>

            <span class="rating_per">67.8%</span>
            <br>
            
            
<span class="stars4 starstop" title="推荐">
    4星
</span>

            
<div class="power" style="width:24px"></div>

            <span class="rating_per">25.6%</span>
            <br>
            
            
<span class="stars3 starstop" title="还行">
    3星
</span>

            
<div class="power" style="width:5px"></div>

            <span class="rating_per">5.8%</span>
            <br>
            
            
<span class="stars2 starstop" title="较差">
    2星
</span>

            
<div class="power" style="width:0px"></div>

            <span class="rating_per">0.5%</span>
            <br>
            
            
<span class="stars1 starstop" title="很差">
    1星
</span>

            
<div class="power" style="width:0px"></div>

            <span class="rating_per">0.3%</span>
            <br>
    </div>
</div>

  </div>
  





  
    
    <div id="interest_sect_level" class="clearfix">
        <a href="#" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-6082808-wish">
          <span>
            
<form method="POST" action="https://www.douban.com/register?reason=collectwish" class="miniform">
    <input type="submit" class="minisubmit j  " value="想读" title="" />
</form>

          </span>
        </a>
        <a href="#" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-6082808-do">
          <span>
            
<form method="POST" action="https://www.douban.com/register?reason=collectdo" class="miniform">
    <input type="submit" class="minisubmit j  " value="在读" title="" />
</form>

          </span>
        </a>
        <a href="#" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-6082808-collect">
          <span>
            
<form method="POST" action="https://www.douban.com/register?reason=collectcollect" class="miniform">
    <input type="submit" class="minisubmit j  " value="读过" title="" />
</form>

          </span>
        </a>
      <div class="ll j a_stars">
        
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-6082808-1">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star1" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-6082808-2">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star2" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-6082808-3">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star3" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-6082808-4">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star4" width="16" height="16"/></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-6082808-5">
        <img src="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" id="star5" width="16" height="16"/></a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value=""  />
    </span>

      </div>
      

    </div>



  
  <div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">
        <li>
          <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;
          <a class="j a_show_login" href="https://book.douban.com/annotation/write?sid=6082808" rel="nofollow">写笔记</a>
        </li>

          <li>
            <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif" />&nbsp;<a class="j a_show_login" href="https://book.douban.com/subject/6082808/new_review" rel="nofollow">写书评</a>
          </li>

      <li>

  <span class="rr">
  

    <img src="https://img3.doubanio.com/pics/add-cart.gif"/>
      <a class="j a_show_login" href="http://http://www.douban.com/register?reason=addbook2cart" rel="nofollow">加入购书单</a>
  <span class="hidden">已在<a href="https://book.douban.com/cart">购书单</a></span>
</span><br class="clearfix" />
</li>


        
        
    
    <li class="rec" id="C-6082808">
        <a href="#" data-url="https://book.douban.com/subject/6082808/" data-desc="" data-title="书籍《百年孤独》 (来自豆瓣) " data-pic="https://img3.doubanio.com/view/subject/l/public/s6384944.jpg" class="bn-sharing ">分享到</a> &nbsp;&nbsp;
    </li>
    <script>
    var __cache_url = __cache_url || {};
    (function(u){
        if(__cache_url[u]) return;
        __cache_url[u] = true;
        window.DoubanShareIcons = 'https://img3.doubanio.com/f/shire/d15ffd71f3f10a7210448fec5a68eaec66e7f7d0/pics/ic_shares.png';
        var initShareButton = function() {
          $.ajax({url:u,dataType:'script',cache:true});
        };
        if (typeof Do == 'function' && 'ready' in Do) {
          Do('https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
            'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js',
            initShareButton);
        } else if(typeof Douban == 'object' && 'loader' in Douban) {
          Douban.loader.batch(
            'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
            'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js'
          ).done(initShareButton);
        }
    })('https://img3.doubanio.com/f/shire/6e6a5f21daeec19bbb41bf48c07fccaa4dad4d98/js/lib/sharebutton.js');
    </script>

    </ul>
  </div>


    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>


<script>
  //bind events for collection button.
  $('.collect_btn', '#interest_sect_level').each(function(){
      Douban.init_collect_btn(this);
  });
</script>








</div>

<br clear="all">
<div id="collect_form_6082808"></div>
<div class="related_info">
  






  

  <h2>
    <span class="">内容简介</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>



<div class="indent" id="link-report">
    
      <div class="">
        <style type="text/css" media="screen">
.intro p{text-indent:2em;word-break:normal;}
</style>
<div class="intro">
    <p>《百年孤独》是魔幻现实主义文学的代表作，描写了布恩迪亚家族七代人的传奇故事，以及加勒比海沿岸小镇马孔多的百年兴衰，反映了拉丁美洲一个世纪以来风云变幻的历史。作品融入神话传说、民间故事、宗教典故等神秘因素，巧妙地糅合了现实与虚幻，展现出一个瑰丽的想象世界，成为20世纪最重要的经典文学巨著之一。1982年加西亚•马尔克斯获得诺贝尔文学奖，奠定世界级文学大师的地位，很大程度上乃是凭借《百年孤独》的巨大影响。</p></div>

      </div>
    
<link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/c4c6dd266f58b41cbeebc9e4e6d7dd7b2a5c3711/css/report.css" />
<link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" />
<link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/b45aa277f8b8df40596b96582dafb1ed0a899a64/css/report_dialog.css" />
<script type="text/javascript" src="https://img3.doubanio.com/f/shire/a14501790b4a2db257dc5be5e37d820e600703c6/js/report_dialog.js"></script>
<style>
    #link-report .report { text-align: right; font-size: 12px; visibility: hidden; }
    #link-report .report a { color: #BBB; }
    #link-report .report a:hover { color: #FFF; background-color: #BBB; }
</style>
<script>
    Do = (typeof Do === 'undefined')? $ : Do;
    Do(function(){
    $("body").delegate("#link-report", 'mouseenter mouseleave', function(e){
      switch (e.type) {
        case "mouseenter":
          $(this).find(".report").css('visibility', 'visible');
          break;
        case "mouseleave":
          $(this).find(".report").css('visibility', 'hidden');
          break;
      }
    });
    $("#link-report").delegate(".report a", 'click', function(e){
        e.preventDefault();
        var opt = "";
        var obj = $(e.target).closest('#link-report');
        var id = obj.length != 0 ? obj.data("id") : undefined;
        var params = (opt&&id) ? ''.concat(opt, '=', id) : '';

        var url = "https://book.douban.com/subject/6082808/";
        url += (~url.indexOf('?') ? '&' : '?') + params
        url = url.replace(/\&+/g, '&')
        generate_report_dialog({report_url: url, type: 'subject'});
    });

    $("#link-report").append('<div class="report"><a rel="nofollow" href="#">举报</a></div>');
  });
</script>

</div>

  

























    
  

  <h2>
    <span class="">作者简介</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>



      <div class="indent ">
          
            <div class="">
            <style type="text/css" media="screen">
.intro p{text-indent:2em;word-break:normal;}
</style>
<div class="intro">
    <p>加西亚•马尔克斯（Gabriel García Márquez）1927年出生于哥伦比亚马格达莱纳海滨小镇阿拉卡塔卡。童年与外祖父母一起生活。1936年随父母迁居苏克雷。1947年考入波哥大国立大学。1948年因内战辍学，进入报界。五十年代开始发表文学作品。六十年代初移居墨西哥。1967年出版《百年孤独》。1982年获诺贝尔文学奖。</p></div>

            </div>
      </div>











































  

  


  


<link rel="stylesheet" href="https://img3.doubanio.com/f/verify/16c7e943aee3b1dc6d65f600fcc0f6d62db7dfb4/entry_creator/dist/author_subject/style.css">

<div id="author_subject" class="author-wrapper">
  <div class="loading"></div>
</div>

<script type="text/javascript">
  var answerObj = {
    TYPE: 'book',
    SUBJECT_ID: '6082808',
    ISALL: 'False' || false,
    USER_ID: 'None'
  }
</script>
<script src="https://img3.doubanio.com/f/book/61252f2f9b35f08b37f69d17dfe48310dd295347/js/book/lib/react/bundle.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/verify/ac140ef86262b845d2be7b859e352d8196f3f6d4/entry_creator/dist/author_subject/index.js"></script> 
  






<div id="db-tags-section" class="blank20">
  
  

  <h2>
    <span class="">豆瓣成员常用的标签(共4757个)</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>


  <div class="indent">    <span class="">
        <a class="  tag" href="/tag/百年孤独">百年孤独</a> &nbsp;    </span>
    <span class="">
        <a class="  tag" href="/tag/加西亚·马尔克斯">加西亚·马尔克斯</a> &nbsp;    </span>
    <span class="">
        <a class="  tag" href="/tag/经典">经典</a> &nbsp;    </span>
    <span class="">
        <a class="  tag" href="/tag/拉美文学">拉美文学</a> &nbsp;    </span>
    <span class="">
        <a class="  tag" href="/tag/魔幻现实主义">魔幻现实主义</a> &nbsp;    </span>
    <span class="">
        <a class="  tag" href="/tag/外国文学">外国文学</a> &nbsp;    </span>
    <span class="">
        <a class="  tag" href="/tag/小说">小说</a> &nbsp;    </span>
    <span class="">
        <a class="  tag" href="/tag/文学">文学</a> &nbsp;    </span>
  </div>
</div>


  


<div class="subject_show block5">
<h2>丛书信息</h2>
<div>
　　<a href="https://book.douban.com/series/10489">新经典文库:加西亚·马尔克斯作品 (共26册)</a>,
这套丛书还有
《世上最美的溺水者》,《米格尔在智利的地下行动》,《没有人给他写信的上校》,《礼拜二午睡时刻》,《一桩事先张扬的凶杀案》    等。</div>
</div>
<script>
$(function(){$(".knnlike a").click(function(){return moreurl(this,{'from':'knnlike'})})})
</script>

  












<div id="rec-ebook-section" class="block5 subject_show">
  

  
  

  <h2>
    <span class="">喜欢读&#34;百年孤独&#34;的人也喜欢的电子书</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>


  <div class="tips-mod">
    支持 Web、iPhone、iPad、Android 阅读器
  </div>
  <div class="content clearfix">
      
      <dl>
        <dt>
          <a href="https://read.douban.com/ebook/1162265/?dcs=subject-rec&amp;dcm=douban&amp;dct=6082808" target="_blank">
            <span class="cover-outer">
              <img src="https://img3.doubanio.com/view/ark_article_cover/retina/public/1162265.jpg?v=0">
            </span>
          </a>
        </dt>
        <dd>
          <div class="title">
              <a href="https://read.douban.com/ebook/1162265/" target="_blank">追风筝的人</a>
          </div>
          <div class="price">
              8.99元
          </div>
        </dd>
      </dl>
      
      <dl>
        <dt>
          <a href="https://read.douban.com/ebook/1610056/?dcs=subject-rec&amp;dcm=douban&amp;dct=6082808" target="_blank">
            <span class="cover-outer">
              <img src="https://img3.doubanio.com/view/ark_article_cover/retina/public/1610056.jpg?v=0">
            </span>
          </a>
        </dt>
        <dd>
          <div class="title">
              <a href="https://read.douban.com/ebook/1610056/" target="_blank">看见</a>
          </div>
          <div class="price">
              6.99元
          </div>
        </dd>
      </dl>
      
      <dl>
        <dt>
          <a href="https://read.douban.com/ebook/30541512/?dcs=subject-rec&amp;dcm=douban&amp;dct=6082808" target="_blank">
            <span class="cover-outer">
              <img src="https://img3.doubanio.com/view/ark_article_cover/retina/public/30541512.jpg?v=0">
            </span>
          </a>
        </dt>
        <dd>
          <div class="title">
              <a href="https://read.douban.com/ebook/30541512/" target="_blank">活着</a>
          </div>
          <div class="price">
              19.99元
          </div>
        </dd>
      </dl>
      
      <dl>
        <dt>
          <a href="https://read.douban.com/ebook/407582/?dcs=subject-rec&amp;dcm=douban&amp;dct=6082808" target="_blank">
            <span class="cover-outer">
              <img src="https://img3.doubanio.com/view/ark_article_cover/retina/public/407582.jpg?v=0">
            </span>
          </a>
        </dt>
        <dd>
          <div class="title">
              <a href="https://read.douban.com/ebook/407582/" target="_blank">少年PI的奇幻漂流（插图珍藏版）</a>
          </div>
          <div class="price">
              5.99元
          </div>
        </dd>
      </dl>
      
      <dl>
        <dt>
          <a href="https://read.douban.com/ebook/1362753/?dcs=subject-rec&amp;dcm=douban&amp;dct=6082808" target="_blank">
            <span class="cover-outer">
              <img src="https://img3.doubanio.com/view/ark_article_cover/retina/public/1362753.jpg?v=0">
            </span>
          </a>
        </dt>
        <dd>
          <div class="title">
              <a href="https://read.douban.com/ebook/1362753/" target="_blank">你一定爱读的极简欧洲史</a>
          </div>
          <div class="price">
              5.99元
          </div>
        </dd>
      </dl>
  </div>
</div>

<div id="db-rec-section" class="block5 subject_show knnlike">
  
  
  

  <h2>
    <span class="">喜欢读&#34;百年孤独&#34;的人也喜欢</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>


  <div class="content clearfix">
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/10594787/" onclick="moreurl(this, {'total': 10, 'clicked': '10594787', 'pos': 0, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img3.doubanio.com/view/subject/l/public/s11284102.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/10594787/" onclick="moreurl(this, {'total': 10, 'clicked': '10594787', 'pos': 0, 'identifier': 'book-rec-books'})" class="">
            霍乱时期的爱情
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/1084336/" onclick="moreurl(this, {'total': 10, 'clicked': '1084336', 'pos': 1, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img3.doubanio.com/view/subject/l/public/s1103152.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/1084336/" onclick="moreurl(this, {'total': 10, 'clicked': '1084336', 'pos': 1, 'identifier': 'book-rec-books'})" class="">
            小王子
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/1008145/" onclick="moreurl(this, {'total': 10, 'clicked': '1008145', 'pos': 2, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img3.doubanio.com/view/subject/l/public/s1070222.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/1008145/" onclick="moreurl(this, {'total': 10, 'clicked': '1008145', 'pos': 2, 'identifier': 'book-rec-books'})" class="">
            围城
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/2567698/" onclick="moreurl(this, {'total': 10, 'clicked': '2567698', 'pos': 3, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img1.doubanio.com/view/subject/l/public/s2768378.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/2567698/" onclick="moreurl(this, {'total': 10, 'clicked': '2567698', 'pos': 3, 'identifier': 'book-rec-books'})" class="">
            三体
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/3259440/" onclick="moreurl(this, {'total': 10, 'clicked': '3259440', 'pos': 4, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img3.doubanio.com/view/subject/l/public/s4610502.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/3259440/" onclick="moreurl(this, {'total': 10, 'clicked': '3259440', 'pos': 4, 'identifier': 'book-rec-books'})" class="">
            白夜行
          </a>
        </dd>
      </dl>
        <dl class="clear"></dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/1007305/" onclick="moreurl(this, {'total': 10, 'clicked': '1007305', 'pos': 5, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img1.doubanio.com/view/subject/l/public/s1070959.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/1007305/" onclick="moreurl(this, {'total': 10, 'clicked': '1007305', 'pos': 5, 'identifier': 'book-rec-books'})" class="">
            红楼梦
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/4820710/" onclick="moreurl(this, {'total': 10, 'clicked': '4820710', 'pos': 6, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img1.doubanio.com/view/subject/l/public/s4371408.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/4820710/" onclick="moreurl(this, {'total': 10, 'clicked': '4820710', 'pos': 6, 'identifier': 'book-rec-books'})" class="">
            1984
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/25862578/" onclick="moreurl(this, {'total': 10, 'clicked': '25862578', 'pos': 7, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img3.doubanio.com/view/subject/l/public/s27264181.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/25862578/" onclick="moreurl(this, {'total': 10, 'clicked': '25862578', 'pos': 7, 'identifier': 'book-rec-books'})" class="">
            解忧杂货店
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/4908885/" onclick="moreurl(this, {'total': 10, 'clicked': '4908885', 'pos': 8, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img3.doubanio.com/view/subject/l/public/s4468484.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/4908885/" onclick="moreurl(this, {'total': 10, 'clicked': '4908885', 'pos': 8, 'identifier': 'book-rec-books'})" class="">
            局外人
          </a>
        </dd>
      </dl>
      
      <dl class="">
        <dt>
            <a href="https://book.douban.com/subject/3066477/" onclick="moreurl(this, {'total': 10, 'clicked': '3066477', 'pos': 9, 'identifier': 'book-rec-books'})"><img class="m_sub_img" src="https://img3.doubanio.com/view/subject/l/public/s3078482.jpg"/></a>
        </dt>
        <dd>
          <a href="https://book.douban.com/subject/3066477/" onclick="moreurl(this, {'total': 10, 'clicked': '3066477', 'pos': 9, 'identifier': 'book-rec-books'})" class="">
            三体Ⅱ
          </a>
        </dd>
      </dl>
        <dl class="clear"></dl>
  </div>
</div>

  






    <link rel="stylesheet" href="https://img3.doubanio.com/f/book/3ec79645ad5a5d15c9ead3c58da97f5d662c7400/css/book/subject/comment.css"/>
    <div class="mod-hd">
        

        <a class="redbutt j a_show_login rr" href="https://www.douban.com/register?reason=review" rel="nofollow">
            <span> 我来说两句 </span>
        </a>

            
  

  <h2>
    <span class="">短评</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
      <span class="pl">&nbsp;(
          <a href="https://book.douban.com/subject/6082808/comments/">全部 62591 条</a>
        ) </span>

  </h2>


    </div>
    <div class="nav-tab">
        
    <div class="tabs-wrapper  line">
        <a class="short-comment-tabs on-tab" href="hot" data-tab="hot">热门</a>
        <span>/</span>
        <a class="short-comment-tabs " href="new" data-tab="new">最新</a>
        <span>/</span>
        <a class="j a_show_login " href="follows" data-tab="follows">好友</a>
    </div>

    </div>
    <div id="comment-list-wrapper" class="indent">
        

<div id="comments" class="comment-list hot show">
        <ul>
                
    <li class="comment-item" data-cid="675961865">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-675961865" class="vote-count">409</span>
                        <a href="javascript:;" id="btn-675961865" class="j a_show_login" data-cid="675961865">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/linyouchen/">Gala</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2013-05-04</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">庆幸是在我22岁的时候读到，没有太晚</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="569051613">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-569051613" class="vote-count">698</span>
                        <a href="javascript:;" id="btn-569051613" class="j a_show_login" data-cid="569051613">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/luffyjun/">Luffyjun</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2012-08-16</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">一开始我还为华丽的辞藻，荒诞的情节，冗长的姓氏感到烦躁不堪，但随着故事的深入展开，我才发现我错了。那么繁复的一大家庭，七代人的辉煌与落寞，激情与孤独，坚毅与懒惰，世俗与超脱，疯狂与冷静，就这样蔓延开来……叫人感慨的同时不禁也要叹惜一下，孤独的何止是百年</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="394307982">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-394307982" class="vote-count">1231</span>
                        <a href="javascript:;" id="btn-394307982" class="j a_show_login" data-cid="394307982">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/enhai/">[已注销]</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2014-07-04</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">一口气读完但却没有能力评价。</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="536750865">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-536750865" class="vote-count">790</span>
                        <a href="javascript:;" id="btn-536750865" class="j a_show_login" data-cid="536750865">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/xiacat/">獅</a>
                        <span class="user-stars allstar40 rating" title="推荐"></span>
                    <span>2012-05-28</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">家族谱太混乱，刚看的时候觉得：这么丧尸居然能是名著。看完以后觉得：这么丧尸不是名著太他妈浪费了...</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="805736834">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-805736834" class="vote-count">342</span>
                        <a href="javascript:;" id="btn-805736834" class="j a_show_login" data-cid="805736834">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/grace_summer/">Caramel_Grace</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2014-05-11</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">伟大的小说便是这样，倾注了作者全部的精神和价值重塑一个世界。而人物、情节、文笔、风格不过是帮助组织架构这伟大工程的工具。原来以为会读不下去，但一开页则根本停不下来。翻译也很加分。</span>
            </p>
        </div>
    </li>


        </ul>
</div>

        

<div id="comments" class="comment-list new noshow">
        <ul>
                
    <li class="comment-item" data-cid="1805341202">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-1805341202" class="vote-count">0</span>
                        <a href="javascript:;" id="btn-1805341202" class="j a_show_login" data-cid="1805341202">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/195893067/">crab的OKAMI</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2019-05-31</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">不好意思打低分，但当年确实看不懂</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="1805339913">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-1805339913" class="vote-count">0</span>
                        <a href="javascript:;" id="btn-1805339913" class="j a_show_login" data-cid="1805339913">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/162280132/">一只豌豆荚</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2019-05-31</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">在博卡拉的小舟上读书。。。当年的我是怎么想的 现在出行完全没了看书的兴致</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="1805329241">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-1805329241" class="vote-count">0</span>
                        <a href="javascript:;" id="btn-1805329241" class="j a_show_login" data-cid="1805329241">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/139063809/">诺曼底灯鹿</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2019-05-31</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">画了族谱来方便记忆和理清关系。神作</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="1805309078">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-1805309078" class="vote-count">0</span>
                        <a href="javascript:;" id="btn-1805309078" class="j a_show_login" data-cid="1805309078">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/ybcj/">ybcj</a>
                        <span class="user-stars allstar30 rating" title="还行"></span>
                    <span>2019-05-31</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">不知道该怎么评价这本经典之作，反正看了一半我就看不下去了。</span>
            </p>
        </div>
    </li>

                
    <li class="comment-item" data-cid="1805287800">
        <div class="comment">
            <h3>
                <span class="comment-vote">
                    <span id="c-1805287800" class="vote-count">0</span>
                        <a href="javascript:;" id="btn-1805287800" class="j a_show_login" data-cid="1805287800">有用</a>
                </span>
                <span class="comment-info">
                    <a href="https://www.douban.com/people/153898254/">点点点点</a>
                        <span class="user-stars allstar50 rating" title="力荐"></span>
                    <span>2019-05-31</span>
                </span>
            </h3>
            <p class="comment-content">
            
                <span class="short">今天完成新版 家里面还有两本老版 对百年孤独我真没什么好评价的了 且读且珍惜 上帝写本书不容易</span>
            </p>
        </div>
    </li>


        </ul>
</div>

    </div>
        <p>&gt; <a href="https://book.douban.com/subject/6082808/comments/">更多短评 62591 条</a></p>
    <script src="https://img3.doubanio.com/f/book/f334de0b97baf7506d0c181ff24dc61f9a7fca64/js/book/subject/short_comment_vote.js"></script>
    <script src="https://img3.doubanio.com/f/book/39eace58cab8aaeec45a44e878bf0ed06f2ed0a4/js/book/subject/short_comment_nav.js"></script>
    <script>
        (function(){
            $('.comment-list').delegate('.vote-comment', 'click', function(e) {
                vote_comment(e);
            }).delegate('.delete-comment', 'click', function(e) {
                if (confirm('确定删除吗？')) {
                    delete_comment(e);
                }
            });
        })();
    </script>

  

<link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/5b893040c800d5cd.css">

<section class="topics mod">
    <header>
        <h2>
            百年孤独的话题 · · · · · ·
            <span class="pl">( <span class="gallery_topics">全部 <span id="topic-count"></span> 条</span> )</span>
        </h2>
    </header>

    




<section class="subject-topics">
    <div class="topic-guide" id="topic-guide">
        <img class="ic_question" src="//img3.doubanio.com/f/ithildin/b1a3edea3d04805f899e9d77c0bfc0d158df10d5/pics/export/icon_question.png">
        <div class="tip_content">
            <div class="tip_title">什么是话题</div>
            <div class="tip_desc">
                <div>无论是一部作品、一个人，还是一件事，都往往可以衍生出许多不同的话题。将这些话题细分出来，分别进行讨论，会有更多收获。</div>
            </div>
        </div>
        <img class="ic_guide" src="//img3.doubanio.com/f/ithildin/529f46d86bc08f55cd0b1843d0492242ebbd22de/pics/export/icon_guide_arrow.png">
        <img class="ic_close" id="topic-guide-close" src="//img3.doubanio.com/f/ithildin/2eb4ad488cb0854644b23f20b6fa312404429589/pics/export/close@3x.png">
    </div>

    <div id="topic-items"></div>

    <script>
        window.subject_id = 6082808;
        window.join_label_text = '写书评参与';

        window.topic_display_count = 4;
        window.topic_item_display_count = 1;
        window.no_content_fun_call_name = "no_topic";

        window.guideNode = document.getElementById('topic-guide');
        window.guideNodeClose = document.getElementById('topic-guide-close');
    </script>
    
        <link rel="stylesheet" href="https://img3.doubanio.com/f/ithildin/f731c9ea474da58c516290b3a6b1dd1237c07c5e/css/export/subject_topics.css">
        <script src="https://img3.doubanio.com/f/ithildin/d3590fc6ac47b33c804037a1aa7eec49075428c8/js/export/moment-with-locales-only-zh.js"></script>
        <script src="https://img3.doubanio.com/f/ithildin/c600fdbe69e3ffa5a3919c81ae8c8b4140e99a3e/js/export/subject_topics.js"></script>

</section>

    <script>
        function no_topic(){
            $('#content .topics').remove();
        }
    </script>
</section>

<section class="reviews mod book-content">
    <header>
        <a href="new_review" rel="nofollow" class="create-review redbutt rr "
            data-isverify="False"
            data-verify-url="https://www.douban.com/accounts/phone/verify?redir=https://book.douban.com/subject/6082808/new_review">
            <span>我要写书评</span>
        </a>
        <h2>
            百年孤独的书评 · · · · · ·
            <span class="pl">( <a href="reviews">全部 3898 条</a> )</span>
        </h2>
    </header>

    

<style>
#gallery-topics-selection {
  position: fixed;
  width: 595px;
  padding: 40px 40px 33px 40px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 16px 0 rgba(0, 0, 0, 0.2);
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  z-index: 9999;
}
#gallery-topics-selection h1 {
  font-size: 18px;
  color: #007722;
  margin-bottom: 36px;
  padding: 0;
  line-height: 28px;
  font-weight: normal;
}
#gallery-topics-selection .gl_topics {
  border-bottom: 1px solid #dfdfdf;
  max-height: 298px;
  overflow-y: scroll;
}
#gallery-topics-selection .topic {
  margin-bottom: 24px;
}
#gallery-topics-selection .topic_name {
  font-size: 15px;
  color: #333;
  margin: 0;
  line-height: inherit;
}
#gallery-topics-selection .topic_meta {
  font-size: 13px;
  color: #999;
}
#gallery-topics-selection .topics_skip {
  display: block;
  cursor: pointer;
  font-size: 16px;
  color: #3377AA;
  text-align: center;
  margin-top: 33px;
}
#gallery-topics-selection .topics_skip:hover {
  background: transparent;
}
#gallery-topics-selection .close_selection {
  position: absolute;
  width: 30px;
  height: 20px;
  top: 46px;
  right: 40px;
  background: #fff;
  color: #999;
  text-align: right;
}
#gallery-topics-selection .close_selection:hover{
  background: #fff;
  color: #999;
}
</style>




        <div class="review_filter">
            <a href="javascript:;;" class="cur" data-sort="">热门</a href="javascript:;;"> /
            <a href="javascript:;;" data-sort="time">最新</a href="javascript:;;"> /
            <a href="javascript:;;" data-sort="follow">好友</a href="javascript:;;">
            
        </div>


        



<div class="review-list  ">
        
    

        
    
    <div data-cid="1109738">
        <div class="main review-item" id="1109738">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/icekiller/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1325437-126.jpg">
        </a>

        <a href="https://www.douban.com/people/icekiller/" class="name">阿落</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2007-01-10" class="main-meta">2007-01-10 15:52:57</span>


            <span class="publisher right">
                <a class="publisher" target="_blank" href="https://book.douban.com/subject/1786670/">上海译文出版社1989版</a>
            </span>
    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/1109738/">在你觉得阅读困难的时候千万不要勉强</a></h2>

                <div id="review_1109738_short" class="review-short" data-rid="1109738">
                    <div class="short-content">

                        面对这样的作品，当你没有能力读它的时候，千万不要试图去读懂。不要逼自己去面对那些看似纷乱的情节，不要强迫自己搞清楚那一代又一代的人物关系，不要翻来覆去的理清某些相似的名字不同的人物。这些屏障存在于那里，已经说明你无须去读它，起码是当下，无须去读。就像高中的...

                        &nbsp;(<a href="javascript:;" id="toggle-1109738-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1109738_full" class="hidden">
                    <div id="review_1109738_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1109738" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1109738">
                                8627
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1109738" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1109738">
                                697
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/1109738/#comments" class="reply ">892回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="3000399">
        <div class="main review-item" id="3000399">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/Sising/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1038143-42.jpg">
        </a>

        <a href="https://www.douban.com/people/Sising/" class="name">菠菜</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2010-02-19" class="main-meta">2010-02-19 16:40:34</span>


            <span class="publisher right">
                <a class="publisher" target="_blank" href="https://book.douban.com/subject/1786670/">上海译文出版社1989版</a>
            </span>
    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/3000399/">无孤独不浪漫</a></h2>

                <div id="review_3000399_short" class="review-short" data-rid="3000399">
                    <div class="short-content">

                        家族中的第一人被绑在树上，家族中的最后一人被蚂蚁吃掉。  该用什么样的眼光来看待布恩地亚家族呢？漫长的几代人之中，有手艺灵巧的、有求知旺盛的、有聪明机灵的、有勇敢坚强的、有吃苦耐劳的、有光彩照人的……他们有坚毅的眼光，不轻易言败的性格，无论是旅途劳顿的南征北...

                        &nbsp;(<a href="javascript:;" id="toggle-3000399-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_3000399_full" class="hidden">
                    <div id="review_3000399_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="3000399" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-3000399">
                                5077
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="3000399" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-3000399">
                                396
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/3000399/#comments" class="reply ">338回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="5750661">
        <div class="main review-item" id="5750661">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/60811255/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u60811255-2.jpg">
        </a>

        <a href="https://www.douban.com/people/60811255/" class="name">而已</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2013-01-22" class="main-meta">2013-01-22 11:43:42</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/5750661/">那些关于时间和孤独故事</a></h2>

                <div id="review_5750661_short" class="review-short" data-rid="5750661">
                    <div class="short-content">

                        坦白说这是我近几年来花最多时间去读的一本书，近两个月的时间--回肠荡气、满腹沉重、欲罢不能。知道自己才疏学浅，为这样的小说写笔记不免有些班门弄斧的嫌疑，但是不写实在是对不住我两个月读了这样一本好书，好在笔记只是自己的笔记而已。喜欢这本书的，看过了就过了，没有...

                        &nbsp;(<a href="javascript:;" id="toggle-5750661-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_5750661_full" class="hidden">
                    <div id="review_5750661_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="5750661" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-5750661">
                                4734
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="5750661" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-5750661">
                                171
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/5750661/#comments" class="reply ">566回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="1210834">
        <div class="main review-item" id="1210834">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/1812564/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1812564-1.jpg">
        </a>

        <a href="https://www.douban.com/people/1812564/" class="name">茉莉</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2007-09-20" class="main-meta">2007-09-20 19:07:23</span>


            <span class="publisher right">
                <a class="publisher" target="_blank" href="https://book.douban.com/subject/1786670/">上海译文出版社1989版</a>
            </span>
    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/1210834/">马尔克斯妻子写的《百年孤独》</a></h2>

                <div id="review_1210834_short" class="review-short" data-rid="1210834">
                    <div class="short-content">

                          马尔克斯的《百年孤独》使他成为拉丁美洲的骄傲。也让他获得了世界级的声望。《霍乱时期的爱情》使他得到了1982年的诺贝尔文学奖。  在他沉着冷静地讲着一些令人毛骨悚然或者幽默荒谬的故事的时候，他的背后也有一个人，一个如他笔下所写的那个魔幻现实主义世界中，坚定地站...

                        &nbsp;(<a href="javascript:;" id="toggle-1210834-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1210834_full" class="hidden">
                    <div id="review_1210834_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1210834" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1210834">
                                2180
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1210834" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1210834">
                                78
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/1210834/#comments" class="reply ">211回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="4976722">
        <div class="main review-item" id="4976722">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/zhaoxianghui/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u2477310-6.jpg">
        </a>

        <a href="https://www.douban.com/people/zhaoxianghui/" class="name">Rilke</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2011-06-04" class="main-meta">2011-06-04 23:27:24</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/4976722/">三种译本的段落对照</a></h2>

                <div id="review_4976722_short" class="review-short" data-rid="4976722">
                    <div class="short-content">

                        一 南海出版公司范晔版：多年以后，面对行刑队，奥里雷亚诺.布恩迪亚上校将会回想起父亲带他去见识冰块的那个遥远的下午。那时的马孔多是一个二十户人家的村落，泥巴和芦苇盖成的屋子沿河岸排开，湍急的河水清澈见底，河床里卵石洁白光滑宛如史前巨蛋。世界新生伊始，许多事物...

                        &nbsp;(<a href="javascript:;" id="toggle-4976722-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_4976722_full" class="hidden">
                    <div id="review_4976722_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="4976722" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-4976722">
                                2105
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="4976722" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-4976722">
                                219
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/4976722/#comments" class="reply ">790回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="6172634">
        <div class="main review-item" id="6172634">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/3064233/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/u3064233-99.jpg">
        </a>

        <a href="https://www.douban.com/people/3064233/" class="name">石头摇篮</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2013-07-20" class="main-meta">2013-07-20 23:38:20</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/6172634/">《百年孤独》之冰块、孤独与人物</a></h2>

                <div id="review_6172634_short" class="review-short" data-rid="6172634">
                    <div class="short-content">

                        读《百年孤独》前便有充分心理准备：小说纵跨百年，七代人，人多，名字都很长，长得还都很像，布恩迪亚家族给新生儿命名总是翻来覆去叫“奥雷里亚诺”或者“何赛·阿尔卡蒂奥”，一堆酷似或者干脆一样的名字听说是很多人怕读和读不下去的重要原因。于是从翻开《百年孤独》起，...

                        &nbsp;(<a href="javascript:;" id="toggle-6172634-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_6172634_full" class="hidden">
                    <div id="review_6172634_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="6172634" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-6172634">
                                1821
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="6172634" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-6172634">
                                117
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/6172634/#comments" class="reply ">278回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="6789680">
        <div class="main review-item" id="6789680">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/GayScript/" class="avator">
            <img width="24" height="24" src="https://img1.doubanio.com/icon/user_normal.jpg">
        </a>

        <a href="https://www.douban.com/people/GayScript/" class="name">[已注销]</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2014-08-03" class="main-meta">2014-08-03 17:56:03</span>


            <span class="publisher right">
                <a class="publisher" target="_blank" href="https://book.douban.com/subject/1786670/">上海译文出版社1989版</a>
            </span>
    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/6789680/">如何阅读马尔克斯的《百年孤独》</a></h2>

                <div id="review_6789680_short" class="review-short" data-rid="6789680">
                    <div class="short-content">

                        年轻人最大的毛病是什么，是浮躁。这种浮躁无处不在。比方说，听别人传闻一本好书，也想去看，看了点看不下去，就想问别人怎么看这本书。想找个捷径赶紧看完，而不是想要自己慢慢摸索。仿佛目的只是为了快点读完这本书，好告诉别人我看过了，并不是真要细细欣赏。   同样的例子...

                        &nbsp;(<a href="javascript:;" id="toggle-6789680-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_6789680_full" class="hidden">
                    <div id="review_6789680_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="6789680" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-6789680">
                                835
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="6789680" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-6789680">
                                31
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/6789680/#comments" class="reply ">96回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="1787908">
        <div class="main review-item" id="1787908">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/spiritualistz81/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1973158-3.jpg">
        </a>

        <a href="https://www.douban.com/people/spiritualistz81/" class="name">Claudia</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2009-03-03" class="main-meta">2009-03-03 20:13:11</span>


            <span class="publisher right">
                <a class="publisher" target="_blank" href="https://book.douban.com/subject/1786670/">上海译文出版社1989版</a>
            </span>
    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/1787908/">除了孤独，我一无所有</a></h2>

                <div id="review_1787908_short" class="review-short" data-rid="1787908">
                    <div class="short-content">

                        我对所有事情都有兴趣，所以我经常上当，在一个冷漠的社会里，你的热情在他们眼睛里就是不成熟。他们为面子活，你为兴趣活，你觉得你这样很开心，他们觉得你很无聊；你觉得你很真诚，他们觉得你在标榜自己。所以，我现在即使有兴趣也会装做“平常心”的样子，只是为了满足大多...

                        &nbsp;(<a href="javascript:;" id="toggle-1787908-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_1787908_full" class="hidden">
                    <div id="review_1787908_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="1787908" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-1787908">
                                798
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="1787908" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-1787908">
                                69
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/1787908/#comments" class="reply ">164回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="5018539">
        <div class="main review-item" id="5018539">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/yinchouyunv/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1417723-31.jpg">
        </a>

        <a href="https://www.douban.com/people/yinchouyunv/" class="name">引愁玉女</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2011-07-10" class="main-meta">2011-07-10 19:44:26</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/5018539/">不会再次出现的体验</a></h2>

                <div id="review_5018539_short" class="review-short" data-rid="5018539">
                    <div class="short-content">

                                多年以后，面对正式授权的《百年孤独》，我不禁会回想起青春年月初读这本书的光景。那时的我刚刚进入高中，学校里破旧的读书馆每周开放一次，我得以在无数泛黄的上世纪八十年代的旧书堆里找出一些似曾相识的书来读。这些名字不知是何时驻扎在脑海里，在功课负担日益沉...

                        &nbsp;(<a href="javascript:;" id="toggle-5018539-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_5018539_full" class="hidden">
                    <div id="review_5018539_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="5018539" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-5018539">
                                470
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="5018539" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-5018539">
                                51
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/5018539/#comments" class="reply ">97回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="5076687">
        <div class="main review-item" id="5076687">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/lengleng/" class="avator">
            <img width="24" height="24" src="https://img3.doubanio.com/icon/u1105865-81.jpg">
        </a>

        <a href="https://www.douban.com/people/lengleng/" class="name">琼斯黄</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2011-08-25" class="main-meta">2011-08-25 20:08:36</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://book.douban.com/review/5076687/">奥雷里亚诺，马孔多在下雨</a></h2>

                <div id="review_5076687_short" class="review-short" data-rid="5076687">
                    <div class="short-content">

                        没有比最近这些日子更合适的时间来重读《百年孤独》了。故乡下着一场连绵不断，眼看着不会终止的雨，我窝在自己的小屋里做着重复再重复的英文练习，很少上网，几乎断了和繁华世界的联系。这些长期的和暂时的，无意的和刻意的，外在的和内在的小小封闭，给了我一颗挨近马孔多的...

                        &nbsp;(<a href="javascript:;" id="toggle-5076687-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_5076687_full" class="hidden">
                    <div id="review_5076687_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="5076687" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png" />
                        <span id="r-useful_count-5076687">
                                391
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="5076687" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png" />
                        <span id="r-useless_count-5076687">
                                18
                        </span>
                    </a>
                    <a href="https://book.douban.com/review/5076687/#comments" class="reply ">76回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>




    

    

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/e4731bfabc0525d.js"></script>
    <!-- COLLECTED CSS -->
</div>








            <p class="pl">
                &gt;
                <a href="reviews">
                    更多书评3898篇
                </a>
            </p>
</section>

<!-- COLLECTED JS -->

  









<div class="ugc-mod reading-notes">
  <div class="hd">
    <h2>
      读书笔记&nbsp;&nbsp;· · · · · ·&nbsp;
          <span class="pl">(<a href="https://book.douban.com/subject/6082808/annotation">共<span property="v:count">4650</span>篇</a>)</span>

    </h2>

      <a class="redbutt rr j a_show_login" href="https://www.douban.com/register?reason=annotate" rel="nofollow"><span>我来写笔记</span></a>
  </div>
  

    <div class="bd">
      <ul class="inline-tabs">
        <li class="on"><a href="#rank" id="by_rank" >按有用程度</a></li>
        <li><a href="#page" id="by_page" >按页码先后</a></li>
        <li><a href="#time" id="by_time" >最新笔记</a></li>
      </ul>
      
  <ul class="comments by_rank" >
      
      <li class="ctsh clearfix" data-cid="19183684">
        <div class="ilst">
          <a href="https://www.douban.com/people/62398672/"><img src="https://img1.doubanio.com/icon/user_normal.jpg" alt="狮子豆豆" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/19183684/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/19183684/" class="">第1页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/62398672/" class=" " title="狮子豆豆">狮子豆豆</a>
              
            </p>
            <div class="reading-note" data-cid="19183684">
              <div class="short">
                
                  <span class=""> 【百年孤独】：无论走到哪里，都应该记住，过去都是假的，回忆是一条没有尽头的路，一切以往的春天都不复存在，就连那最坚韧而又狂乱的爱情归根结底也不过是一种转瞬即逝的现实。</span>
                  &nbsp;&nbsp;<a href="https://book.douban.com/annotation/19183684/">(<span class="">115回应</span>)</a>
                <p class="pl">
                  <span class="">2012-06-24 12:23</span>
                  
                    &nbsp;&nbsp;<span class="">2308人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                 【百年孤独】：无论走到哪里，都应该记住，过去都是假的，回忆是一条没有尽头的路，一切以往的春天都不复存在，就连那最坚韧而又狂乱的爱情归根结底也不过是一种转瞬即逝的现实。
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/19183684/#comments" class="">115回应</a>&nbsp;&nbsp;
                  2012-06-24 12:23
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="18142063">
        <div class="ilst">
          <a href="https://www.douban.com/people/eugenexu/"><img src="https://img1.doubanio.com/icon/u3327235-18.jpg" alt="徐公子～" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/18142063/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/18142063/" class="">第38页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/eugenexu/" class=" " title="徐公子～">徐公子～</a>
                (深深的话呀浅浅地说～)
              
                <span class="allstar50" title="力荐"></span>
            </p>
            <div class="reading-note" data-cid="18142063">
              <div class="short">
                
                  <span class="">失眠症最可怕之处不在于让人毫无倦意不能入睡，而是会不可逆转地恶化到更严重的境地：遗忘。也就是说，患者慢慢习惯了无眠的状态，就开始淡忘童年的记忆，继之以事物的名称和概念，最后是各人的身份，以至失去自我，沦为没有过往的白痴。</span>
                  &nbsp;&nbsp;<a href="https://book.douban.com/annotation/18142063/">(<span class="">69回应</span>)</a>
                <p class="pl">
                  <span class="">2012-05-05 14:40</span>
                  
                    &nbsp;&nbsp;<span class="">649人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                <blockquote><q>失眠症最可怕之处不在于让人毫无倦意不能入睡，而是会不可逆转地恶化到更严重的境地：遗忘。也就是说，患者慢慢习惯了无眠的状态，就开始淡忘童年的记忆，继之以事物的名称和概念，最后是各人的身份，以至失去自我，沦为没有过往的白痴。</q></blockquote>
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/18142063/#comments" class="">69回应</a>&nbsp;&nbsp;
                  2012-05-05 14:40
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="13203391">
        <div class="ilst">
          <a href="https://www.douban.com/people/chenzhuo/"><img src="https://img3.doubanio.com/icon/u1017379-74.jpg" alt="陈灼" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/13203391/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/13203391/" class="">第360页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/chenzhuo/" class=" " title="陈灼">陈灼</a>
              
                <span class="allstar50" title="力荐"></span>
            </p>
            <div class="reading-note" data-cid="13203391">
              <div class="short">
                
                  <div class="ll">
                    <a href="https://book.douban.com/annotation/13203391/"><img src="https://img3.doubanio.com/view/page_note/small/public/p13203391-3.jpg"></a>
                  </div>
                  <span class="">打个广告：

我的短篇小说合集在豆瓣阅读上架了！欢迎大家试阅。

<a rel="nofollow" href="https://read.douban.com/ebook/83139/">算法
</a>


我也来贴谱系，好玩~



<a rel="nofollow" href="http://ww1.sinaimg.cn/large/5b0a1b90jw1dhwjc4azztj.jpg" target="_blank">大图在这儿</a>


翻页：<a rel="nofollow" href="https://book.douban.com/annotation/13203391/?start=100">第二页
</a>
</span>
                  &nbsp;&nbsp;<a href="https://book.douban.com/annotation/13203391/">(<span class="">192回应</span>)</a>
                <p class="pl">
                  <span class="">2011-06-06 11:18</span>
                  
                    &nbsp;&nbsp;<span class="">754人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                打个广告：<div style="padding-bottom:1em;"></div>我的短篇小说合集在豆瓣阅读上架了！欢迎大家试阅。<div style="padding-bottom:1em;"></div><a rel="nofollow" href="https://read.douban.com/ebook/83139/">算法<div style="padding-bottom:1em;"></div></a><div style="padding-bottom:1em;"></div>我也来贴谱系，好玩~<div style="padding-bottom:1em;"></div><div class="left"><img src="https://img3.doubanio.com/view/page_note/large/public/p13203391-3.jpg" alt=""><br><span class="pic-title"></span></div><div style="padding-bottom:1em;"></div><a rel="nofollow" href="http://ww1.sinaimg.cn/large/5b0a1b90jw1dhwjc4azztj.jpg" target="_blank">大图在这儿</a><div style="padding-bottom:1em;"></div>翻页：<a rel="nofollow" href="https://book.douban.com/annotation/13203391/?start=100">第二页<div style="padding-bottom:1em;"></div></a><div style="padding-bottom:1em;"></div>
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/13203391/#comments" class="">192回应</a>&nbsp;&nbsp;
                  2011-06-06 11:18
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="17274833">
        <div class="ilst">
          <a href="https://www.douban.com/people/youngstein/"><img src="https://img3.doubanio.com/icon/u40645814-5.jpg" alt="快乐小超" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/17274833/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/17274833/" class="">第320页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/youngstein/" class=" " title="快乐小超">快乐小超</a>
                (吟啸徐行，闲庭信步)
              
                <span class="allstar40" title="推荐"></span>
            </p>
            <div class="reading-note" data-cid="17274833">
              <div class="short">
                
                  <span class="">孤独是相通的。
一个在自己的思想世界里遨游，整日里一个人勾画未来回忆过去的每个人都是孤独的。这么说来，大多数人都免不了孤独，因为真正的知己有几个，如果有人能够洞穿你的心思，有人能协同你的遭遇，有人能不懈关注你的动态，也许你并不孤独；但也许孤独的还是你，而不孤独的是那个人，因为他的世界是开放的，因为包容了你，而你的世界是封闭的，你的所观所感还是没有基于别人的体验和想法。
除非你是我，才可与我常在。每...</span>
                  &nbsp;&nbsp;<a href="https://book.douban.com/annotation/17274833/">(<span class="">26回应</span>)</a>
                <p class="pl">
                  <span class="">2012-03-15 09:02</span>
                  
                    &nbsp;&nbsp;<span class="">419人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                孤独是相通的。<div style="padding-bottom:1em;"></div>一个在自己的思想世界里遨游，整日里一个人勾画未来回忆过去的每个人都是孤独的。这么说来，大多数人都免不了孤独，因为真正的知己有几个，如果有人能够洞穿你的心思，有人能协同你的遭遇，有人能不懈关注你的动态，也许你并不孤独；但也许孤独的还是你，而不孤独的是那个人，因为他的世界是开放的，因为包容了你，而你的世界是封闭的，你的所观所感还是没有基于别人的体验和想法。<div style="padding-bottom:1em;"></div>除非你是我，才可与我常在。每个人都注定有孤独，只要愿意静下心来思索的人必然都深味过孤独。寻找伴侣的路途，其实只是求一个分享，求一个稳固的关系维系住相濡以沫共存共生的世界。<div style="padding-bottom:1em;"></div>实体的世界只占到了一个人生命的极小一部分，心的世界才占多数。
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/17274833/#comments" class="">26回应</a>&nbsp;&nbsp;
                  2012-03-15 09:02
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
  </ul>
  

      
  <ul class="comments by_page"  style="display: none">
      
      <li class="ctsh clearfix" data-cid="13157828">
        <div class="ilst">
          <a href="https://www.douban.com/people/4007978/"><img src="https://img3.doubanio.com/icon/u4007978-5.jpg" alt="湿花轻絮" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/13157828/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/13157828/" class="">第1页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/4007978/" class=" " title="湿花轻絮">湿花轻絮</a>
                (文具控、图书控、各种控)
              
            </p>
            <div class="reading-note" data-cid="13157828">
              <div class="short">
                
                  <span class="">多年以后，面对行刑队，奥雷里亚诺.布恩迪亚上校将会回想起父亲带他去见识冰块的那个遥远的下午。&lt;</span>
                  &nbsp;&nbsp;<a href="https://book.douban.com/annotation/13157828/">(<span class="">6回应</span>)</a>
                <p class="pl">
                  <span class="">2011-06-02 19:01</span>
                  
                    &nbsp;&nbsp;<span class="">7人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                <blockquote><q>多年以后，面对行刑队，奥雷里亚诺.布恩迪亚上校将会回想起父亲带他去见识冰块的那个遥远的下午。&lt;</q></blockquote>
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/13157828/#comments" class="">6回应</a>&nbsp;&nbsp;
                  2011-06-02 19:01
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="13170075">
        <div class="ilst">
          <a href="https://www.douban.com/people/1658419/"><img src="https://img1.doubanio.com/icon/u1658419-18.jpg" alt="海瑟薇妮" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/13170075/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/13170075/" class="">第1页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/1658419/" class=" " title="海瑟薇妮">海瑟薇妮</a>
                (无论如何要过积极向上的人生。)
              
            </p>
            <div class="reading-note" data-cid="13170075">
              <div class="short">
                
                  <span class="">人名：
奥雷里亚诺•布恩迪亚 上校

吉普赛人 梅尔基亚德斯



地名：

马孔多

“那时的马孔多是一个二十户人家的村落，泥巴和芦苇盖成的屋子沿河岸排开，湍急的河水清澈见底，河床里卵石洁白光滑宛如史前巨蛋。”</span>
                <p class="pl">
                  <span class="">2011-06-03 16:40</span>
                  
                    &nbsp;&nbsp;<span class="">3人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                人名：<div style="padding-bottom:1em;"></div>奥雷里亚诺•布恩迪亚 上校<div style="padding-bottom:1em;"></div>吉普赛人 梅尔基亚德斯<div style="padding-bottom:1em;"></div>地名：<div style="padding-bottom:1em;"></div>马孔多<div style="padding-bottom:1em;"></div>“那时的马孔多是一个二十户人家的村落，泥巴和芦苇盖成的屋子沿河岸排开，湍急的河水清澈见底，河床里卵石洁白光滑宛如史前巨蛋。”
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/13170075/#comments" class="">回应</a>&nbsp;&nbsp;
                  2011-06-03 16:40
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="13170718">
        <div class="ilst">
          <a href="https://www.douban.com/people/fm365bbs/"><img src="https://img3.doubanio.com/icon/u1027565-492.jpg" alt="盲刺客" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/13170718/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/13170718/" class="">第1页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/fm365bbs/" class=" " title="盲刺客">盲刺客</a>
                (废业中年，求睬若渴)
              
                <span class="allstar40" title="推荐"></span>
            </p>
            <div class="reading-note" data-cid="13170718">
              <div class="short">
                
                  <span class="">说说这本书的遗憾之处。

居然没有家族人物关系图。

对于这么纷繁的任人物关系，有那么个家族关系图是多么方便啊。

不过，也许这是我个人的爱好。我每次看到家族史的小说都要自己整理个人物关系图出来。</span>
                  &nbsp;&nbsp;<a href="https://book.douban.com/annotation/13170718/">(<span class="">18回应</span>)</a>
                <p class="pl">
                  <span class="">2011-06-03 17:31</span>
                  
                    &nbsp;&nbsp;<span class="">4人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                说说这本书的遗憾之处。<div style="padding-bottom:1em;"></div>居然没有家族人物关系图。<div style="padding-bottom:1em;"></div>对于这么纷繁的任人物关系，有那么个家族关系图是多么方便啊。<div style="padding-bottom:1em;"></div>不过，也许这是我个人的爱好。我每次看到家族史的小说都要自己整理个人物关系图出来。
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/13170718/#comments" class="">18回应</a>&nbsp;&nbsp;
                  2011-06-03 17:31
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="13179092">
        <div class="ilst">
          <a href="https://www.douban.com/people/louzhong/"><img src="https://img3.doubanio.com/icon/u1280797-14.jpg" alt="冬妮娅" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/13179092/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/13179092/" class="">第1页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/louzhong/" class=" " title="冬妮娅">冬妮娅</a>
                (地球牧场时期的打杂工)
              
                <span class="allstar20" title="较差"></span>
            </p>
            <div class="reading-note" data-cid="13179092">
              <div class="short">
                
                  <span class="">马尔克斯的悖论：马孔多

“多年以后，奥雷连诺上校站在行刑队面前，准会想起父亲带他去参观冰块的那个遥远的下午。”
――马尔克斯《百年孤独》

众所周知，《百年孤独》开头这一段，影响过无数文本的开头，小说理论家也热衷于对这个开头的津津乐道，自然这里面也有不乏非常精彩的论述，但是在这篇文章当中，我们不准备讨论这个开头，我们将就《百年孤独》来谈论小说中另一个问题：叙述的在场性问题。
关于在场性问题是詹姆...</span>
                  &nbsp;&nbsp;<a href="https://book.douban.com/annotation/13179092/">(<span class="">11回应</span>)</a>
                <p class="pl">
                  <span class="">2011-06-04 13:59</span>
                  
                    &nbsp;&nbsp;<span class="">66人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                马尔克斯的悖论：马孔多<div style="padding-bottom:1em;"></div>“多年以后，奥雷连诺上校站在行刑队面前，准会想起父亲带他去参观冰块的那个遥远的下午。”<div style="padding-bottom:1em;"></div>――马尔克斯《百年孤独》<div style="padding-bottom:1em;"></div>众所周知，《百年孤独》开头这一段，影响过无数文本的开头，小说理论家也热衷于对这个开头的津津乐道，自然这里面也有不乏非常精彩的论述，但是在这篇文章当中，我们不准备讨论这个开头，我们将就《百年孤独》来谈论小说中另一个问题：叙述的在场性问题。<div style="padding-bottom:1em;"></div>关于在场性问题是詹姆逊等人提出来的，而我们所熟悉的作品是被称为具有现代叙述意识的小说《包法利夫人》的开头：“我们正在上自习，忽然校长进来了，后面跟着一个没有穿学生装的新学生，还有一个小校工，却端着一张大书桌。正在打瞌睡的学生也醒过来了，个个站了起来，仿佛功课受到打扰似的。”至此，整个小说史上的“我”出现了。<div style="padding-bottom:1em;"></div>当然，“我”的出现，并不能保证绝对的在场，因为“我”也有虚妄的成分存在。你看《包法利夫人》后面的叙述对于在场仍然是不自觉的。我倒认为是福楼拜的在文学上主张的客观立场导致了文学史上这一“我”的出现。或许从他的学生左拉和莫泊桑等人身上更能够精确的看到这一点。而福楼拜的精神导师巴尔扎克更像是具有科学精神的小说社会学者和人类学家。不管怎样，“我”出现了，到后来的新小说派诸作家这里，归结为对“客观叙述”的忠诚――及物。人们曾经为意识流小说普鲁斯特、乔伊斯、安德烈•别雷、伍尔芙呐喊过，认为他们在作品中找到了绝对的在场，保证了绝对的“我”的在场，但是不久，人们开始对这种绝对主观在场性感到了厌倦，因为不管怎样，这仍然是虚妄的。所以新小说在恰当的时间和地点登上历时舞台（这里有一个很大的背景，新小说之前的小说史和法兰西在哲学上的盛典都是其根源，这可专门立一个命题来论述），他们声称要从主观场撤离，回到纯粹客观的在场，就像植物自己在生长一样，人的意志应该退场。所以我们看到了一张张照相机拍摄下来的图片，这就是小说。这种对自我意识的清理是有其积极意义的。但是我以为，这仍然是主观，仍然和意识流没有本质上的区别。罗伯－格里耶在谈到比喻的时候，说过一句话，给我印象非常深刻，他说“一切比喻都是泛神的”，也就是说在清理意识的介入的时候，前提是这个“我”从根本上是无法被清理掉的。我到觉得他从形而上把握了一个现象学家们研究的问题：现象即一切。这个现象根据胡塞尔的定义则是心物一元。因此，我们不得不重新回到“我”上来。<div style="padding-bottom:1em;"></div>关于在场问题我相信我完全说多了，《百年孤独》整个一部小说都是不在场的叙述，或许刚一开始，给人假象，以为是在场的，正如我们看到的开头，小说以奥雷连诺上校的视角进入叙述，但是在第三句子，作者又破坏以奥雷连诺上校的视角进行叙述的企图，将叙述权重新拿回自己的手上：“奥雷连诺上校……准会想起父亲带他去参观冰块的那个遥远的下午。”接下来，作者以我们熟悉的所谓全知全能的叙述方式展开小说的全部细节和故事。但是读到最后，你会看到一个奇怪的绝对惊人的结尾：这个里面的所有人物，关于马孔多的一切都被风刮走了，一干二净，更荒唐的是作者声称记录着马孔多一切奥秘的那本梵文密码书被破译了出来，但是也被刮走了……，到这里，任何不是白痴的人都看出来了。这是一个谎言，为什么呢？因为，作者本人也没有见过这本书，因为它被刮走了，马孔多破译此书的人也被刮走了，死了；然而小说的作者马尔克斯却能绘声绘色的描述出这本密码书的详细的全部内容，显然，这是一个天大的谎言、谬论、逻辑漏洞，这个“漏洞”至今没有人跟马尔克斯清算过。因为它被掩饰在“魔幻”这一巨大的光辉之下――尽管马尔克斯自己否认属于这个写作范畴，甚至那些评论家和仰慕者也笼罩在内。我们需要区别对待的是：作者内容上的拉丁美洲魔幻现实和小说叙述手法上的逻辑漏洞完全是两码事。实质上这不过是一个克里特岛人的谎言。细心的读者可以再回过头去看看《百年孤独》最后一章。相信你还会有更大的惊讶。从这点上看，《百年孤独》的叙述是不成熟的，缺乏最基本的现代小说叙事意识。<div style="padding-bottom:1em;"></div>我们不是有意去否定这部小说所展现出来的拉丁美洲的独特风情和马尔克斯要建立马孔多的良苦用心；如果把它当一个传奇故事，这仍然是一个很妙的具有可读性的文本；试想，《天方夜谭》不荒唐吗？荒唐，但是却美妙无比。对于马尔克斯，或许可以再再拔高一点，只有把《百年孤独》当作寓言和初级神话才可以被理解。《天方夜谭》提供的叙述学动力问题至今都令人赞叹不已。一个基本前提，纯粹讲述的故事，要有绝对的魅力保证听众（苏丹）毫不犹豫的听下去。否则就是死亡――砍头。叙述的极致，这是。叙述和死亡是同等的。山鲁佐德的讲述也提供了一种叙述形式，是小说叙述上的动力学之一个值得深究的范例。<div style="padding-bottom:1em;"></div>马尔克斯的叙述密度很大，也很雄奇，有些想像力。他把福克纳的小县城搬到了美洲大陆，来了一个象征。这些叙述上的动力来自于他预先设置的马孔多和奥雷连诺家族，因此可以说这是一部象征性的家族史诗小说。很长一段时间他都是我的枕边书。但是现在，我越读越觉得乏味了。我还不大清楚问题出在哪里。<div style="padding-bottom:1em;"></div>我还清楚的记得第一次读到这本书的时间，那是1993年，小学毕业、转升中学，恰逢我小舅师范毕业，在他那我读到《百年孤独》。当时我认为自己并没有过分的分辨能力，很轻易的就被马尔克斯雄奇厚实的叙述吸收掉了，他突然撞进我的视野，震撼着一个少年，尤其对他说自己打小就想写一部像《百年孤独》这样的书那时大约还只有十六岁这一后记中的叙述一直“耿耿于怀”，因为在十四岁这个年头的我读《百年孤独》的时候全然不明白这是怎么一回事。对整个童年在革命文学和传统文学以及连环画语境阅读下成长起来的我－们而言，这部书太神奇了，竟然到第三次才勉强读懂，这和当时阅读《围城》的经历极其相似，也看《西游记》，它很好理解，却不能理解马孔多。这是为何?小时候读的失火，小说中那些名词人物其实是最大的障碍。现在大了读出的乏味又来自哪里？<div style="padding-bottom:1em;"></div>我对《百年孤独》的反省是近来的事情，我以为阅读上的分辨力来自比较，没有一个理论家能给人比比较阅读更容易对一部作品产生“理念”了，这是一个阅读累积过程，也就是对福克纳、马尔克斯、大江健三郎等人的地域性写作全面阅读之后的事情。这种比较阅读让人更加清醒的觉察到这一写作方式在全世界范围内的衰落与终结，包括利用这一方式写作的中国本土作家。<div style="padding-bottom:1em;"></div>马尔克斯悖论是我心理上的一个结，我想，每个人都会有自己的结，所面对的只是归顺还是清算的问题，我更愿意选择后者。目前，我相信，对于“我”的理解是我面对的最大问题。到今天，我不再幼稚的相信只有一个“我”，而是任何时候的我是“群我”的存在，也就是说“我－群我&amp;我－我群”这样一个公式可能更逼近写作者更为真实的心境，更为逼近叙述的在场性，一切的都是关于“我－群我&amp;我－我群”的事，无有其他。但是哪一天我重新面对《百年孤独》时，可能又有会全新的看法，这也说不准。因为在反复阅读中，很多所谓的经典一时被清算掉了，又在另外的时间维度上悄悄回到了自己阁下，我一直这样摇摆和反复着。<div style="padding-bottom:1em;"></div>但是最终还是自我断定，这部小说并不涉及深刻的精神分析。所以才觉出乏味。他仍然是一种较古典的作小说的手法。读《喧哗与骚动》的时候，我感觉更贴近自己的心灵。这是很不同的阅读感受。小说要去反映一个东西的时候比如说现实，那就是被动的。是心灵的残渣。那么，为什么不直截介入心灵呢？ 原本觉得雄奇的马尔克斯式的句式现在我觉得十分臃肿，笨拙不堪。<div style="padding-bottom:1em;"></div>2005年12月1日初稿 宋庄<div style="padding-bottom:1em;"></div>2006年3月3日修改 小汤山<div style="padding-bottom:1em;"></div>
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/13179092/#comments" class="">11回应</a>&nbsp;&nbsp;
                  2011-06-04 13:59
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
  </ul>
  

      
  <ul class="comments by_time"  style="display: none">
      
      <li class="ctsh clearfix" data-cid="79039998">
        <div class="ilst">
          <a href="https://www.douban.com/people/194349387/"><img src="https://img3.doubanio.com/icon/u194349387-1.jpg" alt="林川灏尔" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/79039998/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/79039998/" class="">第121页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/194349387/" class=" " title="林川灏尔">林川灏尔</a>
              
            </p>
            <div class="reading-note" data-cid="79039998">
              <div class="short">
                
                  <span class="">要不了多久，人们不用离开家门，就能看到世界上任何地方发生的事情。 每一个人都是预言家，他们在对未来做着憧憬，而这些幻想有的会成为现实，有的会暂时还是梦想，然后在更远一点的时间，成为现实。</span>
                <p class="pl">
                  <span class="">2019-05-29 12:06</span>
                  
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                <p>要不了多久，人们不用离开家门，就能看到世界上任何地方发生的事情。</p><p>每一个人都是预言家，他们在对未来做着憧憬，而这些幻想有的会成为现实，有的会暂时还是梦想，然后在更远一点的时间，成为现实。</p>
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/79039998/#comments" class="">回应</a>&nbsp;&nbsp;
                  2019-05-29 12:06
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="79028595">
        <div class="ilst">
          <a href="https://www.douban.com/people/186337910/"><img src="https://img3.doubanio.com/icon/u186337910-2.jpg" alt="还没学会" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/79028595/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/79028595/" class="">第243页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/186337910/" class=" " title="还没学会">还没学会</a>
              
            </p>
            <div class="reading-note" data-cid="79028595">
              <div class="short">
                
                  <span class="">世界不过是身外之物。 显而易见又振聋发聩。</span>
                <p class="pl">
                  <span class="">2019-05-28 22:43</span>
                  
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                <p>世界不过是身外之物。</p><p>显而易见又振聋发聩。</p>
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/79028595/#comments" class="">回应</a>&nbsp;&nbsp;
                  2019-05-28 22:43
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="78992764">
        <div class="ilst">
          <a href="https://www.douban.com/people/53284030/"><img src="https://img3.doubanio.com/icon/u53284030-11.jpg" alt="Peggy Sue" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/78992764/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/78992764/" class="">第1页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/53284030/" class=" " title="Peggy Sue">Peggy Sue</a>
              
                <span class="allstar50" title="力荐"></span>
            </p>
            <div class="reading-note" data-cid="78992764">
              <div class="short">
                
                  <span class="">世界新生伊始，许多事物还没有名字，提到的时候尚需用手指指点点。 无论走到哪里，都应该记住，过去都是假的，回忆是一条没有尽头的路，一切以往的春天都不复存在，就连那最坚韧而又狂乱的爱情归根结底也不过是一种转瞬即逝的现实。 人们一派懈怠，而遗忘却日渐贪婪，无情地吞噬一点一滴的记忆。 往日的推心置腹已经一去不复返，同谋和交流变成敌意与缄默。他渴望孤独，对整个世界的怨恨咬噬着他的心。 没有实力支撑的高姿态是...</span>
                <p class="pl">
                  <span class="">2019-05-28 07:51</span>
                  
                    &nbsp;&nbsp;<span class="">1人喜欢</span>
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                <p>世界新生伊始，许多事物还没有名字，提到的时候尚需用手指指点点。</p><p>无论走到哪里，都应该记住，过去都是假的，回忆是一条没有尽头的路，一切以往的春天都不复存在，就连那最坚韧而又狂乱的爱情归根结底也不过是一种转瞬即逝的现实。</p><p>人们一派懈怠，而遗忘却日渐贪婪，无情地吞噬一点一滴的记忆。</p><p>往日的推心置腹已经一去不复返，同谋和交流变成敌意与缄默。他渴望孤独，对整个世界的怨恨咬噬着他的心。</p><p>没有实力支撑的高姿态是在给自己上枷锁。不如华丽的低调。</p><p>世界不过是身外之物，她的内心不再为任何痛苦而波动。她深深遗憾没能在多年前获得这样的领悟，那时还还来得及净化记忆，在崭新的光芒下重建世界，平静地唤回傍晚时皮埃特罗.克雷斯皮身上的薰衣草味道，并且将丽贝卡救出悲惨的境地，而这不是出于爱也不是出于恨，而是出于对孤独的深刻理解。</p><p>他带着这个谜团，深入她的心灵反复探究，想要找寻利益却找到了爱情，他本想让她爱自己结果自己却爱上了她。</p><p>面对着面，彼此凝视，在静谧中相爱，并不比当初在癫狂中相爱减色。</p><p>岁月的航船正在绕过盛年的最后一个岬角。她的微笑带上风琴那般的低音，她的乳房经过无数爱抚耸垂下来，她的小腹和大腿成为无可挽回的尤物生涯的牺牲品，但她的心在衰老中不觉苦涩。她肥胖，饶舌，散发出落难主妇的傲气，摈弃纸牌营造的乏味幻梦，却在旁人的爱情中找到慰籍。</p><p>你那么憎恨军人，跟他们斗了那么久，琢磨了他们那么久，最终却变得和他们一样。人世间没有任何理想值得以这样的沉沦作为代价。</p><p>实际上他成功和失败都因为同一原因，即纯粹、罪恶的自大。她最终得结论，自己不惜为他付出生命的这个儿子，不过是个无力去爱的人。</p><p>既然除了看雨再无事可做，那么将时光分为年月，将日子分为钟点都终归是徒劳。</p><p>蕾梅黛丝在下午两点令人昏昏欲睡的空气中，蕾梅黛丝在玫瑰无声的呼吸中，蕾梅黛丝在蠹虫如沙漏般的暗地蛀蚀中，蕾梅黛丝在清晨面包的热气中，蕾梅黛丝无所不在，蕾梅黛丝无时或缺。</p>
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/78992764/#comments" class="">回应</a>&nbsp;&nbsp;
                  2019-05-28 07:51
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
      
      <li class="ctsh clearfix" data-cid="78977389">
        <div class="ilst">
          <a href="https://www.douban.com/people/164568645/"><img src="https://img3.doubanio.com/icon/u164568645-1.jpg" alt="紫菜小姐🍉" class="" /></a>
        </div>
        <div class="con">
          <div class="nlst">
            <h3>
              <div class="note-toggle rr">
                <a href="https://book.douban.com/annotation/78977389/" class="note-unfolder">展开</a>
                <a href="javascript:void(0);" class="note-folder">收起</a>
              </div>
              <a href="https://book.douban.com/annotation/78977389/" class="">第78页</a></h3>
          </div>
          <div class="clst">
            <p class="user"><a href="https://www.douban.com/people/164568645/" class=" " title="紫菜小姐🍉">紫菜小姐🍉</a>
              
            </p>
            <div class="reading-note" data-cid="78977389">
              <div class="short">
                
                  <span class="">蕾梅黛丝死了。被阿玛兰旦下毒。</span>
                <p class="pl">
                  <span class="">2019-05-27 16:46</span>
                  
                </p>
              </div>
              <div class="all hidden" style="display:none" >
                蕾梅黛丝死了。被阿玛兰旦下毒。
                  <div class="col-rec-con clearfix">
                    







<div class="rec-sec">

    <span class="rec">

<a href="https://www.douban.com/accounts/register?reason=collect" class="j a_show_login lnk-sharing lnk-douban-sharing">推荐</a>
</span>
</div>

                  </div>
                <div class="pl col-time">
                  <a href="https://book.douban.com/annotation/78977389/#comments" class="">回应</a>&nbsp;&nbsp;
                  2019-05-27 16:46
                </div>
              </div>
            </div>
          </div>
        </div>
      </li>
  </ul>
  

    </div>
      <div class="ft">
        <p class="trr">&gt; <a href="https://book.douban.com/subject/6082808/annotation">更多读书笔记（共4650篇）</a></p>
      </div>

</div>



<script type="text/javascript">
  $(document).ready(function(){
    var TEMPL_ADD_COL = '<a href="" id="n-{NOTE_ID}" class="colbutt ll add-col"><span>收藏</span></a>',
      TEMPL_DEL_COL = '<span class="pl">已收藏 &gt;<a href="" id="n-{NOTE_ID}" class="del-col">取消收藏</a></span>';

    $('body').delegate('.add-col', 'click', function(e){
      e.preventDefault();
      var nnid = $(this).attr('id').split('-')[1],
        bn_add = $(this);
      $.post_withck("/j/book/annotation_collect",{nid:nnid},function(){
        var a = $(TEMPL_DEL_COL.replace('{NOTE_ID}', nnid));
        bn_add.before(a);
        bn_add.remove();
      })
    });

    $('body').delegate('.del-col', 'click', function(e){
      e.preventDefault();
      var nnid = $(this).attr('id').split('-')[1],
        bn_del = $(this).parent();
      $.post_withck("/j/book/annotation_uncollect", {nid: nnid}, function() {
        var a = $(TEMPL_ADD_COL.replace('{NOTE_ID}', nnid));
        bn_del.before(a);
        bn_del.remove();
      })
    });

    $("pre.source").each(function(){
      var cn = $(this).attr('class').split(' ');
      l = cn[1];
      s = 'rand01';
      n = cn[2];
      $(this).snippet(n,{style: s, showNum: l});
    });

    var annotationMod = $('.reading-notes .bd')
      , annotationTabs = annotationMod.find('.inline-tabs li')
      , annotationTabLinks = annotationTabs.find('a')
      , annotationTabContents = annotationMod.find('ul.comments');

    annotationTabLinks.click(function(e){
      e.preventDefault();
      var el = $(this)
        , kind = el.attr('id');

      annotationTabs.removeClass('on');
      el.parent().addClass('on');
      annotationTabContents.hide();
      annotationTabContents.filter('.' + kind).show();
    });
  });
</script>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
	jax: ["input/TeX", "output/HTML-CSS"],
    extensions: ["tex2jax.js","TeX/AMSmath.js","TeX/AMSsymbols.js","TeX/noUndefined.js"],
    tex2jax: {
		inlineMath: [ ["($", "$)"], ['\\(','\\)'] ],
		displayMath: [ ["($$","$$)"], ['\\[','\\]']],
		skipTags: ["script","noscript","style","textarea"],
		processEscapes: true,
		processEnvironments: true,
		preview: "TeX"
	},
	showProcessingMessages: false
  });
</script>


  






<div id="db-discussion-section" class="indent ugc-mod">




        
  

  <h2>
    <span class="">论坛</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>



        
<table class="olt"><tr><td><td><td><td></tr>
        
        <tr class="">
            <td class="pl"><a href="https://book.douban.com/subject/6082808/discussion/616016434/" title="看了三分之一，真心不觉得名字有传说中的那么难记" class="">看了三分之一，真心不觉得名字有传说中的那么难记</a></td>
            <td class="pl"><span class="">来自</span><a class="" href="https://www.douban.com/people/43553445/">Au童子</a></td>
            <td class="pl"><span class="">3 回应</span></td>
            <td class="pl"><span class="">2019-05-30</span></td>
        </tr>
        
        <tr class="">
            <td class="pl"><a href="https://book.douban.com/subject/6082808/discussion/615900085/" title="看了一圈发现很多人都被书中人物祖传的名字给敲昏了" class="">看了一圈发现很多人都被书中人物祖传的名字给敲昏了</a></td>
            <td class="pl"><span class="">来自</span><a class="" href="https://www.douban.com/people/187465039/">月下逢</a></td>
            <td class="pl"><span class="">10 回应</span></td>
            <td class="pl"><span class="">2019-05-30</span></td>
        </tr>
        
        <tr class="">
            <td class="pl"><a href="https://book.douban.com/subject/6082808/discussion/615072314/" title="想问下上校唯一的儿子的结局" class="">想问下上校唯一的儿子的结局</a></td>
            <td class="pl"><span class="">来自</span><a class="" href="https://www.douban.com/people/147705963/">07刘夏莱</a></td>
            <td class="pl"><span class="">12 回应</span></td>
            <td class="pl"><span class="">2019-05-29</span></td>
        </tr>
        
        <tr class="">
            <td class="pl"><a href="https://book.douban.com/subject/6082808/discussion/616322267/" title="当众孤独" class="">当众孤独</a></td>
            <td class="pl"><span class="">来自</span><a class="" href="https://www.douban.com/people/197291020/">于鱼</a></td>
            <td class="pl"><span class=""></span></td>
            <td class="pl"><span class="">2019-05-29</span></td>
        </tr>
        
        <tr class="">
            <td class="pl"><a href="https://book.douban.com/subject/6082808/discussion/616321117/" title="书评" class="">书评</a></td>
            <td class="pl"><span class="">来自</span><a class="" href="https://www.douban.com/people/197226352/">大大泡泡糖</a></td>
            <td class="pl"><span class=""></span></td>
            <td class="pl"><span class="">2019-05-28</span></td>
        </tr>
</table>


            <p class="pl" align="right">&gt;
                <a href="https://book.douban.com/subject/6082808/discussion/">浏览更多话题</a>
            </p>


</div>




</div>
<script type="text/javascript">
$(function(){if($.browser.msie && $.browser.version == 6.0){
    var maxWidth = parseInt($('#info').css('max-width'));
    if($('#info').width() > maxWidth)
        $('#info').width(maxWidth)
}});
</script>
</div>
      <div class="aside">
        
  
  






  <div id="dale_book_subject_top_right"></div>
    
  
  
  <div class="gray_ad">
    
  

  <h2>
    <span class="">其他版本在豆瓣书店有售</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>


    <div class="market-banner">
        <a class="publish" href="https://book.douban.com/subject/27107109/" target="_blank">
          南海出版公司版
        </a><br/>
      <span class="title">
        纸质版&nbsp;
      </span>
      <span class="price"> 44.00元</span>
        <span class="price"> <del>55.00元</del></span>
      <span class="promotion-info">满48元包邮</span>
      <span class="actions">
        <a class="buy-btn buy" target="_blank" href="https://market.douban.com/cart/checkout/?sku_id=235355&utm_campaign=douban_book_subject_buy_btn&utm_source=douban&utm_medium=pc_web">
          去购买
        </a>
          <a class="j a_show_login buy-btn cart" href="javascript:;">加入购物车</a>
      </span>
    </div>
  </div>


  






<style type="text/css" media="screen">
  .add2cartContainer{overflow:hidden;vertical-align:bottom;line-height:1}.add2cartContainer .add2cart{margin-right:0;display:inline-block}#buyinfo .bs{margin:0}#buyinfo li{padding:10px 0;position:relative;line-height:1;border-bottom:1px solid #eaeaea}#buyinfo li a:hover{background-image:none !important}#buyinfo li a:hover .buylink-price{background:#37a}#buyinfo li .publish,#buyinfo li .other-activity{margin-top:5px}#buyinfo li .publish a,#buyinfo li .other-activity a{color:#999}#buyinfo li .publish a:hover,#buyinfo li .other-activity a:hover{color:#37a;background:none;opacity:0.5;filter:alpha(opacity=50)}#buyinfo li .buylink-price{position:absolute;right:90px;text-align:right}#buyinfo .more-info{color:#aaa;margin:6px 0 -2px 0}#buyinfo .more-ebooks{padding:10px 0;color:#37a;cursor:pointer}#buyinfo .price-page{border-bottom:0;padding:15px 0 0}#buyinfo .saved-price{display:none;margin-left:5px}#buyinfo .cart-tip{float:right;padding-right:5px}#buyinfo #buyinfo-ebook{margin-bottom:15px}#buyinfo #buyinfo-ebook .buylink-price{display:inline}#buyinfo #buyinfo-ebook li.no-border{border:0}#buyinfo-printed{margin-bottom:15px}#buyinfo-printed.no-border{border-bottom:0}#buyinfo-printed .more-ebooks{line-height:1;padding:10px 0;color:#37a;cursor:pointer;padding:10px 0 0}#buyinfo-report{display:none}#buyinfo-report .lnk-close-report{float:right;margin-top:-30px;line-height:14px}#buyinfo-report .item{margin-bottom:10px}#buyinfo-report .item input{vertical-align:text-bottom;*vertical-align:middle}#buyinfo-report .item label{margin:0 5px 0 2px}#buyinfo-report .item-submit .bn-flat{margin-right:10px}#buyinfo-report .item-price input{width:220px;border:1px solid #ccc;padding:4px}#buyinfo-report form{margin:5px 0 10px}#bi-report-btn{float:right;margin:2px 0;line-height:14px;display:none}.bi-vendor-report{color:#aaa}.bi-vendor-report-form{display:none;color:#111;margin:0 5px;line-height:25px}.gray_ad{padding:30px 20px 25px 20px;background:#f6f6f1}.gray_ad h2{margin-bottom:6px;font-size:15px}.gray_ad .ebook-tag{margin-top:5px;color:#999;font-size:12px}.bs.more-after{margin-bottom:0px}@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi){#buyinfo li a:hover{background-image:url(https://img3.doubanio.com/f/book/fc4ff7f0a3a7f452f06d586540284b9738f2fe87/pics/book/cart/icon-brown@2x.png);background-size:16px 12px}}#intervenor-buyinfo .bs{margin:0}#intervenor-buyinfo li{position:relative;border-bottom:1px solid #eaeaea;padding:10px 0;line-height:1}#intervenor-buyinfo li .basic-info{color:#494949;font-size:14px;line-height:18px}#intervenor-buyinfo li a:hover .comment{color:#f67;opacity:0.75;filter:alpha(opacity=75)}#intervenor-buyinfo li a:hover .buy-btn{background:#fff;border:1px solid #e97e7e;border-radius:2px;color:#e97e7e}#intervenor-buyinfo li a:hover .buylink-price{background:#37a}#intervenor-buyinfo li .buylink-price{position:absolute;right:90px;text-align:right}#intervenor-buyinfo li .publish,#intervenor-buyinfo li .other-activity{margin-top:5px}#intervenor-buyinfo li .publish a,#intervenor-buyinfo li .other-activity a{color:#999}#intervenor-buyinfo li .publish a:hover,#intervenor-buyinfo li .other-activity a:hover{color:#37a;background:none;opacity:0.5;filter:alpha(opacity=50)}#intervenor-buyinfo .jd-buy-icon{float:left;margin-right:3px}#intervenor-buyinfo .buy-btn{float:right;position:absolute;right:10px;bottom:3px;color:#9c9c9c;padding:0 12px;border:1px solid transparent}#intervenor-buyinfo .comment{color:#FF8C9C;margin:6px 0 -2px 0}#intervenor-buyinfo .price-page a{display:inline-block;line-height:16px !important}#intervenor-buyinfo .price-page{border-bottom:0;padding:15px 0 0}#intervenor-buyinfo .saved-price{display:none;margin-left:5px}#intervenor-buyinfo .cart-tip{float:right;padding-right:5px}#intervenor-buyinfo #buyinfo-ebook{margin-bottom:15px}#intervenor-buyinfo #buyinfo-ebook .buylink-price{display:inline}#intervenor-buyinfo #buyinfo-ebook li.no-border{border:0}#buyinfo-printed .presale-indicator{margin:0;width:auto;color:#999;text-indent:0;background:none}#buyinfo-printed .buylink-title{color:#999}#buyinfo-printed .second-hand{display:block;margin-top:30px}

</style>

      <div class="gray_ad" id="buyinfo">
      <div id="buyinfo-printed">
        
  

  <h2>
    <span class="">在哪儿买这本书</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>


        <ul class="bs noline more-after ">
          
              
                <span class="buylink-title">购买全新书</span>
                
                <li class="">
                    <a target="_blank" href="https://book.douban.com/link2/?lowest=1770&amp;pre=0&amp;vendor=jingdong&amp;srcpage=subject&amp;price=3870&amp;pos=1&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEwBRElwQBSJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQMVA1wcXhIdS0IJRmsdUWxZI0EpdGJyBFJ5AHF2VnsLTTlDDh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBpeEgURAVcrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsUBRYOUh5cCltXWwg%253D&amp;cntvendor=2&amp;srcsubj=6082808&amp;type=bkbuy&amp;subject=6082808" class="">
                      <span class="">京东商城</span>
                    </a>
                    <a target="_blank" href="https://book.douban.com/link2/?lowest=1770&amp;pre=0&amp;vendor=jingdong&amp;srcpage=subject&amp;price=3870&amp;pos=1&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEwBRElwQBSJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQMVA1wcXhIdS0IJRmsdUWxZI0EpdGJyBFJ5AHF2VnsLTTlDDh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBpeEgURAVcrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsUBRYOUh5cCltXWwg%253D&amp;cntvendor=2&amp;srcsubj=6082808&amp;type=bkbuy&amp;subject=6082808" class="buylink-price ">
                      <span class="">
                        38.70 元
                      </span>
                    </a>
                      
                </li>
              <!-- duozhuayu --!>
                <span class="buylink-title second-hand">购买二手书</span>
                
                <li class="">
                    <a target="_blank" href="https://book.douban.com/link2/?lowest=1770&amp;pre=0&amp;vendor=duozhuayu&amp;srcpage=subject&amp;price=1770&amp;pos=1&amp;url=https%3A%2F%2Fwww.duozhuayu.com%2Fbooks%2F47009263117142058%3Futm_medium%3Dweb%26utm_source%3Ddouban&amp;cntvendor=2&amp;link2key=0ebf1d773c&amp;srcsubj=6082808&amp;type=bkbuy&amp;subject=6082808" class="">
                      <span class="">多抓鱼</span>
                    </a>
                    <a target="_blank" href="https://book.douban.com/link2/?lowest=1770&amp;pre=0&amp;vendor=duozhuayu&amp;srcpage=subject&amp;price=1770&amp;pos=1&amp;url=https%3A%2F%2Fwww.duozhuayu.com%2Fbooks%2F47009263117142058%3Futm_medium%3Dweb%26utm_source%3Ddouban&amp;cntvendor=2&amp;link2key=0ebf1d773c&amp;srcsubj=6082808&amp;type=bkbuy&amp;subject=6082808" class="buylink-price ">
                      <span class="">
                        17.70 元起
                      </span>
                    </a>
                      
                </li>
          <li class="price-page">
            <a href="https://book.douban.com/subject/6082808/buylinks">
              &gt; 查看2家网店价格
                (17.70 元起)
            </a>
          </li>
        </ul>
      </div>
      
  <div class="add2cartContainer ft no-border">
    
  <span class="add2cartWidget ll">
      <a class="j  add2cart a_show_login" href="https://www.douban.com/accounts/passport/login?reason=addbook2cart" rel="nofollow">
        <span>+ 加入购书单</span></a>
  </span>
  

  </div>

  </div>
  <script type="text/javascript">
  $('.more-ebooks').on('click', function() {
    var $this = $(this),
      $li = $this.siblings('ul').find('li');
    if ($this.hasClass('isShow')) {
      $(this).text('展开更多').removeClass('isShow');
      $li.not(':first').addClass('hide');
    }else{
      $(this).text('收起').addClass('isShow');
      $li.removeClass('hide');
    }
    
  })
  </script>

<style class="text/css">
  .presale-indicator {
  display: inline-block;
  *display: inline;
  *zoom: 1;
  width: 24px;
  height: 15px;
  line-height: 15px;
  background: url(https://img3.doubanio.com/f/book/1679c65572eac1371f9872807199dea6e55a7f06/pics/book/cart/presale_text.gif) no-repeat;
  text-indent: -9999px;
  vertical-align: middle;
  *vertical-align: 0px;
  _vertical-align: 2px;
  margin-left: 0.5em;
}

</style>



  





<div class="gray_ad" id="borrowinfo">
  
  

  <h2>
    <span class="">在哪儿借这本书</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;

  </h2>


  <ul class="bs more-after">
      
      <li style="border: none">
        <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fipac.library.sh.cn%2Fipac20%2Fipac.jsp%3Faspect%3Dbasic_search%26profile%3Dsl%26index%3DISBN%26term%3D9787544253994%26otherloc%3Dtrue&amp;subject=7544253996&amp;type=borrow&amp;library=10011&amp;link2key=0ebf1d773c" target="_blank">上海市中心图书馆(84)</a>
      </li>
      
      <li style="border: none">
        <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fopac.gzlib.gov.cn%2Fopac%2Fsearch%3Frows%3D10%26curlibcode%3DGT%26hasholding%3D1%26searchWay0%3Dmarc%26q0%3D%26logical0%3DAND%26q%3D9787544253994%26searchWay%3Disbn%26scWay%3Ddim%26searchSource%3Dreader&amp;subject=7544253996&amp;type=borrow&amp;library=10023&amp;link2key=0ebf1d773c" target="_blank">广州其他馆藏(2)</a>
      </li>
      
      <li style="border: none">
        <a href="https://www.douban.com/link2/?url=http%3A%2F%2F218.62.1.221%3A8080%2Fopac%2Fopenlink.php%3FstrText%3D978-7-5442-5399-4%26strSearchType%3Disbn&amp;subject=7544253996&amp;type=borrow&amp;library=10002&amp;link2key=0ebf1d773c" target="_blank">吉林省图书馆</a>
      </li>
      
      <li style="border: none">
        <a href="https://www.douban.com/link2/?url=http%3A%2F%2F58.154.49.3%3A8080%2Fopac%2Fopenlink.php%3FhistoryCount%3D1%26strText%3D978-7-5442-5399-4%26doctype%3DALL%26strSearchType%3Disbn%26match_flag%3Dforward%26displaypg%3D20%26sort%3DCATA_DATE%26orderby%3Ddesc%26showmode%3Dlist%26location%3DALL&amp;subject=7544253996&amp;type=borrow&amp;library=10010&amp;link2key=0ebf1d773c" target="_blank">沈阳师范大学图书馆</a>
      </li>
      
      <li style="border: none">
        <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fopac3.wzlib.cn%2Fopac%2Fsearch%3FsearchWay%3Disbn%26q%3D978-7-5442-5399-4%26booktype%3D%26marcformat%3D%26sortWay%3Dscore%26sortOrder%3Ddesc%26startPubdate%3D%26endPubdate%3D%26rows%3D10&amp;subject=7544253996&amp;type=borrow&amp;library=10020&amp;link2key=0ebf1d773c" target="_blank">温州市图书馆</a>
      </li>
      
      <li style="border: none">
        <a href="https://www.douban.com/link2/?url=http%3A%2F%2F222.177.237.197%3A8080%2FInDigLib%2Ffront%2FComplexSearch.action%3FcurrentPage%3D1%26select1%3Disbn%26select2%3D%26select3%3D%26text1%3D978-7-5442-5399-4%26text2%3D%26text3%3D%26pageSize%3D20%26condition%3D%26table%3Di_biblios%26type%3D%26videoType%3Dcomplex&amp;subject=7544253996&amp;type=borrow&amp;library=10021&amp;link2key=0ebf1d773c" target="_blank">重庆图书馆</a>
      </li>
  </ul>
  <div class="clearfix"></div>
  <!--<div class="ft pl">-->
    <!--<a class="rr"  href="https://book.douban.com/library_invitation">&gt; 图书馆合作</a>-->
    <!--找不到你需要的图书馆？-->
  <!--</div>-->
</div>

  <div id="dale_book_subject_top_middle"></div>
  





  

  
  

  <h2>
    <span class="">这本书的其他版本 </span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
      <span class="pl">&nbsp;(
          <a href="https://book.douban.com/works/1007890">全部47</a>
        ) </span>

  </h2>


  <div class="indent">
    <ul>
        <li class="mb8 pl">
          <a href="https://book.douban.com/subject/1424568/">Everyman&#39;s Library版</a>
          1995-10-17 / 298人读过
        </li>
        <li class="mb8 pl">
          <a href="https://book.douban.com/subject/1786670/">上海译文出版社版</a>
          1989-10 / 72845人读过
        </li>
        <li class="mb8 pl">
          <a href="https://book.douban.com/subject/1059112/">浙江文艺出版社版</a>
          1991-12 / 9941人读过
        </li>
        <li class="mb8 pl">
          <a href="https://book.douban.com/subject/2008724/">南海出版社版</a>
          2007 / 3804人读过 / 有售
        </li>
    </ul>
  </div>


  



      
  

  <h2>
    <span class="">以下豆列推荐</span>
      &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
      <span class="pl">&nbsp;(
          <a href="https://book.douban.com/subject/6082808/doulists">全部</a>
        ) </span>

  </h2>


    <div id="db-doulist-section" class="indent">
      <ul class="bs">
          <li class=""><a class="" href="https://www.douban.com/doulist/1294399/" target="_blank">世界100位文学大师排行榜及代表作最佳中文版本</a>
                <span class="pl">(子萌先生)</span>
            </li>
          <li class=""><a class="" href="https://www.douban.com/doulist/226728/" target="_blank">一湄私人书橱</a>
                <span class="pl">(一湄)</span>
            </li>
          <li class=""><a class="" href="https://www.douban.com/doulist/436036/" target="_blank">你好好睡，我好好读书。等你醒了我们聊柏拉图。</a>
                <span class="pl">(琼斯黄)</span>
            </li>
          <li class=""><a class="" href="https://www.douban.com/doulist/1757387/" target="_blank">评分9.0~9.7(1000+人参与评价)</a>
                <span class="pl">(第五顾尘ᕦ)</span>
            </li>
          <li class=""><a class="" href="https://www.douban.com/doulist/15494/" target="_blank">值得看看的一些文史哲闲书</a>
                <span class="pl">(froggy)</span>
            </li>
      </ul>
    </div>

  <div id="dale_book_subject_middle_mini"></div>
  






  <h2>谁读这本书?</h2>
  <div class="indent" id="collector">

    

<div class="">
    
    <div class="ll"><a href="https://www.douban.com/people/193706924/"><img src="https://img3.doubanio.com/icon/u193706924-3.jpg" class="pil" alt="仰望随想" /></a></div>
    <div style="padding-left:60px"><a class="" href="https://www.douban.com/people/193706924/">仰望随想</a><br/>
      <div class="pl ll">          26分钟前          读过      </div>

        <span class="allstar50" title="力荐"></span>
      <br/>

    </div>
    <div class="clear"></div><br/>
    <div class="ul" style="margin-bottom:12px;"></div>
</div>
<div class="">
    
    <div class="ll"><a href="https://www.douban.com/people/197357095/"><img src="https://img3.doubanio.com/icon/u197357095-4.jpg" class="pil" alt="庄雯-ZhangWen" /></a></div>
    <div style="padding-left:60px"><a class="" href="https://www.douban.com/people/197357095/">庄雯-ZhangWen</a><br/>
      <div class="pl ll">          28分钟前          读过      </div>

        <span class="allstar50" title="力荐"></span>
      <br/>

    </div>
    <div class="clear"></div><br/>
    <div class="ul" style="margin-bottom:12px;"></div>
</div>
<div class="">
    
    <div class="ll"><a href="https://www.douban.com/people/withtea/"><img src="https://img3.doubanio.com/icon/u1941805-14.jpg" class="pil" alt="singsingsong" /></a></div>
    <div style="padding-left:60px"><a class="" href="https://www.douban.com/people/withtea/">singsingsong</a><br/>
      <div class="pl ll">          29分钟前          读过      </div>

      <br/>

    </div>
    <div class="clear"></div><br/>
    <div class="ul" style="margin-bottom:12px;"></div>
</div>


        <p class="pl">&gt; <a href="https://book.douban.com/subject/6082808/doings">41220人在读</a></p>
        <p class="pl">&gt; <a href="https://book.douban.com/subject/6082808/collections">216516人读过</a></p>
        <p class="pl">&gt; <a href="https://book.douban.com/subject/6082808/wishes">194407人想读</a></p>

  </div>





  
<!-- douban ad begin -->
<div id="dale_book_subject_middle_right"></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_book_subject_middle_right');
        }
    })(this);
</script>
<!-- douban ad end -->

  





  

  <h2>二手市场</h2>
  <div class="indent">
    <ul class="bs">
    <li class="">
        <a class=" " href="https://book.douban.com/subject/6082808/offers">35本二手书欲转让</a>
          <span class="">
            (0.01
                至 500元以上)
          </span>
      </li>
      <li>
          <a class="rr j a_show_login" href="https://www.douban.com/register?reason=secondhand-offer&amp;cat=book"><span>&gt; 在豆瓣转让</span></a>

        有194407人想读,手里有一本闲着?
      </li>
      <li>
          <a href='https://www.duozhuayu.com/sell?utm_source=douban&utm_medium=new_offer' class="rr">&gt; 多抓鱼</a>
          转让给其他二手平台？
      </li>
    </ul>
  </div>

  
<p class="pl">订阅关于百年孤独的评论: <br/><span class="feed">
    <a href="https://book.douban.com/feed/subject/6082808/reviews"> feed: rss 2.0</a></span></p>


      </div>
      <div class="extra">
        
  
<!-- douban ad begin -->
<div id="dale_book_subject_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_book_subject_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->


      </div>
    </div>
  </div>

        
<div id="footer">

<span id="icp" class="fleft gray-link">
    &copy; 2005－2019 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/?app=book" target="_blank">帮助中心</a>
    · <a href="https://book.douban.com/library_invitation">图书馆合作</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

</div>

    </div>
      
  

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/7dccdcfb50652052.js"></script>
    <!-- mako -->
    
  








    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = 'MnaANSL_x8I',
            criteria = '7:百年孤独|7:加西亚·马尔克斯|7:经典|7:拉美文学|7:魔幻现实主义|7:外国文学|7:小说|7:文学|7:孤独|7:名著|3:/subject/6082808/',
            preview = '',
            debug = false,
            adSlots = ['dale_book_subject_top_icon', 'dale_book_subject_top_right', 'dale_book_subject_top_middle', 'dale_book_subject_middle_mini'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/b2a623018cd76036bb32ad74c28ea231fb2aa462/ad.release.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>












    
  

<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; 
    g.type='text/javascript';
    g.defer=true; 
    g.async=true; 
    g.src=p+'://s.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
  })();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-16', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id])

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>








    <!-- anson60-docker-->

</body>
</html>






































'''
selector=etree.fromstring(html)

#contents=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]')

# simple1=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/span[1]/a')
# print simple1
# print simple1

simple2=selector.xpath('//*[@id="link-report"]/div[1]/div')
print simple2
print simple2