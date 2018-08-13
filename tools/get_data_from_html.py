from bs4 import BeautifulSoup
import os
import urllib
import requests

# 解析html，获取验证码的图片链接
def get_img_src_from_html(html):
    print(html)
    soup = BeautifulSoup(html)
    src = ""
    link = soup.find_all('img', attrs={'id': 'captcha_image'})  # 获取步骤-预期
    for step in link:
        item = step.get('src')
        if item:
            src=item.replace('','')
    return src


def save_img(img_url,file_name, file_path):
    # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print("File path isn't exist,build one!")
            # os.mkdir(file_path)
            os.makedirs(file_path)
        # 获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        # 下载图片，并保存到文件夹中
        # urllib.urlretrieve(img_url, filename=filename)
        r = requests.get(img_url)
        r.raise_for_status()
        with open(file_path,"wb") as f:
            f.write(r.content)
    except IOError as e:
        print('Operation failed ',e)
    except Exception as e:
        print('Error ：', e)


html1 = """
<!DOCTYPE HTML>
<html lang="zh-cmn-Hans" class="ua-windows ua-webkit">
<head>
<meta charset="UTF-8">
<meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
<meta name="description" content="提供图书、电影、音乐唱片的推荐、评论和价格比较，以及城市独特的文化生活。">
<meta name="keywords" content="豆瓣,广播,登陆豆瓣">
<meta property="qc:admins" content="2554215131764752166375" />
<meta property="wb:webmaster" content="375d4a17a4fa24c2" />
<meta name="mobile-agent" content="format=html5; url=https://m.douban.com">
<title>豆瓣</title>
<script>
function set_cookie(t,e,o,n){var i,a,r=new Date;r.setTime(r.getTime()+24*(e||30)*60*60*1e3),i="; expires="+r.toGMTString();for(a in t)document.cookie=a+"="+t[a]+i+"; domain="+(o||"douban.com")+"; path="+(n||"/")}function get_cookie(t){var e,o,n=t+"=",i=document.cookie.split(";");for(e=0;e<i.length;e++){for(o=i[e];" "==o.charAt(0);)o=o.substring(1,o.length);if(0===o.indexOf(n))return o.substring(n.length,o.length).replace(/\"/g,"")}return null}window.Douban=window.Douban||{};var Do=function(){Do.actions.push([].slice.call(arguments))};Do.ready=function(){Do.actions.push([].slice.call(arguments))},Do.add=Do.define=function(t,e){Do.mods[t]=e},Do.global=function(){Do.global.mods=Array.prototype.concat(Do.global.mods,[].slice.call(arguments))},Do.global.mods=[],Do.mods={},Do.actions=[],Douban.init_show_login=function(t){Do("dialog",function(){var t="/j/misc/login_form";dui.Dialog({title:"登录",url:t,width:/device-mobile/i.test(document.documentElement.className)?.9*document.documentElement.offsetWidth:350,cache:!0,callback:function(t,e){e.node.addClass("dialog-login"),e.node.find("h2").css("display","none"),e.node.find(".hd h3").replaceWith(e.node.find(".bd h3")),e.node.find("form").css({border:"none",width:"auto",padding:"0"}),e.update()}}).open()})},Do(function(){function t(t,e){var o=["ref="+encodeURIComponent(location.pathname)];for(var n in e)e.hasOwnProperty(n)&&o.push(n+"="+e[n]);window._SPLITTEST&&o.push("splittest="+window._SPLITTEST),localStorage.setItem("report",(localStorage.getItem("report")||"")+"_moreurl_separator_"+o.join("&"))}!function(){"localStorage"in window||(window.localStorage=function(){var t=document;if(!t.documentElement.addBehavior)throw"don't support localstorage or userdata.";var e="_localstorage_ie",o=t.createElement("input");o.type="hidden";var n=function(n){return function(){t.body.appendChild(o),o.addBehavior("#default#userData");var i=new Date;i.setDate(i.getDate()+365),o.expires=i.toUTCString(),o.load(e);var a=n.apply(o,arguments);return t.body.removeChild(o),a}};return{getItem:n(function(t){return this.getAttribute(t)}),setItem:n(function(t,o){this.setAttribute(t,o),this.save(e)}),removeItem:n(function(t){this.removeAttribute(t),this.save(e)}),clear:n(function(){for(var t,o=this.XMLDocument.documentElement.attributes,n=0;t=o[n];n++)this.removeAttribute(t.name);this.save(e)})}}())}(),$(window).one("load",function(){var t=localStorage.getItem("report");if(t){t=t.split("_moreurl_separator_");var e=function(o){return""==o?void e(t.shift()):void $.get("undefined"==typeof _MOREURL_REQ?"/stat.html?"+o:_MOREURL_REQ+"?"+o,function(){return t.length?(e(t.shift()),void localStorage.setItem("report",t.join("_moreurl_separator_"))):void localStorage.removeItem("report")})};e(t.shift())}}),window.moreurl=t,$(document).click(function(e){var o=e.target,n=$(o).data("moreurl-dict");n&&t(o,n)}),$.ajax_withck=function(t){return"POST"==t.type&&(t.data=$.extend(t.data||{},{ck:get_cookie("ck")})),$.ajax(t)},$.postJSON_withck=function(t,e,o){return $.post_withck(t,e,o,"json")},$.post_withck=function(t,e,o,n){return $.isFunction(e)&&(n=o,o=e,e={}),$.ajax({type:"POST",url:t,data:$.extend(e,{ck:get_cookie("ck")}),success:o,dataType:n||"text"})},$("html").click(function(t){var e=$(t.target),o=e.attr("class");o&&$(o.match(/a_(\w+)/gi)).each($.proxy(function(e,o){var n=Douban[o.replace(/^a_/,"init_")];"function"==typeof n&&(t.preventDefault(),n.call(this,t))},e[0]))})});

Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/4ea3216519a6183c7bcd4f7d1a6d4fd57ce1a244/js/ui/dialog.js', type: 'js', requires: ['https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css']});
Do.global('https://img3.doubanio.com/f/sns/b5793c2d7c298173d57ecf7d96708b5615336def/js/sns/fp/base.js', 'dialog');
</script>
<link rel="stylesheet" href="https://img3.doubanio.com/f/shire/8b9fa55c839b74f72d2279a4f6839a2c8a1a9553/css/core/_init_.css">
<link rel="stylesheet" href="https://img3.doubanio.com/f/sns/8b0746b6f033deded1cb9786440a0d621242c6ba/css/sns/anonymous_home.css">
<style type="text/css">
.rec_topics_name{
    display: inline-block;
    margin-bottom: 6px;
    font-size: 14px;
    line-height: 1.3;
    color: #3377aa;
}
.rec_topics_subtitle{
    display: block;
    margin-bottom: 15px;
    font-size: 13px;
    line-height: 1;
    color: #aaaaaa;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.rec_topics_label{
    transform: translateY(-0.5px);
    display: inline-block;
    font-size: 13px;
    margin-left: 2px;
}
.rec_topics{
    line-height: 1;
    margin-bottom: 15px;
}
.rec_topics:last-child{
    margin-bottom: 0;
}
.rec_topics_label_ad{
    color: #c9c9c9;
    -moz-transform: scale(0.91);
    -webkit-transform: scale(0.91);
    transform: scale(0.91);
}

html[class*=ua-ff] .rec_topics_subtitle{
    line-height: 14px;
}

</style>
</head>

<body>


  <div id="anony-nav">
    <div class="anony-nav-links">
    <ul>
    <li> <a target="_blank" class="lnk-book" href="https://book.douban.com">豆瓣读书</a></li>
    <li> <a target="_blank" class="lnk-movie" href="https://movie.douban.com">豆瓣电影</a></li>
    <li> <a target="_blank" class="lnk-music" href="https://music.douban.com">豆瓣音乐</a></li>
    <li> <a target="_blank" class="lnk-group" href="https://www.douban.com/group/">豆瓣小组</a></li>
    <li> <a target="_blank" class="lnk-events" href="https://www.douban.com/location/">豆瓣同城</a></li>
    <li> <a target="_blank" class="lnk-fm" href="https://douban.fm">豆瓣FM</a></li>
    <li> <a target="_blank" class="lnk-shijian" href="https://time.douban.com/?dt_time_source=douban-web_anonymous_index_top_nav">豆瓣时间</a></li>
    <li> <a target="_blank" class="lnk-market" href="https://market.douban.com?utm_campaign=anonymous_top_nav&utm_source=douban&utm_medium=pc_web">豆瓣豆品</a></li>
    </ul>
    </div>

    <h1><a href="https://www.douban.com">豆瓣</a></h1>

    <div class="anony-srh">
    <form action="https://www.douban.com/search" method="get">
      <span class="inp"><input type="text" maxlength="60" size="12" placeholder="书籍、电影、音乐、小组、小站、成员" name="q" autocomplete="off"></span>
    <span class="bn"><input type="submit" value="搜索"></span>
    </form>
    </div>
  </div>



<div id="anony-reg-new">
  <div class="wrapper">
    
<div class="login">
    <form id="lzform" name="lzform" method="post" action="https://www.douban.com/accounts/login">
        <fieldset>
            <legend>登录</legend>
            <input type="hidden" value="index_nav" name="source">
            <div class="item item-account">
                <input type="text" name="form_email" id="form_email" value="fannyco@163.com" class="inp" placeholder="邮箱 / 手机号" tabIndex="1">
            </div>
            <div class="item item-passwd">
                <input name="form_password" placeholder="密码" id="form_password" class="inp" type="password" tabIndex="2">
                <div class="opt">
                    <a href="https://www.douban.com/accounts/resetpassword">帮助</a>
                </div>
            </div>
              <div class="item item-captcha">
                  


<div class="captcha_block">
    <input type="text" autocomplete="off" class="inp" id="captcha_field" name="captcha-solution" tabindex="3" placeholder="验证码"/>
    <input type="hidden" name="captcha-id" value="tu37QFVEkwbiCi29OJp6UyEW:en"/>
</div>
<img id="captcha_image" src="https://www.douban.com/misc/captcha?id=tu37QFVEkwbiCi29OJp6UyEW:en&amp;size=s" alt="captcha" class="captcha_image" title="看不清楚?点图片可以换一个"/>



              </div>
            <div class="item item-submit">
                <input value="登录豆瓣" type="submit" class="bn-submit" tabIndex="4">
                <a href="/accounts/register" class="lnk-reg">注册帐号</a>
            </div>
            <div class="item-action">
                <label for="form_remember">
                    <input name="remember" type="checkbox" id="form_remember" tabIndex="4">记住我
                </label>
                <ul class="item-action-third">
                    <li><a class="wechat" href="https://www.douban.com/accounts/connect/wechat/?from=douban-web-anony-home" target="_blank" title="微信登录">微信登录</a></li>
                    <li><a class="weibo" href="https://www.douban.com/accounts/connect/sina_weibo/?from=douban-web-anony-home" target="_blank" title="微博登录">微博登录</a></li>
                </ul>
            </div>
        </fieldset>
    </form>
    <div style="display:none;">
        <img src="https://www.douban.com/pics/blank.gif" onload="(function(url){document.getElementById('lzform').action=url;})('https://www.douban.com/accounts/login')"/>
    </div>
</div>

    <div class="app">
      <p class="app-title">豆瓣<span>5.0</span></p>
      <p class="app-slogan"></p>
      <a href="https://www.douban.com/doubanapp/app?channel=nimingye" class="lnk-app">下载豆瓣 App</a>
      <div class="app-qr">
        <a href="javascript: void 0;" class="lnk-qr" id="expand-qr"><img src="https://img3.doubanio.com/f/sns/0c708de69ce692883c1310053c5748c538938cb0/pics/sns/anony_home/icon_qrcode_green.png" width="28" height="28" /></a>
        <div class="app-qr-expand">
          <img src="https://img3.doubanio.com/f/sns/1cad523e614ec4ecb6bf91b054436bb79098a958/pics/sns/anony_home/doubanapp_qrcode.png" width="160" height="160" />
          <p>iOS / Android 扫码直接下载</p>
        </div>
      </div>
    </div>
  </div>
  <script>
  Do(function() {
    var app_qr = $('.app-qr');
    app_qr.hover(function() {
      app_qr.addClass('open');
    }, function() {
      app_qr.removeClass('open');
    });
  });
  </script>
</div>







      
<div id="anony-sns" class="section">
  <div class="wrapper">
  
<!-- douban ad begin -->
<div id="dale_anonymous_homepage_top_for_crazy_ad"></div>
<!-- douban ad end -->

  
  <div class="side">
  <div style="margin:10px 0px;">
    <div id="dale_anonymous_homepage_right_top"></div>
  </div>
  <div class="online">
    <ul>
      






<div class="mod">
    
    <h2>
        热门话题
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="/gallery/" target="_self">去话题广场</a>
                ) </span>
    </h2>


    <ul>
        
            <li class="rec_topics">
                    <a href="https://www.douban.com/gallery/topic/17041/?from=hot_topic_anony_sns" class="rec_topics_name">纪念奈保尔</a>
                    
                    <span class="rec_topics_subtitle">4641人浏览</span>
            </li>
            <li class="rec_topics">
                    <a href="https://www.douban.com/gallery/topic/16774/?from=hot_topic_anony_sns" class="rec_topics_name">你的哲学阅读脉络</a>
                    
                    <span class="rec_topics_subtitle">新话题</span>
            </li>
            <li class="rec_topics">
                    <a href="https://www.douban.com/gallery/topic/14673/?from=hot_topic_anony_sns" class="rec_topics_name">你买了之后却一直没看完的书</a>
                    
                    <span class="rec_topics_subtitle">5784人浏览</span>
            </li>
            <li class="rec_topics">
                    <a href="https://www.douban.com/gallery/topic/15172/?from=hot_topic_anony_sns" class="rec_topics_name">你心中最好的日本动漫电影</a>
                    
                    <span class="rec_topics_subtitle">1117人浏览</span>
            </li>
            <li class="rec_topics">
                    <a href="https://www.douban.com/gallery/topic/15368/?from=hot_topic_anony_sns" class="rec_topics_name">晒出你家猫主子小时候的照片</a>
                    
                    <span class="rec_topics_subtitle">40581人浏览</span>
            </li>
            <li class="rec_topics">
                    <a href="https://www.douban.com/gallery/topic/16567/?from=hot_topic_anony_sns" class="rec_topics_name">你变成小时候所期待的大人模样了吗？</a>
                    
                    <span class="rec_topics_subtitle">新话题</span>
            </li>
    </ul>
</div>

      <!-- douban ad begin -->
      <li>
        <div id="dale_homepage_online_activity_promo_1"></div>
      </li>
      <li>
        <div id="dale_anonymous_homepage_doublemint"></div>
      </li>
      <!-- douban ad end -->
    </ul>
  </div>
</div>
  <div class="main">
<div class="mod">

  
    <h2>
        热点内容
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://www.douban.com/explore/" target="_self">更多</a>
                ) </span>
    </h2>

  <div class="albums">
    <ul>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/153740994/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/photo/albumcover/public/p2530536409.webp" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/153740994/">对生活热爱如昨。</a>
      <span class="num">126张照片</span>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/1659708524/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/albumcover/public/p2517142460.webp" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/1659708524/">甘南｜光芒引领。</a>
      <span class="num">48张照片</span>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/1660596367/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/photo/albumcover/public/p2519255768.webp" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/1660596367/">台湾之城市篇</a>
      <span class="num">288张照片</span>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/1660199003/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/albumcover/public/p2518238732.webp" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/1660199003/">还是那些樱花</a>
      <span class="num">99张照片</span>
    </ul>
  </div>
  <div class="notes">
    <ul>
      <li class="first">
      <div class="title">
          <a href="https://www.douban.com/note/682178109/">我听过最好的故事，是小时候奶奶坐在板凳上告诉我的</a>
      </div>
      <div class="author">
        豆瓣时间的日记
      </div>
      <p>奶奶讲故事的时候喜欢叙述细节，描述天气，讲旁人的只言片语，她心里的一个忽闪，...</p>
      </li>

      <li><a href="https://www.douban.com/note/681291646/">上一次，你感到快乐是什么时候？|马男波杰克，现代人的精神创伤病理手册</a></li>
      <li><a href="https://www.douban.com/note/625092950/">“我结婚前一天，我爸抽搐地在我奶奶家哭了好久，不说话，就是哭” | 父亲的50个脆弱瞬间</a></li>
      <li><a href="https://www.douban.com/note/673644060/">在我最自暴自弃的时候，是音乐给了我出口</a></li>
      <li><a href="https://www.douban.com/note/622826805/">小白放火</a></li>
      <li><a href="https://www.douban.com/note/623810857/">无缘高考：学生厌学、老师开店，“非重点”高中的夜与雾</a></li>
      <li><a href="https://www.douban.com/note/675599591/">知道点冷知识没什么用，但它能让你成为人群中的焦点</a></li>
      <li><a href="https://www.douban.com/note/623471280/">逃走的高考</a></li>
      <li><a href="https://www.douban.com/note/625255572/">少时并不知，跟父亲自在相处的时光，并非我们想象的无边无际</a></li>
      <li><a href="https://www.douban.com/note/680758842/">别去羡慕那些大作家，他们曾经和你一样不想动笔</a></li>
    </ul>
  </div>
</div>
</div>
  </div>
  

</div>








      
<div id="anony-time" class="section">
  <div class="wrapper">
  
  
    <div class="sidenav">
        <h2 class="section-title"><a href="https://time.douban.com?dt_time_source=douban-web_anonymous">豆瓣时间</a></h2>
    </div>

  <div class="side"></div>
  <div class="main">
    
    <h2>
        热门专栏
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://time.douban.com?dt_time_source=douban-web_anonymous" target="_self">更多</a>
                ) </span>
    </h2>


    



<ul class="time-list">
        <li>
            
            <a class="cover audio new " href="https://m.douban.com/time/column/99?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img1.doubanio.com/dae/niffler/niffler/images/81c6658c-6341-11e8-b830-0242ac110019.jpg" alt="古典音乐的奇幻之旅——从入门到上瘾的108堂课">
            </a>
            <a class="title" href="https://m.douban.com/time/column/99?dt_time_source=douban-web_anonymous" target="_blank">古典音乐的奇幻之旅——从入门到上瘾的108堂课</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover video new " href="https://m.douban.com/time/column/100?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img1.doubanio.com/dae/niffler/niffler/images/66a7d756-698e-11e8-b8c5-0242ac11002c.jpg" alt="花知道答案——中日名师插花课">
            </a>
            <a class="title" href="https://m.douban.com/time/column/100?dt_time_source=douban-web_anonymous" target="_blank">花知道答案——中日名师插花课</a>
            <span class="type">视频专栏</span>
        </li>
        <li>
            
            <a class="cover audio  new" href="https://m.douban.com/time/column/76?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img3.doubanio.com/dae/niffler/niffler/images/f90e218a-b8aa-11e7-9cc5-0242ac110021.jpg" alt="52倍人生——戴锦华大师电影课">
            </a>
            <a class="title" href="https://m.douban.com/time/column/76?dt_time_source=douban-web_anonymous" target="_blank">52倍人生——戴锦华大师电影课</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover audio new " href="https://m.douban.com/time/column/101?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img3.doubanio.com/dae/niffler/niffler/images/a1e1fedc-73ac-11e8-b5f7-0242ac110013.png" alt="花鸟鱼虫的生活意见——博物君的自然笔记">
            </a>
            <a class="title" href="https://m.douban.com/time/column/101?dt_time_source=douban-web_anonymous" target="_blank">花鸟鱼虫的生活意见——博物君的自然笔记</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover audio new " href="https://m.douban.com/time/column/98?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img1.doubanio.com/dae/niffler/niffler/images/3a845768-5da8-11e8-b5f8-0242ac110008.jpg" alt="美剧大爆炸——创作、脑洞与文化密码">
            </a>
            <a class="title" href="https://m.douban.com/time/column/98?dt_time_source=douban-web_anonymous" target="_blank">美剧大爆炸——创作、脑洞与文化密码</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover audio  new" href="https://m.douban.com/time/column/83?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img3.doubanio.com/dae/niffler/niffler/images/6da43bc4-cdd7-11e7-bb25-0242ac110014.png" alt="哲学闪耀时——不一样的西方哲学史">
            </a>
            <a class="title" href="https://m.douban.com/time/column/83?dt_time_source=douban-web_anonymous" target="_blank">哲学闪耀时——不一样的西方哲学史</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover audio  new" href="https://m.douban.com/time/column/85?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img3.doubanio.com/dae/niffler/niffler/images/f9493ac4-d428-11e7-a75c-0242ac11002e.jpg" alt="黑镜人生——网络生活的传播学肖像">
            </a>
            <a class="title" href="https://m.douban.com/time/column/85?dt_time_source=douban-web_anonymous" target="_blank">黑镜人生——网络生活的传播学肖像</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover audio  new" href="https://m.douban.com/time/column/91?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img3.doubanio.com/dae/niffler/niffler/images/c4972ec0-e3bf-11e7-9d88-0242ac110021.jpg" alt="一个故事的诞生——22堂创意思维写作课">
            </a>
            <a class="title" href="https://m.douban.com/time/column/91?dt_time_source=douban-web_anonymous" target="_blank">一个故事的诞生——22堂创意思维写作课</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover audio  " href="https://m.douban.com/time/column/96?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img1.doubanio.com/dae/niffler/niffler/images/bb95fef4-290c-11e8-accf-0242ac11000b.jpg" alt="12文豪——围绕日本文学的冒险">
            </a>
            <a class="title" href="https://m.douban.com/time/column/96?dt_time_source=douban-web_anonymous" target="_blank">12文豪——围绕日本文学的冒险</a>
            <span class="type">音频专栏</span>
        </li>
        <li>
            
            <a class="cover audio  " href="https://m.douban.com/time/column/95?dt_time_source=douban-web_anonymous" target="_blank">
                <img src="https://img3.doubanio.com/dae/niffler/niffler/images/2c50d150-3187-11e8-a133-0242ac110026.jpg" alt="成为更好的自己——许燕人格心理学32讲">
            </a>
            <a class="title" href="https://m.douban.com/time/column/95?dt_time_source=douban-web_anonymous" target="_blank">成为更好的自己——许燕人格心理学32讲</a>
            <span class="type">音频专栏</span>
        </li>
</ul>

</div>
  </div>
  
</div>








      
<div id="anony-video" class="section">
  <div class="wrapper">
  
  
    <div class="sidenav">
        <h2 class="section-title"><a href="https://video.douban.com?dt_time_source=douban-web_anonymous">视频</a></h2>
    </div>

  <div class="side"></div>
  <div class="main">
    
    <a href="https://video.douban.com/column/10018/">
        
    <h2>
        瓣嘴
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

    </a>
    
    <ul class="video-list video-rushi" data-id="10018">
        <li>
            <div class="video-cover"><a><span></span></a></div>
            <a class="video-title"></a>
        </li>
        <li>
            <div class="video-cover"><a><span></span></a></div>
            <a class="video-title"></a>
        </li>
        <li>
            <div class="video-cover"><a><span></span></a></div>
            <a class="video-title"></a>
        </li>
    </ul>


    <a href="https://video.douban.com/column/10008/">
        
    <h2>
        观影会客厅
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

    </a>
    
    <ul class="video-list video-banzui" data-id="10008">
        <li>
            <div class="video-cover"><a><span></span></a></div>
            <a class="video-title"></a>
        </li>
        <li>
            <div class="video-cover"><a><span></span></a></div>
            <a class="video-title"></a>
        </li>
        <li>
            <div class="video-cover"><a><span></span></a></div>
            <a class="video-title"></a>
        </li>
    </ul>

</div>
  </div>
  
</div>








      
<div id="anony-movie" class="section">
  <div class="wrapper">
  
  
<div class="sidenav">
  <h2 class="section-title"><a href="https://movie.douban.com">电影</a></h2>
  
  
  <div class="side-links nav-anon">
      <ul>
                          
                 <li><a href="https://movie.douban.com/nowplaying/">影讯&amp;购票</a></li>
             
                 <li class="site-nav-bt">
                     <a href="https://movie.douban.com/explore">选电影</a>
                     <img style="top: -5px; position: relative;" src="https://img3.doubanio.com/pics/new_menu.gif"/>
                 </li>
             
                 <li><a href="https://movie.douban.com/tv/">电视剧</a></li>
             
                 <li><a href="https://movie.douban.com/chart">排行榜</a></li>
             
                 <li><a href="https://movie.douban.com/tag/">分类</a></li>
             
                 <li><a href="https://movie.douban.com/review/best/">影评</a></li>
             
                 <li class="site-nav-bt"><a href="https://movie.douban.com/trailers">预告片</a></li>
             
                 <li><a href="https://movie.douban.com/askmatrix/hot_questions/all">问答</a></li>
      
      </ul>
  </div>
 
  


    <div class="apps-list">
    <ul>
    </ul>
    </div>

</div>

  <div class="side">
<div class="mod">


    <h2>
        影片分类
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://movie.douban.com/tag/?view=type" target="_self">更多</a>
                ) </span>
    </h2>

<div class="tags list">
  <ul>
    <li><a href="https://movie.douban.com/tag/爱情">爱情</a></li>
    <li><a href="https://movie.douban.com/tag/喜剧">喜剧</a></li>
    <li><a href="https://movie.douban.com/tag/剧情">剧情</a></li>
    <li><a href="https://movie.douban.com/tag/动画">动画</a></li>
    <li><a href="https://movie.douban.com/tag/科幻">科幻</a></li>
    <li><a href="https://movie.douban.com/tag/动作">动作</a></li>
    <li><a href="https://movie.douban.com/tag/经典">经典</a></li>
    <li><a href="https://movie.douban.com/tag/悬疑">悬疑</a></li>
    <li><a href="https://movie.douban.com/tag/犯罪">犯罪</a></li>
    <li><a href="https://movie.douban.com/tag/青春">青春</a></li>
    <li><a href="https://movie.douban.com/tag/惊悚">惊悚</a></li>
    <li><a href="https://movie.douban.com/tag/文艺">文艺</a></li>
    <li><a href="https://movie.douban.com/tag/搞笑">搞笑</a></li>
    <li><a href="https://movie.douban.com/tag/励志">励志</a></li>
    <li><a href="https://movie.douban.com/tag/纪录片">纪录片</a></li>
    <li><a href="https://movie.douban.com/tag/战争">战争</a></li>
    <li><a href="https://movie.douban.com/tag/恐怖">恐怖</a></li>
    <li><a href="https://movie.douban.com/tag/黑色幽默">黑色幽默</a></li>
    <li><a href="https://movie.douban.com/tag/美国">美国</a></li>
    <li><a href="https://movie.douban.com/tag/日本">日本</a></li>
    <li><a href="https://movie.douban.com/tag/香港">香港</a></li>
    <li><a href="https://movie.douban.com/tag/英国">英国</a></li>
    <li><a href="https://movie.douban.com/tag/中国">中国</a></li>
    <li><a href="https://movie.douban.com/tag/韩国">韩国</a></li>
    <li><a href="https://movie.douban.com/tag/法国">法国</a></li>
    <li><a href="https://movie.douban.com/tag/中国大陆">中国大陆</a></li>
    <li><a href="https://movie.douban.com/tag/台湾">台湾</a></li>
    <li><a href="https://movie.douban.com/tag/德国">德国</a></li>
  </ul>
</div>
</div>

<div class="mod">


    <h2>
        近期热门
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://movie.douban.com/chart" target="_self">更多</a>
                ) </span>
    </h2>

<div class="list1 movie-charts">
  <ol>
    <li>
    <a href="https://movie.douban.com/subject/26588308/">死侍2</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/26842702/">燃烧</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/26640371/">犬之岛</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/26721644/">鬼故事</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/26942645/">厕所英雄</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/26791452/">塔利</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/24773958/">复仇者联盟3：无限战争</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/27195080/">泄密者</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/26997663/">寂静之地</a>
    </li>
    <li>
    <a href="https://movie.douban.com/subject/26818314/">猛虫过江</a>
    </li>
  </ol>
</div>
</div>
</div>
  <div class="main">


    <h2>
        正在热映
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://movie.douban.com/showtimes/" target="_self">更多</a>
                ) </span>
    </h2>

<div class="movie-list list">
  <ul>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/26985127/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529571873.webp" alt="一出好戏" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/26985127/">一出好戏</a>
    </div>
    <div class="rating">
        <span class="allstar40"></span><i>7.4</i>
    </div>
    <a href="https://movie.douban.com/subject/26985127/cinema/" class="bn-link bn-ticket">选座购票</a>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/26426194/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530572643.webp" alt="巨齿鲨" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/26426194/">巨齿鲨</a>
    </div>
    <div class="rating">
        <span class="allstar30"></span><i>6.1</i>
    </div>
    <a href="https://movie.douban.com/subject/26426194/cinema/" class="bn-link bn-ticket">选座购票</a>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/24852545/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2521648155.webp" alt="爱情公寓" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/24852545/">爱情公寓</a>
    </div>
    <div class="rating">
        <span class="allstar15"></span><i>2.7</i>
    </div>
    <a href="https://movie.douban.com/subject/24852545/cinema/" class="bn-link bn-ticket">选座购票</a>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/27605698/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529206747.webp" alt="西虹市首富" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/27605698/">西虹市首富</a>
    </div>
    <div class="rating">
        <span class="allstar35"></span><i>6.7</i>
    </div>
    <a href="https://movie.douban.com/subject/27605698/cinema/" class="bn-link bn-ticket">选座购票</a>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/30208005/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2528380655.webp" alt="神秘世界历险记4" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/30208005/">神秘世界历险记...</a>
    </div>
    <div class="rating">
        <span class="allstar30"></span><i>5.5</i>
    </div>
    <a href="https://movie.douban.com/subject/30208005/cinema/" class="bn-link bn-ticket">选座购票</a>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/30146756/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530872223.webp" alt="风语咒" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/30146756/">风语咒</a>
    </div>
    <div class="rating">
        <span class="allstar35"></span><i>7.0</i>
    </div>
    <a href="https://movie.douban.com/subject/30146756/cinema/" class="bn-link bn-ticket">选座购票</a>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/27622447/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530599636.webp" alt="小偷家族" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/27622447/">小偷家族</a>
    </div>
    <div class="rating">
        <span class="allstar45"></span><i>8.7</i>
    </div>
    <a href="https://movie.douban.com/subject/27622447/cinema/" class="bn-link bn-ticket">选座购票</a>
    <li>
    <div class="pic">
        <a href="https://movie.douban.com/subject/25882296/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2526405034.webp" alt="狄仁杰之四大天王" /></a>
    </div>
    <div class="title">
      <a href="https://movie.douban.com/subject/25882296/">狄仁杰之四大天...</a>
    </div>
    <div class="rating">
        <span class="allstar35"></span><i>6.5</i>
    </div>
    <a href="https://movie.douban.com/subject/25882296/cinema/" class="bn-link bn-ticket">选座购票</a>
  </ul>
</div>
</div>
  </div>
  
    <div id="dale_anonymous_homepage_movie_bottom" class="extra"></div>

</div>








      
<div id="anony-group" class="section">
  <div class="wrapper">
  
  
<div class="sidenav">
  <h2 class="section-title"><a href="https://www.douban.com/group/">小组</a></h2>
  
  
  <div class="side-links nav-anon">
      <ul>
                          
                 <li><a href="/group/explore">精选</a></li>
             
                 <li><a href="/group/explore/culture">文化</a></li>
             
                 <li><a href="/group/explore/travel">行摄</a></li>
             
                 <li><a href="/group/explore/ent">娱乐</a></li>
             
                 <li><a href="/group/explore/fashion">时尚</a></li>
             
                 <li><a href="/group/explore/life">生活</a></li>
             
                 <li><a href="/group/explore/tech">科技</a></li>
      
      </ul>
  </div>
 
  


    <div class="apps-list">
    <ul>
    </ul>
    </div>

</div>

  <div class="side">
<div class="mod">

    <h2>
        小组分类
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=兴趣">兴趣&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=旅行">旅行</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=摄影">摄影</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=影视">影视</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=音乐">音乐</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=文学">文学</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=游戏">游戏</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=动漫">动漫</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=运动">运动</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=戏曲">戏曲</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=桌游">桌游</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=怪癖">怪癖</a></li>
       </ul>
    </div>
   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=生活">生活&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=健康">健康</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=美食">美食</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=宠物">宠物</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=美容">美容</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=化妆">化妆</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=护肤">护肤</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=服饰">服饰</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=公益">公益</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=家庭">家庭</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=育儿">育儿</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=汽车">汽车</a></li>
       </ul>
    </div>
   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=购物">购物&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=淘宝">淘宝</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=二手">二手</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=团购">团购</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=数码">数码</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=品牌">品牌</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=文具">文具</a></li>
       </ul>
    </div>
   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=社会">社会&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=求职">求职</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=租房">租房</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=励志">励志</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=留学">留学</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=出国">出国</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=理财">理财</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=传媒">传媒</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=创业">创业</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=考试">考试</a></li>
       </ul>
    </div>
   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=艺术">艺术&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=设计">设计</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=手工">手工</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=展览">展览</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=曲艺">曲艺</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=舞蹈">舞蹈</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=雕塑">雕塑</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=纹身">纹身</a></li>
       </ul>
    </div>
   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=学术">学术&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=人文">人文</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=社科">社科</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=自然">自然</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=建筑">建筑</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=国学">国学</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=语言">语言</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=宗教">宗教</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=哲学">哲学</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=软件">软件</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=硬件">硬件</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=互联网">互联网</a></li>
       </ul>
    </div>
   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=情感">情感&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=恋爱">恋爱</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=心情">心情</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=心理学">心理学</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=星座">星座</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=塔罗">塔罗</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=LES">LES</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=GAY">GAY</a></li>
       </ul>
    </div>
   <div class="cate group-cate">
       <ul>
       <li class="cate-label"><a href="https://www.douban.com/group/explore?tag=闲聊">闲聊&raquo; </a></li>
       <li><a href="https://www.douban.com/group/explore?tag=吐槽">吐槽</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=笑话">笑话</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=直播">直播</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=八卦">八卦</a></li>
       <li><a href="https://www.douban.com/group/explore?tag=发泄">发泄</a></li>
       </ul>
    </div>
</div>
</div>
  <div class="main">


    <h2>
        热门小组
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://www.douban.com/group/explore" target="_self">更多</a>
                ) </span>
    </h2>

<div class="group-list list">
  <ul>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/407193/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/group/sqxs/public/c285ce8ca3631db.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/407193/">帮帮组™加入这个组就有人帮你了！</a>
      </div>
      15589 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/echofans/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/group/sqxs/public/ef4bd6235a7c6c2.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/echofans/">我爱三毛</a>
      </div>
      45166 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/shafake/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/group/sqxs/public/063bb07a807a340.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/shafake/">沙发客</a>
      </div>
      22314 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/liucixin/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/group/sqxs/public/68b08f0f3595407.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/liucixin/">刘慈欣</a>
      </div>
      25957 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/20618/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/group/sqxs/public/8f11b2285655782.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/20618/">西双版纳</a>
      </div>
      10710 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/402725/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/group/sqxs/public/17fdb616ff143d8.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/402725/">记事本圆梦小组</a>
      </div>
      113050 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/dashan/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/icon/g33120-3.jpg" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/dashan/">搭讪学</a>
      </div>
      93666 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/170177/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/group/sqxs/public/2e49d167d4322c2.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/170177/">这辈子一定要做几件疯狂的事</a>
      </div>
      93174 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/cuthair/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/icon/g109498-1.jpg" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/cuthair/">自己给自己剪头发</a>
      </div>
      35197 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/83759/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/icon/g83759-2.jpg" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/83759/">我们就是要做衣服给自己穿</a>
      </div>
      3789 个成员
    </div>
    <li>
    <div class="pic">
        <a href="https://www.douban.com/group/362263/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/group/sqxs/public/e6ba9bc4c8facbe.webp" alt="" width="48" /></a>
    </div>
    <div class="info">
      <div class="title">
        <a href="https://www.douban.com/group/362263/">对象太他妈难找了党-单身凸^-^凸</a>
      </div>
      15733 个成员
    </div>
  </ul>
</div>
</div>
  </div>
  
</div>








      
<div id="anony-book" class="section">
  <div class="wrapper">
  
  
<div class="sidenav">
  <div class="mod">
  <h2 class="section-title"><a href="https://book.douban.com">读书</a></h2>
  
  
  <div class="side-links nav-anon">
      <ul>
                                                    
                 <li><a href="https://book.douban.com/tag/">分类浏览</a></li>
             
                <li>
                    <a target="_blank" href="https://read.douban.com?dcn=entry&amp;dcs=book-nav&amp;dcm=douban">阅读</a>
                    <img style="top: 4px; position: absolute;" src="https://img3.doubanio.com/pics/new_menu.gif"/>
                </li>
             
                 <li><a href="https://book.douban.com/writers/">作者</a></li>
             
                 <li><a href="https://book.douban.com/review/best/">书评</a></li>
      
          <li class="site-nav-prom">
              <a class="lnk-buy" href="https://book.douban.com/cart">
                  <em>购书单</em>
              </a>
          </li>
      </ul>
  </div>
 
  </div>

  


    <div class="apps-list">
    <ul>
    <li><a href="https://read.douban.com/app/" class="lnk-icon"><i class="app-icon app-icon-read"></i></a><a href="https://read.douban.com/app/">豆瓣阅读</a></li>
    </ul>
    </div>

</div>

  <div class="side">

<div class="mod">

    <h2>
        热门标签
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://book.douban.com/tag/?view=type" target="_self">更多</a>
                ) </span>
    </h2>

<div class="book-cate-mod">
<div class="cate book-cate">
  <ul>
  <li class="cate-label">[文学]</li>
  <li><a href="https://book.douban.com/tag/小说">小说</a></li>
  <li><a href="https://book.douban.com/tag/随笔">随笔</a></li>
  <li><a href="https://book.douban.com/tag/日本文学">日本文学</a></li>
  <li><a href="https://book.douban.com/tag/散文">散文</a></li>
  <li><a href="https://book.douban.com/tag/诗歌">诗歌</a></li>
  <li><a href="https://book.douban.com/tag/童话">童话</a></li>
  <li><a href="https://book.douban.com/tag/名著">名著</a></li>
  <li><a href="https://book.douban.com/tag/港台">港台</a></li>
  <li><a href="https://book.douban.com/tag/?view=type#文学">更多</a></li>
  </ul>
</div>
<div class="cate book-cate">
  <ul>
  <li class="cate-label">[流行]</li>
  <li><a href="https://book.douban.com/tag/漫画">漫画</a></li>
  <li><a href="https://book.douban.com/tag/推理">推理</a></li>
  <li><a href="https://book.douban.com/tag/绘本">绘本</a></li>
  <li><a href="https://book.douban.com/tag/青春">青春</a></li>
  <li><a href="https://book.douban.com/tag/科幻">科幻</a></li>
  <li><a href="https://book.douban.com/tag/言情">言情</a></li>
  <li><a href="https://book.douban.com/tag/奇幻">奇幻</a></li>
  <li><a href="https://book.douban.com/tag/武侠">武侠</a></li>
  <li><a href="https://book.douban.com/tag/?view=type#流行">更多</a></li>
  </ul>
</div>
<div class="cate book-cate">
  <ul>
  <li class="cate-label">[文化]</li>
  <li><a href="https://book.douban.com/tag/历史">历史</a></li>
  <li><a href="https://book.douban.com/tag/哲学">哲学</a></li>
  <li><a href="https://book.douban.com/tag/传记">传记</a></li>
  <li><a href="https://book.douban.com/tag/设计">设计</a></li>
  <li><a href="https://book.douban.com/tag/建筑">建筑</a></li>
  <li><a href="https://book.douban.com/tag/电影">电影</a></li>
  <li><a href="https://book.douban.com/tag/回忆录">回忆录</a></li>
  <li><a href="https://book.douban.com/tag/音乐">音乐</a></li>
  <li><a href="https://book.douban.com/tag/?view=type#文化">更多</a></li>
  </ul>
</div>
<div class="cate book-cate">
  <ul>
  <li class="cate-label">[生活]</li>
  <li><a href="https://book.douban.com/tag/旅行">旅行</a></li>
  <li><a href="https://book.douban.com/tag/励志">励志</a></li>
  <li><a href="https://book.douban.com/tag/职场">职场</a></li>
  <li><a href="https://book.douban.com/tag/教育">教育</a></li>
  <li><a href="https://book.douban.com/tag/美食">美食</a></li>
  <li><a href="https://book.douban.com/tag/灵修">灵修</a></li>
  <li><a href="https://book.douban.com/tag/健康">健康</a></li>
  <li><a href="https://book.douban.com/tag/家居">家居</a></li>
  <li><a href="https://book.douban.com/tag/?view=type#生活">更多</a></li>
  </ul>
</div>
<div class="cate book-cate">
  <ul>
  <li class="cate-label">[经管]</li>
  <li><a href="https://book.douban.com/tag/经济学">经济学</a></li>
  <li><a href="https://book.douban.com/tag/管理">管理</a></li>
  <li><a href="https://book.douban.com/tag/商业">商业</a></li>
  <li><a href="https://book.douban.com/tag/金融">金融</a></li>
  <li><a href="https://book.douban.com/tag/营销">营销</a></li>
  <li><a href="https://book.douban.com/tag/理财">理财</a></li>
  <li><a href="https://book.douban.com/tag/股票">股票</a></li>
  <li><a href="https://book.douban.com/tag/企业史">企业史</a></li>
  <li><a href="https://book.douban.com/tag/?view=type#经管">更多</a></li>
  </ul>
</div>
<div class="cate book-cate">
  <ul>
  <li class="cate-label">[科技]</li>
  <li><a href="https://book.douban.com/tag/科普">科普</a></li>
  <li><a href="https://book.douban.com/tag/互联网">互联网</a></li>
  <li><a href="https://book.douban.com/tag/编程">编程</a></li>
  <li><a href="https://book.douban.com/tag/交互设计">交互设计</a></li>
  <li><a href="https://book.douban.com/tag/算法">算法</a></li>
  <li><a href="https://book.douban.com/tag/通信">通信</a></li>
  <li><a href="https://book.douban.com/tag/神经网络">神经网络</a></li>
  <li><a href="https://book.douban.com/tag/?view=type#科技">更多</a></li>
  </ul>
</div>
</div>
</div>
</div>
  <div class="main">

<div class="mod">

    <h2>
        新书速递
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://book.douban.com/latest" target="_self">更多</a>
                ) </span>
    </h2>

<div class="book-list list">
  <ul>
      <li>
      <div class="pic">
          <a href="https://book.douban.com/subject/30194496/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/m/public/s29827942.jpg" alt="朋友之间" /></a>
      </div>
      <div class="title">
        <a href="https://book.douban.com/subject/30194496/" >朋友之间</a>
      </div>
      <div class="author">〔以色列〕阿摩...</div>
      <a href="https://read.douban.com/reader/ebook/55371745/" target="_blank" class="bn-link">免费试读</a>
      <li>
      <div class="pic">
          <a href="https://book.douban.com/subject/27598730/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/subject/m/public/s29803767.jpg" alt="突然死亡" /></a>
      </div>
      <div class="title">
        <a href="https://book.douban.com/subject/27598730/" >突然死亡</a>
      </div>
      <div class="author">〔墨〕阿尔瓦罗...</div>
      <a href="https://read.douban.com/reader/ebook/55524885/" target="_blank" class="bn-link">免费试读</a>
      <li>
      <div class="pic">
          <a href="https://book.douban.com/subject/30254431/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/m/public/s29799206.jpg" alt="被猜死的人" /></a>
      </div>
      <div class="title">
        <a href="https://book.douban.com/subject/30254431/" >被猜死的人</a>
      </div>
      <div class="author">田耳</div>
      <a href="https://read.douban.com/reader/ebook/55523827/" target="_blank" class="bn-link">免费试读</a>
      <li>
      <div class="pic">
          <a href="https://book.douban.com/subject/28170953/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/m/public/s29823916.jpg" alt="荣耀" /></a>
      </div>
      <div class="title">
        <a href="https://book.douban.com/subject/28170953/" >荣耀</a>
      </div>
      <div class="author">〔美〕弗拉基米...</div>
      <a href="https://read.douban.com/reader/ebook/55519311/" target="_blank" class="bn-link">免费试读</a>
  </ul>
</div>
</div>

<div class="mod">

    <h2>
        原创数字作品
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://read.douban.com/ebooks/" target="_self">更多</a>
                ) </span>
    </h2>

<div class="book-list list">
  <ul>
    <li>
    <div class="pic">
        <a href="https://read.douban.com/ebook/49182289" target="_blank"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/ark_article_cover/large/public/49182289.jpg?v=1522077947.0" alt="一窟鬼" /></a>
    </div>
    <div class="title">
      <a href="https://read.douban.com/ebook/49182289" target="_blank">一窟鬼</a>
    </div>
    <div class="author">林津鲈</div>
    <div class="price">
        1.99元
    </div>
    <a href="https://read.douban.com/reader/ebook/49182289/" target="_blank" class="bn-link">免费试读</a>
    <li>
    <div class="pic">
        <a href="https://read.douban.com/ebook/52252225" target="_blank"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/ark_article_cover/large/public/52252225.jpg?v=1531102811.0" alt="不速之客" /></a>
    </div>
    <div class="title">
      <a href="https://read.douban.com/ebook/52252225" target="_blank">不速之客</a>
    </div>
    <div class="author">三七</div>
    <div class="price">
        2.99元
    </div>
    <a href="https://read.douban.com/reader/ebook/52252225/" target="_blank" class="bn-link">免费试读</a>
    <li>
    <div class="pic">
        <a href="https://read.douban.com/ebook/54203709" target="_blank"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/ark_article_cover/large/public/54203709.jpg?v=1532685583.0" alt="一生一次" /></a>
    </div>
    <div class="title">
      <a href="https://read.douban.com/ebook/54203709" target="_blank">一生一次</a>
    </div>
    <div class="author">七月果</div>
    <div class="price">
        6.99元
    </div>
    <a href="https://read.douban.com/reader/ebook/54203709/" target="_blank" class="bn-link">免费试读</a>
    <li>
    <div class="pic">
        <a href="https://read.douban.com/ebook/52177965" target="_blank"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/ark_article_cover/large/public/52177965.jpg?v=1531106035.0" alt="心心斋之婚恋解密" /></a>
    </div>
    <div class="title">
      <a href="https://read.douban.com/ebook/52177965" target="_blank">心心斋之婚恋解...</a>
    </div>
    <div class="author">陈敬之</div>
    <div class="price">
        4.99元
    </div>
    <a href="https://read.douban.com/reader/ebook/52177965/" target="_blank" class="bn-link">免费试读</a>
  </ul>
</div>
</div>
</div>
  </div>
  
</div>








      
<div id="anony-music" class="section">
  <div class="wrapper">
  
  
  <div class="sidenav">
    <h2 class="section-title"><a href="https://music.douban.com">音乐</a></h2>
    
  
  <div class="side-links nav-anon">
      <ul>
                          
                 <li><a href="https://music.douban.com/artists/">音乐人</a></li>
             
                 <li><a href="https://www.douban.com/wetware/">潮潮豆瓣音乐周</a></li>
             
                 <li><a href="https://music.douban.com/artists/royalty/">金羊毛计划</a></li>
             
                 <li><a href="https://music.douban.com/topics/">专题</a></li>
             
                 <li><a href="https://music.douban.com/chart">排行榜</a></li>
             
                 <li><a href="https://music.douban.com/tag/">分类浏览</a></li>
             
                 <li><a href="https://music.douban.com/review/latest/">乐评</a></li>
             
                 <li><a href="https://douban.fm/?from_=music_nav">豆瓣FM</a></li>
             
                 <li><a href="https://douban.fm/explore/songlists/">歌单</a></li>
             
                 <li><a href="https://artist.douban.com/abilu/">阿比鹿音乐奖</a></li>
      
      </ul>
  </div>

    


    <div class="apps-list">
    <ul>
    <li><a href="https://douban.fm/app?from_=shire_anonymous_home" class="lnk-icon"><i class="app-icon app-icon-fm"></i></a><a href="https://douban.fm/app?from_=shire_anonymous_home">豆瓣FM</a></li>
    <li><a href="https://artist.douban.com/app" class="lnk-icon"><i class="app-icon app-icon-artists"></i></a><a href="https://artist.douban.com/app">豆瓣音乐人</a></li>
    </ul>
    </div>

  </div>

  <div class="side">
  <div class="mod">
    
    
    <h2>
        本周流行音乐人
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://music.douban.com/artists/" target="_self">更多</a>
                ) </span>
    </h2>

    <div class="list1 artist-charts">
      <ul>
          <li>
            <span class="num">1.</span>
            <div class="pic artist-song-play" data-sids="[&#34;731383&#34;, &#34;602203&#34;, &#34;603364&#34;]">
              <a href="https://site.douban.com/philoenigma/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/site/small/public/79d44ffaedd6a10.jpg" width="48"></a>
              <i class="icon icon-bg"></i>
              <i class="icon icon-stat icon-play"></i>
            </div>
            <div class="content">
              <a href="https://site.douban.com/philoenigma/">Phigma</a>
              <div class="desc">
                流派: 世界音乐 World
                <br>247人关注
              </div>
            </div>
          </li>
          <li>
            <span class="num">2.</span>
            <div class="pic artist-song-play" data-sids="[&#34;731360&#34;, &#34;105155&#34;, &#34;352764&#34;]">
              <a href="https://site.douban.com/AirS/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/site/small/public/69012f1f266e51a.jpg" width="48"></a>
              <i class="icon icon-bg"></i>
              <i class="icon icon-stat icon-play"></i>
            </div>
            <div class="content">
              <a href="https://site.douban.com/AirS/">AirS</a>
              <div class="desc">
                流派: 流行 Pop
                <br>298人关注
              </div>
            </div>
          </li>
          <li>
            <span class="num">3.</span>
            <div class="pic artist-song-play" data-sids="[&#34;730805&#34;, &#34;730492&#34;, &#34;730484&#34;]">
              <a href="https://site.douban.com/DVC/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/site/small/public/f4e3b525ec4b314.jpg" width="48"></a>
              <i class="icon icon-bg"></i>
              <i class="icon icon-stat icon-play"></i>
            </div>
            <div class="content">
              <a href="https://site.douban.com/DVC/">DVC</a>
              <div class="desc">
                流派: 说唱 Rap
                <br>140人关注
              </div>
            </div>
          </li>
          <li>
            <span class="num">4.</span>
            <div class="pic artist-song-play" data-sids="[&#34;731254&#34;, &#34;355635&#34;, &#34;731253&#34;]">
              <a href="https://site.douban.com/Dizkar/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/site/small/public/ca842a37438cd7b.jpg" width="48"></a>
              <i class="icon icon-bg"></i>
              <i class="icon icon-stat icon-play"></i>
            </div>
            <div class="content">
              <a href="https://site.douban.com/Dizkar/">地磁卡</a>
              <div class="desc">
                流派: 说唱 Rap
                <br>238人关注
              </div>
            </div>
          </li>
          <li>
            <span class="num">5.</span>
            <div class="pic artist-song-play" data-sids="[&#34;730232&#34;, &#34;41581&#34;, &#34;41587&#34;]">
              <a href="https://site.douban.com/miserablefaith/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/site/small/public/28f3a69d8925227.jpg" width="48"></a>
              <i class="icon icon-bg"></i>
              <i class="icon icon-stat icon-play"></i>
            </div>
            <div class="content">
              <a href="https://site.douban.com/miserablefaith/">痛仰</a>
              <div class="desc">
                流派: 摇滚 Rock
                <br>102068人关注
              </div>
            </div>
          </li>
      </ul>
    </div>
  </div>
</div>
  <div class="main">

  
    
    <h2>
        豆瓣新碟榜
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://music.douban.com#new1" target="_self">更多</a>
                ) </span>
    </h2>

    <div class="album-list list">
      <ul>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30283109/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/subject/s/public/s29834568.jpg" alt="1" style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              1. <a href="https://music.douban.com/subject/30283109/">1</a>
            </div>
            <div class="artist">
              <a href="">蔡徐坤</a>
            </div>
            <div class="rating">
              <span class="allstar30"></span><i>6.0</i>
            </div>
          </li>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30283133/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/s/public/s29828321.jpg" alt="丹青千里" style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              2. <a href="https://music.douban.com/subject/30283133/">丹青千里</a>
            </div>
            <div class="artist">
              <a href="">易烊千玺 Jackson Yee</a>
            </div>
            <div class="rating">
              <span class="allstar40"></span><i>7.3</i>
            </div>
          </li>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30258487/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/s/public/s29804776.jpg" alt="寻宝游戏" style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              3. <a href="https://music.douban.com/subject/30258487/">寻宝游戏</a>
            </div>
            <div class="artist">
              <a href="">许嵩</a>
            </div>
            <div class="rating">
              <span class="allstar40"></span><i>7.5</i>
            </div>
          </li>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30263007/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/s/public/s29808194.jpg" alt="看不见的城市" style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              4. <a href="https://music.douban.com/subject/30263007/">看不见的城市</a>
            </div>
            <div class="artist">
              <a href="">惘闻</a>
            </div>
            <div class="rating">
              <span class="allstar45"></span><i>8.4</i>
            </div>
          </li>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30245730/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/s/public/s29842956.jpg" alt="Queen" style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              5. <a href="https://music.douban.com/subject/30245730/">Queen</a>
            </div>
            <div class="artist">
              <a href="">尼基·米纳杰  Nicki Minaj</a>
            </div>
            <div class="rating">
              <span class="allstar45"></span><i>8.3</i>
            </div>
          </li>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30247502/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/subject/s/public/s29792561.jpg" alt="Know." style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              6. <a href="https://music.douban.com/subject/30247502/">Know.</a>
            </div>
            <div class="artist">
              <a href="">Jason Mraz</a>
            </div>
            <div class="rating">
              <span class="allstar35"></span><i>7.0</i>
            </div>
          </li>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30282081/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/subject/s/public/s29838299.jpg" alt="Summer Magic" style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              7. <a href="https://music.douban.com/subject/30282081/">Summer Magic</a>
            </div>
            <div class="artist">
              <a href="">红色天鹅绒 Red Velvet</a>
            </div>
            <div class="rating">
              <span class="allstar35"></span><i>6.5</i>
            </div>
          </li>
          <li>
            <div class="pic">
              <a href="https://music.douban.com/subject/30293554/">
                <img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/subject/s/public/s29839027.jpg" alt="TROUBLE" style="width: 80px; max-height: 120px;"/>
              </a>
            </div>
            <div class="title">
              8. <a href="https://music.douban.com/subject/30293554/">TROUBLE</a>
            </div>
            <div class="artist">
              <a href="">浜崎あゆみ 滨崎步 Ayumi Hamasaki ayumi hamasaki</a>
            </div>
            <div class="rating">
              <span class="allstar35"></span><i>6.5</i>
            </div>
          </li>
      </ul>
    </div>

  
  
    <h2>
        热门歌单
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://music.douban.com/programmes/" target="_self">更多</a>
                ) </span>
    </h2>

  <div class="programme-list list">
    <ul>
        
          <li>
            <div class="pic cover"><img width=80 src="https://img3.doubanio.com/img/songlist/large/360375-1.jpg"><a href="https://music.douban.com/programme/360375" target="_blank"><i></i></a></div>
            <div class="title">克莱德曼及其他</div>
          </li>
        
          <li>
            <div class="pic cover"><img width=80 src="https://img3.doubanio.com/img/songlist/large/7344236-3.jpg"><a href="https://music.douban.com/programme/7344236" target="_blank"><i></i></a></div>
            <div class="title">ZARD激励我的每一天</div>
          </li>
        
          <li>
            <div class="pic cover"><img width=80 src="https://img3.doubanio.com/img/songlist/large/1393011-3.jpg"><a href="https://music.douban.com/programme/1393011" target="_blank"><i></i></a></div>
            <div class="title">船窗外的星云</div>
          </li>
        
          <li>
            <div class="pic cover"><img width=80 src="https://img3.doubanio.com/img/songlist/large/10002858-1.jpg"><a href="https://music.douban.com/programme/10002858" target="_blank"><i></i></a></div>
            <div class="title">德国美味拼盘-乡村雷鬼爵士102</div>
          </li>
        
          <li>
            <div class="pic cover"><img width=80 src="https://img3.doubanio.com/img/songlist/large/6719629-3.jpg"><a href="https://music.douban.com/programme/6719629" target="_blank"><i></i></a></div>
            <div class="title">打动你的声音</div>
          </li>
        
          <li>
            <div class="pic cover"><img width=80 src="https://img3.doubanio.com/img/songlist/large/11116-1.jpg"><a href="https://music.douban.com/programme/11116" target="_blank"><i></i></a></div>
            <div class="title">天淋清韵</div>
          </li>
    </ul>
  </div>

</div>
  </div>
  
  <div id="dale_anonymous_home_page_middle_2" class="extra"></div>

</div>








      
<div id="anony-market" class="section">
  <div class="wrapper">
  
  
<div class="sidenav">
  <h2 class="section-title">
    <a href="https://market.douban.com?dcs=anonymous-home-sidenav&amp;dcm=douban">
      豆品
    </a>
  </h2>
</div>

  <div class="side">
<div class="mod">
  
    <h2>
        热门活动
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

  <ul class="market-topics">
      <li class="market-topic-item" >
        <a href="https://www.douban.com/update/topic/%E6%88%91%E9%80%89%E6%97%A9%E9%A4%90?dcm=douban&dcs=anonymous-home-topic"
          target="_blank">
          <div class="market-topic-pic"
            style="background-image:url(https://img3.doubanio.com/img/files/file-1513305186-3.jpg)">
          </div>
        </a>
        <p class="market-topic-footer">
          <a href="https://www.douban.com/update/topic/%E6%88%91%E9%80%89%E6%97%A9%E9%A4%90?dcm=douban&dcs=anonymous-home-topic"
            target="_blank">
          我的豆瓣收藏夹里有什么
          </a>
        </p>
      </li>
  </ul>
</div>

  <div class="mod">
    
    <h2>
        官方小组
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://www.douban.com/group/588598?dcs=anonymous-home-more-shops&amp;dcm=douban#hot-shop-wrapper" target="_self">更多</a>
                ) </span>
    </h2>

    <ul class="market-group-topics">
        <li>
          <p class="market-group-topic-title">
            <a href="https://www.douban.com/group/topic/110121403?dcm=douban&dcs=anonymous-home-group"
              target="_blank">
              2018豆瓣电影日历发货时间答疑
            </a>
          </p>
          <p class="market-group-topic-footer">
            <span class="market-group-topic-date">
              01-03
            </span>
            <span class="market-group-topic-amount">
              94 人参与
            </span>
          </p>
        </li>
        <li>
          <p class="market-group-topic-title">
            <a href="https://www.douban.com/group/topic/109227642?dcm=douban&dcs=anonymous-home-group"
              target="_blank">
              有奖建议征集→你心目中“豆瓣”味道的咖啡豆是什么味？
            </a>
          </p>
          <p class="market-group-topic-footer">
            <span class="market-group-topic-date">
              03-12
            </span>
            <span class="market-group-topic-amount">
              92 人参与
            </span>
          </p>
        </li>
        <li>
          <p class="market-group-topic-title">
            <a href="https://www.douban.com/group/topic/109228247?dcm=douban&dcs=anonymous-home-group"
              target="_blank">
              有奖建议征集→如果出一款手机壳，你希望上面有什么样的设计？
            </a>
          </p>
          <p class="market-group-topic-footer">
            <span class="market-group-topic-date">
              07-03
            </span>
            <span class="market-group-topic-amount">
              333 人参与
            </span>
          </p>
        </li>
    </ul>
  </div>
</div>
  <div class="main">
  
    <h2>
        热卖商品
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://market.douban.com?dcs=anonymous-home-more-skus&amp;dcm=douban" target="_self">更多</a>
                ) </span>
    </h2>

  <ul class="market-spu-list">
      
      <li class="main-sku">
        <a href="https://market.douban.com/campaign/calendar2018?dcm=douban&dcs=anonymous-home-spu"
          target="_blank">
          <div class="market-spu-pic"
            style="background-image: url(https://img3.doubanio.com/img/files/file-1513305186-0.jpg)">
          </div>
        </a>
        <div class="market-spu-footer">
          <span class="market-spu-price">
            ￥98.00
          </span>
          <a href="https://market.douban.com/campaign/calendar2018?dcm=douban&dcs=anonymous-home-spu"
            target="_blank"
            class="market-spu-title">
            豆瓣电影日历2018
          </a>
        </div>
    </li>
      
      <li class="main-sku">
        <a href="https://market.douban.com/campaign/notebook?dcm=douban&dcs=anonymous-home-spu"
          target="_blank">
          <div class="market-spu-pic"
            style="background-image: url(https://img3.doubanio.com/img/files/file-1513305186-5.jpg)">
          </div>
        </a>
        <div class="market-spu-footer">
          <span class="market-spu-price">
            ￥48.00
          </span>
          <a href="https://market.douban.com/campaign/notebook?dcm=douban&dcs=anonymous-home-spu"
            target="_blank"
            class="market-spu-title">
            布面精装本
          </a>
        </div>
    </li>
      
      <li class="main-sku">
        <a href="https://market.douban.com/campaign/collection?dcm=douban&dcs=anonymous-home-spu"
          target="_blank">
          <div class="market-spu-pic"
            style="background-image: url(https://img3.doubanio.com/img/files/file-1513305186-4.jpg)">
          </div>
        </a>
        <div class="market-spu-footer">
          <span class="market-spu-price">
            ￥99.00
          </span>
          <a href="https://market.douban.com/campaign/collection?dcm=douban&dcs=anonymous-home-spu"
            target="_blank"
            class="market-spu-title">
            豆瓣收藏夹
          </a>
        </div>
    </li>
      
      <li class="main-sku">
        <a href="https://market.douban.com/campaign/canvasbag?dcm=douban&dcs=anonymous-home-spu"
          target="_blank">
          <div class="market-spu-pic"
            style="background-image: url(https://img3.doubanio.com/img/files/file-1513305186-2.jpg)">
          </div>
        </a>
        <div class="market-spu-footer">
          <span class="market-spu-price">
            ￥149.00
          </span>
          <a href="https://market.douban.com/campaign/canvasbag?dcm=douban&dcs=anonymous-home-spu"
            target="_blank"
            class="market-spu-title">
            帆布包·早餐系列
          </a>
        </div>
    </li>
    </ul>
</div>
  </div>
  
</div>








      
<div id="anony-events" class="section">
  <div class="wrapper">
  
  
<div class="sidenav">
  <h2 class="section-title"><a href="https://www.douban.com/location/">同城</a></h2>
  
  
  <div class="side-links nav-anon">
      <ul>
        
  
    
    <li>
        <a
        href="https://www.douban.com/location/shenzhen/events">近期活动</a>
    </li>
    
    <li>
        <a
        href="https://www.douban.com/location/shenzhen/hosts">主办方</a>
    </li>
    
    <li>
        <a
        href="https://www.douban.com/location/drama/">舞台剧</a>
    </li>

      
      </ul>
  </div>
 
  


    <div class="apps-list">
    <ul>
    </ul>
    </div>

</div>

  <div class="side">

<div class="mod">

    <h2>
        活动标签
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
    </h2>

<div class="cate events-cate">
  <ul>
  <li class="cate-label"><a href="https://www.douban.com/location/shenzhen/events/week-music">音乐&raquo;</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1001">小型现场</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1002">音乐会</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1003">演唱会</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1004">音乐节</a></li>
  </ul>
</div>
<div class="cate events-cate">
  <ul>
  <li class="cate-label"><a href="https://www.douban.com/location/shenzhen/events/week-drama">戏剧&raquo;</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1101">话剧</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1102">音乐剧</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1103">舞剧</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1104">歌剧</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1105">戏曲</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1106">其他</a></li>
  </ul>
</div>
<div class="cate events-cate">
  <ul>
  <li class="cate-label"><a href="https://www.douban.com/location/shenzhen/events/week-party">聚会&raquo;</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1401">生活</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1402">集市</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1403">摄影</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1404">外语</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1405">桌游</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1406">夜店</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1407">交友</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1408">美食</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1409">派对</a></li>
  </ul>
</div>
<div class="cate events-cate">
  <ul>
  <li class="cate-label"><a href="https://www.douban.com/location/shenzhen/events/week-film">电影&raquo;</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1801">主题放映</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1802">影展</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-1803">影院活动</a></li>
  </ul>
</div>
<div class="cate events-cate">
  <ul>
  <li class="cate-label"><a href="https://www.douban.com/location/shenzhen/events/week-all">其他&raquo;</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-salon">讲座</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-exhibition">展览</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-sports">运动</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-travel">旅行</a></li>
    <li><a href="https://www.douban.com/location/shenzhen/events/week-commonweal">公益</a></li>
  </ul>
</div>
</div>
</div>
  <div class="main">


    <h2>
        深圳 · 本周热门活动
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                
                    <a href="https://www.douban.com/location/" target="_self">更多</a>
                ) </span>
    </h2>

<div class="events-list list">
  <ul>
    <li>
      <div class="pic">
        <a href="https://www.douban.com/event/30856440/">
            <img data-origin="https://img1.doubanio.com/pview/event_poster/small/public/ecab4412782309c.jpg" src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" width="70">
        </a>
      </div>
      <div class="info">
        <div class="title">
          <a href="https://www.douban.com/event/30856440/" title="2018谢春花“点心”全国巡回演唱会—深圳站">
            2018谢春花“点心”全国巡回演唱会—深圳站
          </a>
        </div>
        <div class="datetime">
            8月19日 周日 19:30 - 22:00
        </div>
        <address title="后海滨路3013号保利剧院（保利文化广场D区）">
          后海滨路3013号保利剧院（...
        </address>
        <div class="follow">
          116人关注
        </div>
      </div>
    <li>
      <div class="pic">
        <a href="https://www.douban.com/event/30524746/">
            <img data-origin="https://img3.doubanio.com/pview/event_poster/small/public/101f9952f6d6cf4.jpg" src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" width="70">
        </a>
      </div>
      <div class="info">
        <div class="title">
          <a href="https://www.douban.com/event/30524746/" title="【万有音乐系】大塚爱2018亚洲巡演 AIO PIANO at ASIA-深圳站">
            【万有音乐系】大塚爱2018亚洲巡演 AIO PIANO at ASIA...
          </a>
        </div>
        <div class="datetime">
            8月17日 周五 20:00 - 21:30
        </div>
        <address title="南山文体中心剧院 大剧院 南山大道与南头街交汇处南山文体中心">
          南山文体中心剧院 大剧院 ...
        </address>
        <div class="follow">
          55人关注
        </div>
      </div>
    <li>
      <div class="pic">
        <a href="https://www.douban.com/event/30726741/">
            <img data-origin="https://img3.doubanio.com/pview/event_poster/small/public/1b0ecde55d9e0d1.jpg" src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" width="70">
        </a>
      </div>
      <div class="info">
        <div class="title">
          <a href="https://www.douban.com/event/30726741/" title="2018蔡琴风华绝代深圳站演唱会">
            2018蔡琴风华绝代深圳站演唱会
          </a>
        </div>
        <div class="datetime">
            8月18日 周六 19:30 - 22:00
        </div>
        <address title="深圳湾体育中心春茧体育馆">
          深圳湾体育中心春茧体育馆
        </address>
        <div class="follow">
          38人关注
        </div>
      </div>
    <li>
      <div class="pic">
        <a href="https://www.douban.com/event/30736906/">
            <img data-origin="https://img1.doubanio.com/pview/event_poster/small/public/2818326c295c617.jpg" src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" width="70">
        </a>
      </div>
      <div class="info">
        <div class="title">
          <a href="https://www.douban.com/event/30736906/" title="直到世界尽头——8090经典动漫演唱会">
            直到世界尽头——8090经典动漫演唱会
          </a>
        </div>
        <div class="datetime">
            9月8日 周六 19:30 - 21:30
        </div>
        <address title="深圳市南山区A8音乐大厦二层A8Live 科园路一号">
          深圳市南山区A8音乐大厦二...
        </address>
        <div class="follow">
          28人关注
        </div>
      </div>
  </ul>
</div>
</div>
  </div>
  
</div>









<div class="wrapper">
  <div id="dale_anonymous_home_page_bottom" class="extra"></div>
  <div id="ft">
  
  
<span id="icp" class="fleft gray-link">
    &copy; 2005－2018 douban.com, all rights reserved 北京豆网科技有限公司
  <br>
  <a href="http://www.miibeian.gov.cn/">京ICP证090015号</a> 京ICP备11027288号 网络视听许可证<a href="https://www.douban.com/about?topic=licence" target="_blank">0110418</a>号
  <br>京网文[2015]2026-368号 <img src="https://img3.doubanio.com/pics/biaoshi.gif" align="absmiddle"> <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502000728">京公网安备11010502000728</a>&nbsp;&nbsp;新出网证(京)字129号
  <br>违法和不良信息举报电话：4008353331-9&nbsp;<img src="https://img3.doubanio.com/img/files/file-1423193113.png" height="16" align="top"/>
  <br><img src="https://img3.doubanio.com/pics/icon/jubao.png" align="absmiddle" width="15px"> <a href="http://www.12377.cn/">中国互联网举报中心</a> 电话：12377 <a href="https://img1.doubanio.com/img/files/file-1478594087.jpg">《食品流通许可证》许可证：SP1101051510347287</a>
  <br><a href="https://img3.doubanio.com/img/files/file-1495708840.jpg">新出发京批字第直160029号</a>
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>
    
    · <a href="https://help.douban.com/?app=main" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
    <a href="http://report.12377.cn:13225/toreportinputNormal_anis.do" target="_blank" style="display: block; margin-top: 20px; width: 150px">
      <img src="https://img3.doubanio.com/img/files/file-1489464722.jpg" alt="网上有害信息举报专区">
    </a>
</span>

  </div>
</div>






<script src="https://img3.doubanio.com/f/shire/4b1bbfaa49f8fb30d2719ec0ec08a11f24412ff5/js/core/do/_init_.js" data-cfg-corelib="https://img3.doubanio.com/f/shire/72ced6df41d4d158420cebdd254f9562942464e3/js/jquery.min.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/73b005363d0908b7.js"></script>

    <!-- douban ad begin -->
    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = 'gpsCrpiYmas',
            criteria = '3:/',
            preview = '',
            debug = false,
            adSlots = ['dale_anonymous_homepage_top_for_crazy_ad', 'dale_anonymous_homepage_right_top', 'dale_anonymous_homepage_movie_bottom', 'dale_anonymous_home_page_top', 'dale_homepage_online_activity_promo_1', 'dale_anonymous_homepage_doublemint', 'dale_anonymous_home_page_middle', 'dale_anonymous_home_page_middle_2', 'dale_anonymous_home_page_bottom'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/cdc904d1376a43e44bbf399a0aff51973016cd77/ad.release.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>










    <!-- douban ad end -->
    









<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5WP579" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-5WP579');</script>
<!-- End Google Tag Manager -->


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
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-7019765-1']);
_gaq.push(['_setCampNameKey', 'dcn']);
_gaq.push(['_setCampSourceKey', 'dcs']);
_gaq.push(['_setCampMediumKey', 'dcm']);
_gaq.push(['_setCampTermKey', 'dct']);
_gaq.push(['_setCampContentKey', 'dcc']);
_gaq.push(['_addOrganic', 'baidu', 'word']);
_gaq.push(['_addOrganic', 'soso', 'w']);
_gaq.push(['_addOrganic', '3721', 'name']);
_gaq.push(['_addOrganic', 'youdao', 'q']);
_gaq.push(['_addOrganic', 'so.360.cn', 'q']);
_gaq.push(['_addOrganic', 'vnet', 'kw']);
_gaq.push(['_addOrganic', 'sogou', 'query']);
_gaq.push(['_addIgnoredOrganic', '豆瓣']);
_gaq.push(['_addIgnoredOrganic', 'douban']);
_gaq.push(['_addIgnoredOrganic', '豆瓣网']);
_gaq.push(['_addIgnoredOrganic', 'www.douban.com']);
_gaq.push(['_setDomainName', '.douban.com']);


    _gaq.push(['_setCustomVar', 1, 'responsive_view_mode', 'desktop', 3]);

_gaq.push(['_trackPageview']);
_gaq.push(['_trackPageLoadTime']);

window._ga_init = function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
};
if (window.addEventListener) {
    window.addEventListener('load', _ga_init, false);
} else {
    window.attachEvent('onload', _ga_init);
}
</script>






</body>
</html>


"""
# src = get_img_src_from_html(html1)
# print(src)

img_url = "https://upload-images.jianshu.io/upload_images/4131789-a485e499d0427baf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700"
file_name = "test.jpg"
file_path = "/spider/img"
save_img(img_url,file_name,file_path)