/**************************************************
 * MKOnlinePlayer v2.4
 * Ajax 后台数据交互请求模块
 * 编写：mengkun(https://mkblog.cn)
 * 时间：2018-3-11
 *************************************************/

// ajax加载搜索结果
function ajaxSearch() {
    if(rem.wd === ""){
        layer.msg('搜索内容不能为空', {anim:6});
        return false;
    }
    
    if(rem.loadPage == 1) { // 弹出搜索提示
        var tmpLoading = layer.msg('搜索中', {icon: 16,shade: 0.01});
    }
    
    $.ajax({
        type: mkPlayer.method, 
        url: mkPlayer.api, 
        data: "types=search&count=" + mkPlayer.loadcount + "&source=" + rem.source + "&pages=" + rem.loadPage + "&name=" + rem.wd,
        dataType : "jsonp",
        complete: function(XMLHttpRequest, textStatus) {
            if(tmpLoading) layer.close(tmpLoading);    // 关闭加载中动画
        },  // complete
        success: function(jsonData){
            
            // 调试信息输出
            if(mkPlayer.debug) {
                console.debug("搜索结果数：" + jsonData.length);
            }
            
            if(rem.loadPage == 1)   // 加载第一页，清空列表
            {
                if(jsonData.length === 0)   // 返回结果为零
                {
                    layer.msg('没有找到相关歌曲', {anim:6});
                    return false;
                }
                musicList[0].item = [];
                rem.mainList.html('');   // 清空列表中原有的元素
                addListhead();      // 加载列表头
            } else {
                $("#list-foot").remove();     //已经是加载后面的页码了，删除之前的“加载更多”提示
            }
            
            if(jsonData.length === 0)
            {
                addListbar("nomore");  // 加载完了
                return false;
            }
            
            var tempItem = [], no = musicList[0].item.length;
            
            for (var i = 0; i < jsonData.length; i++) {
                no ++;
                tempItem =  {
                    id: jsonData[i].id,  // 音乐ID
                    name: jsonData[i].name,  // 音乐名字
                    artist: jsonData[i].artist[0], // 艺术家名字
                    album: jsonData[i].album,    // 专辑名字
                    source: jsonData[i].source,     // 音乐来源
                    url_id: jsonData[i].url_id,  // 链接ID
                    pic_id: jsonData[i].pic_id,  // 封面ID
                    lyric_id: jsonData[i].lyric_id,  // 歌词ID
                    pic: null,    // 专辑图片
                    url: null   // mp3链接
                };
                musicList[0].item.push(tempItem);   // 保存到搜索结果临时列表中
                addItem(no, tempItem.name, tempItem.artist, tempItem.album);  // 在前端显示
            }
            
            rem.dislist = 0;    // 当前显示的是搜索列表
            rem.loadPage ++;    // 已加载的列数+1
            
            dataBox("list");    // 在主界面显示出播放列表
            refreshList();  // 刷新列表，添加正在播放样式
            
            if(no < mkPlayer.loadcount) {
                addListbar("nomore");  // 没加载满，说明已经加载完了
            } else {
                addListbar("more");     // 还可以点击加载更多
            }
            
            if(rem.loadPage == 2) listToTop();    // 播放列表滚动到顶部
        },   //success
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            layer.msg('搜索结果获取失败 - ' + XMLHttpRequest.status);
            console.error(XMLHttpRequest + textStatus + errorThrown);
        }   // error
    });//ajax
}






