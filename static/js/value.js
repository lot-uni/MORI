// 現在のURLを取得
var currentURL = window.location.href;

// URLを解析し、クエリーパラメータを取得
var url = new URL(currentURL);
var face = url.searchParams.get("face");
// URLを解析し、クエリーパラメータを取得
var url = new URL(currentURL);
console.log(location.protocol+"//"+location.host+"/dele/"+face);
