var express = require('express');
var config = require('../config');
var url=require('url');
var child_process=require('child_process');
var fs=require('fs');
var request=require('request');
var router = express.Router();


var blacklist=['127.0.0.1.xip.io','::ffff:127.0.0.1','127.0.0.1','0','localhost','0.0.0.0','[::1]','::1'];

router.get('/', function(req, res, next) {
    res.json({});
});

router.get('/debug', function(req, res, next) {
    console.log(req.ip);
    if(blacklist.indexOf(req.ip)!=-1){
        console.log('res');
	var u = req.query.url.replace(/[\"\']/ig,'');
	let log = `echo  '${url.parse(u).href}'>> /tmp/log`;
	child_process.exec(log);
	res.json({data:fs.readFileSync('/tmp/log').toString()});
    }else{
        res.json({});
    }
});


router.post('/debug', function(req, res, next) {
    console.log(req.body);
    if(req.body.url !== undefined) {
        var u = req.body.url;
	var urlObject=url.parse(u);
	if(blacklist.indexOf(urlObject.hostname) == -1){
		var dest=urlObject.href;
		request(dest,(err,result,body)=>{
			res.json(body);
		})
	}
	else{
		res.json([]);
	}
	}
});

module.exports = router;
