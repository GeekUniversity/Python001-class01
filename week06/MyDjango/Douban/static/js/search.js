	var obj = document.getElementById("search_btn");
	obj.addEventListener("click",function(){
	  var searchcontent=$("[id='content-search']").val();
	  if (searchcontent.length > 0){
          url = 'search'+'?keyw='+searchcontent;
          window.location.href=url;
	  }
	  else{
	    alert('请输入搜索内容！');
	  }
	},false);

