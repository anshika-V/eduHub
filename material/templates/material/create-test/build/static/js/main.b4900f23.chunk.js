(this["webpackJsonpcreate-test"]=this["webpackJsonpcreate-test"]||[]).push([[0],{11:function(e,t,a){e.exports={dot1:"SocketStatus_dot1__2gVtp",dot1Anim:"SocketStatus_dot1Anim__2GG5M",dot2:"SocketStatus_dot2__2ZiMM",dot2Anim:"SocketStatus_dot2Anim__2b30V",dot3:"SocketStatus_dot3__2aMyN",dot3Anim:"SocketStatus_dot3Anim__3SIAx",status:"SocketStatus_status__LHVNz"}},16:function(e,t,a){e.exports={sidebarMain:"Sidebar_sidebarMain__3xpJL",sideHead:"Sidebar_sideHead__3_rEt",addBtn:"Sidebar_addBtn__17vBb"}},17:function(e,t,a){e.exports={qBtnsCont:"QuestionsBtns_qBtnsCont__r19tx",btns:"QuestionsBtns_btns__3JyHc"}},2:function(e,t,a){e.exports={questionMain:"Question_questionMain__1_rxd",qno:"Question_qno__WrjZj",qtext:"Question_qtext__Z1Mmf",rightpannel:"Question_rightpannel__2UY0F",marksinp:"Question_marksinp__2Uhvn",choicesCont:"Question_choicesCont__wBpp9",choices:"Question_choices__lz6pm",choicesLabel:"Question_choicesLabel__1Ls73",ansInp:"Question_ansInp__egB3m",desc:"Question_desc__2_tAt"}},24:function(e,t,a){e.exports={notifBtn:"Notification_notifBtn__U2Qxp"}},25:function(e,t,a){e.exports={main:"Main_main__1oWsp"}},27:function(e,t,a){e.exports=a(41)},31:function(e,t,a){},41:function(e,t,a){"use strict";a.r(t);var n=a(0),s=a.n(n),i=a(12),r=a.n(i),o=(a(31),a(9)),c=a.n(o);var l=function(e){return s.a.createElement("div",{className:"ml-4 pl-4",id:c.a.navCont},s.a.createElement("a",{href:"/",className:[c.a.navLink,"ml-4 mr-4"].join(" ")},"Home"),s.a.createElement("a",{href:"#",className:[c.a.navLink,"ml-4 mr-4"].join(" "),style:{opacity:"30%"}},"Blog"),s.a.createElement("a",{href:"#",className:[c.a.navLink,"ml-4 mr-4"].join(" "),style:{opacity:"30%"}},"Contact"))},u=a(26),p=a(8),d=a.n(p),m=a(1);var f=Object(m.b)((function(e){return{profile:e.Profile}}))((function(e){var t=Object(n.useState)("none"),a=Object(u.a)(t,2),i=a[0],r=a[1];return s.a.createElement("div",{className:"ml-2",id:d.a.userBtnCont},s.a.createElement("button",{className:"p-0",id:d.a.userBtn,onClick:function(e){return r("block"===i?"none":"block")},onBlur:function(e){return setTimeout(r,10,"none")}},s.a.createElement("img",{src:void 0!==e.profile.name?window.media_url+e.profile.fields.profile_pic:"",id:d.a.userBtnImg,alt:""})),s.a.createElement("div",{onClick:function(e){return setTimeout(r,20,"block")},id:d.a.userPannel,className:"p-2 pr-3 bg-white",style:{display:i}},void 0!==e.profile.name?s.a.createElement(s.a.Fragment,null,s.a.createElement("span",{className:d.a.userData},e.profile.username),s.a.createElement("span",{className:[d.a.userData,"text-secondary"].join(" ")},e.profile.email)):"",s.a.createElement("hr",{className:"m-0 mt-1"}),s.a.createElement("a",{href:"#",className:[d.a.navLink,d.a.userPannelLink,"pb-0 mt-2 mb-1 mr-2 ml-1"].join(" "),style:{opacity:"30%"}},"Profile"),s.a.createElement("a",{href:window.base+"/user/logout/",className:[d.a.navLink,d.a.userPannelLink,"pb-0 mb-0 mr-2 ml-1"].join(" ")},"Logout")))})),v=a(24),h=a.n(v);var b=function(e){return s.a.createElement("div",{className:"ml-auto mr-4",style:{opacity:"30%"}},s.a.createElement("button",{className:"material-icons  btn",id:h.a.notifBtn},"notifications"))},y=a(11),g=a.n(y);var k=Object(m.b)((function(e){return{socketStatus:e.SocketState.status}}))((function(e){var t="default";switch(e.socketStatus){case"connecting":case"saving":case"reconnecting":t=s.a.createElement("h6",{className:"text-muted mb-0 pb-0",id:g.a.status},e.socketStatus,s.a.createElement("span",{id:g.a.dot1},"."),s.a.createElement("span",{id:g.a.dot2},"."),s.a.createElement("span",{id:g.a.dot3},"."));break;case"saved":t=s.a.createElement("h6",{className:"text-muted",id:g.a.status},"All previous changes saved");break;case"connected":t=s.a.createElement("h6",{className:"text-muted",id:g.a.status},"Connected")}return s.a.createElement("div",{className:"ml-4 pb-0 mt-4"},t)}));var w=Object(m.b)(null,(function(e){return{updateProfile:function(t){return e(function(e){return{type:"updateProfile",payload:e}}(t))}}}))((function(e){return Object(n.useEffect)((function(){fetch(window.base+"/user/api/profile/",{credentials:window.cred}).then((function(e){return e.json()})).then((function(t){return e.updateProfile(t)}))}),[e]),s.a.createElement("div",{id:c.a.topBar,className:"d-flex flex-row align-items-center col-12 pl-2  text-light"},s.a.createElement("h1",{className:"display-3 ml-2 text-dark",id:c.a.edu,onClick:function(){return window.location.assign("/")}},s.a.createElement("span",null,"eduHub")),s.a.createElement(l,null),s.a.createElement(k,null),s.a.createElement(b,null),s.a.createElement(f,null))})),E=a(3),_=a(4),j=a(6),q=a(5),N=a(25),x=a.n(N),O=a(16),C=a.n(O),S=a(2),T=a.n(S),B=a(14),A=a(7),D=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case"updateProfile":e=Object(A.a)({},t.payload)}return e},M=a(10),Q=(a(38),function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{active:-1,questions:[],fields:{},changed:0},t=arguments.length>1?arguments[1]:void 0;switch(e=Object(A.a)({},e),t.type){case"updateTestData":e=Object(A.a)({},t.payload);break;case"newQuestion":e.questions=[].concat(Object(M.a)(e.questions),[{pk:null,fields:{parent_test:e.pk,text:"",type:"",image:"",marks:0,answer:"",jsonChoices:""}}]),-1!==e.active?e.questions[e.active].changed=0:-1===e.active&&(e.changed=0),e.active=e.questions.length-1;break;case"updatePk":console.log(t),e.questions[t.payload.index].pk=t.payload.pk,e.questions[t.payload.index]=Object(A.a)({},e.questions[t.payload.index]),console.log(e.questions[t.payload.index]);break;case"updateActive":-1!==e.active?e.questions[e.active].changed=0:-1===e.active&&(e.changed=0),e.active=t.payload;break;case"updateTestTitle":e.fields.title=t.payload,e.changed=1;break;case"updateTestDescription":e.fields.description=t.payload,e.changed=1;break;case"updateTestAccess":e.fields.access=t.payload,e.changed=1;break;case"updateTestAccessKey":e.fields.accessKey=t.payload,e.changed=1;break;case"updateTestDuration":e.fields.duration=t.payload,e.changed=1;break;case"updateActiveQuestionText":e.questions[e.active].fields.text=t.payload,e.questions[e.active].changed=1,e.questions[e.active]=Object(A.a)({},e.questions[e.active]);break;case"updateActiveAnswer":e.questions[e.active].fields.answer=t.payload,e.questions[e.active].changed=1,e.questions[e.active]=Object(A.a)({},e.questions[e.active]);break;case"updateActiveMarks":e.questions[e.active].fields.marks=t.payload,e.questions[e.active].changed=1,e.questions[e.active]=Object(A.a)({},e.questions[e.active]);break;case"updateActiveQuestionType":e.questions[e.active].fields.type=t.payload,e.questions[e.active].changed=1,"O"==t.payload||"M"==t.payload?e.questions[e.active].fields.answer="0000":e.questions[e.active].fields.answer="",e.questions[e.active]=Object(A.a)({},e.questions[e.active]);break;case"updateActiveChoices":var a=e.questions[e.active].fields.jsonChoices;(a=""===a?[]:JSON.parse(a))[t.payload.cindex-1]=t.payload.cdata,e.questions[e.active].fields.jsonChoices=JSON.stringify(a),e.questions[e.active].changed=1,e.questions[e.active]=Object(A.a)({},e.questions[e.active]);break;case"imageUploaded":e.questions[t.payload.index].fields.image=t.payload.image,e.questions[t.payload.index]=Object(A.a)({},e.questions[t.payload.index])}return e}),L=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{socket:null,status:"connecting",buffer:[],dataBuffer:[],isready:0},t=arguments.length>1?arguments[1]:void 0;switch(e=Object(A.a)({},e),t.type){case"setSocket":e.socket=t.payload;break;case"connected":e.status="connected",e.isready=1;break;case"disconnected":e.status="reconnecting",e.isready=0;break;case"addToBuffer":e.buffer=[].concat(Object(M.a)(e.buffer),[t.payload]);break;case"sendingData":e.isready=0,e.status="saving";break;case"savedData":e.buffer.shift(),e.buffer=Object(M.a)(e.buffer),0===e.buffer.length&&0===e.dataBuffer.length&&(e.status="saved"),e.isready=1;break;case"dataBufferShift":e.dataBuffer.shift(),e.dataBuffer=Object(M.a)(e.dataBuffer),e.isready=1,0===e.buffer.length&&0===e.dataBuffer.length&&(e.status="saved");break;case"addToDataBuffer":e.dataBuffer=[].concat(Object(M.a)(e.dataBuffer),[t.payload])}return e},U=Object(B.c)(Object(B.b)({Profile:D,Test:Q,SocketState:L}),{});function I(e){return{type:"addToDataBuffer",payload:e}}function P(){var e=U.getState().Test;if(-1===e.active||1!==e.questions[e.active].changed){if(-1===e.active&&1===e.changed){var t={type:"testUpdate",payload:e.fields};t=JSON.stringify(t),U.dispatch(I(t))}}else U.dispatch({type:"addToBuffer",payload:e.active})}function F(e){return P(),{type:"updateActive",payload:e}}function H(e){return{type:"updateActiveAnswer",payload:e}}function J(e,t){return{type:"imageUploaded",payload:{index:e,image:t}}}var W=function(e){Object(j.a)(a,e);var t=Object(q.a)(a);function a(){var e;Object(E.a)(this,a);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(e=t.call.apply(t,[this].concat(s))).answerHandler=function(t,a){var n=e.props.question.fields.answer;if(n=(n=n.split("")).map((function(e){return parseInt(e)})),"O"===e.props.question.fields.type)switch(a){case 1:n=[1,0,0,0];break;case 2:n=[0,1,0,0];break;case 3:n=[0,0,1,0];break;case 4:n=[0,0,0,1]}else n[a-1]=(n[a-1]+1)%2;e.props.updateAnswer(n.join(""))},e}return Object(_.a)(a,[{key:"render",value:function(){var e=this;return s.a.createElement(s.a.Fragment,null,s.a.createElement("div",{className:["p-0 d-flex w-100",T.a.choicesCont].join(" ")},s.a.createElement("div",{className:["p-0 d-flex w-100 align-items-baseline",T.a.choicesCont].join(" ")},s.a.createElement("div",{className:"d-flex flex-row align-items-baseline ml-4"},s.a.createElement("input",{type:"radio",onClick:function(t){return e.answerHandler(t,1)},checked:"1"===this.props.question.fields.answer[0]}),s.a.createElement("label",{className:["ml-1",T.a.choicesLabel].join(" ")},"Choice 1:")),s.a.createElement("input",{type:"text",className:["form-control m-4",T.a.choices].join(" "),value:void 0!==this.props.choices[0]?this.props.choices[0]:"",onChange:function(t){return e.props.updateChoice(1,t.target.value)}})),s.a.createElement("div",{className:["p-0 d-flex w-100 align-items-baseline",T.a.choicesCont].join(" ")},s.a.createElement("div",{className:"d-flex flex-row align-items-baseline ml-4"},s.a.createElement("input",{type:"radio",onClick:function(t){return e.answerHandler(t,2)},checked:"1"===this.props.question.fields.answer[1]}),s.a.createElement("label",{className:["ml-1",T.a.choicesLabel].join(" ")},"Choice 2:")),s.a.createElement("input",{type:"text",className:["m-4 form-control",T.a.choices].join(" "),value:void 0!==this.props.choices[1]?this.props.choices[1]:"",onChange:function(t){return e.props.updateChoice(2,t.target.value)}}))),s.a.createElement("div",{className:["p-0 d-flex w-100",T.a.choicesCont].join(" ")},s.a.createElement("div",{className:["p-0 d-flex w-100 align-items-baseline",T.a.choicesCont].join(" ")},s.a.createElement("div",{className:"d-flex flex-row align-items-baseline ml-4"},s.a.createElement("input",{type:"radio",onClick:function(t){return e.answerHandler(t,3)},checked:"1"===this.props.question.fields.answer[2]}),s.a.createElement("label",{className:["ml-1",T.a.choicesLabel].join(" ")},"Choice 3:")),s.a.createElement("input",{type:"text",className:["form-control m-4",T.a.choices].join(" "),value:void 0!==this.props.choices[2]?this.props.choices[2]:"",onChange:function(t){return e.props.updateChoice(3,t.target.value)}})),s.a.createElement("div",{className:["p-0 d-flex w-100 align-items-baseline",T.a.choicesCont].join(" ")},s.a.createElement("div",{className:"d-flex flex-row align-items-baseline ml-4"},s.a.createElement("input",{type:"radio",onClick:function(t){return e.answerHandler(t,4)},checked:"1"===this.props.question.fields.answer[3]}),s.a.createElement("label",{className:["ml-1",T.a.choicesLabel].join(" ")},"Choice 4:")),s.a.createElement("input",{type:"text",className:["form-control m-4",T.a.choices].join(" "),value:void 0!==this.props.choices[3]?this.props.choices[3]:"",onChange:function(t){return e.props.updateChoice(4,t.target.value)}}))),s.a.createElement("span",{className:"text-muted ml-4"},"Sellect correct answer/answers."))}}]),a}(n.Component),z=Object(m.b)((function(e){return{active:e.Test.active,choices:""!==e.Test.questions[e.Test.active].fields.jsonChoices?JSON.parse(e.Test.questions[e.Test.active].fields.jsonChoices):[],question:e.Test.questions[e.Test.active]}}),(function(e){return{updateChoice:function(t,a){return e(function(e,t){return{type:"updateActiveChoices",payload:{cindex:e,cdata:t}}}(t,a))},updateAnswer:function(t){return e(H(t))}}}))(W);var K=Object(m.b)((function(e){return{active:e.Test.active,question:e.Test.questions[e.Test.active]}}),(function(e){return{addToDataBuffer:function(t){return e(I(t))},putSpinner:function(t){return e(J(t,"spinner-border"))}}}))((function(e){return s.a.createElement(s.a.Fragment,null,s.a.createElement("input",{className:"ml-4 pl-4 mt-4",type:"file",accept:"image/*",name:"image",onChange:function(t){var a=t.target.files[0],n=new FileReader;n.onload=function(t){var n=t.target.result,s=new Uint8Array(n),i=Array.from(s),r={type:"imageUpload",payload:{key:e.question.pk,name:a.name,image:i,index:e.active}};r=JSON.stringify(r),e.addToDataBuffer(r),e.putSpinner(e.active)},n.readAsArrayBuffer(a)}}),s.a.createElement("div",{className:e.question.fields.image,role:"status",style:{display:"spinner-border"===e.question.fields.image?"":"none"}}),s.a.createElement("img",{className:["m-2 ml-4 pl-4 w-50"].join(" "),alt:"not found",style:{display:""===e.question.fields.image||"spinner-border"===e.question.fields.image?"none":"inline-block"},src:""===e.question.fields.image||"spinner-border"===e.question.fields.image?"#":window.media_url+e.question.fields.image}))})),Z=function(e){Object(j.a)(a,e);var t=Object(q.a)(a);function a(){return Object(E.a)(this,a),t.apply(this,arguments)}return Object(_.a)(a,[{key:"render",value:function(){var e=this,t=0;return this.props.questions.forEach((function(e){t+=e.fields.marks})),s.a.createElement("div",{className:"p-4"},s.a.createElement("label",null,"Test Title:"),s.a.createElement("input",{type:"text",className:"form-control ",value:this.props.test.fields.title,onChange:function(t){return e.props.updateTitle(t.target.value)}}),s.a.createElement("div",{class:"custom-control custom-switch mt-2 d-flex flex-row align-items-center"},s.a.createElement("input",{type:"checkbox",class:"custom-control-input",id:"switch",checked:-1!==this.props.test.fields.duration,onChange:function(t){return-1!==e.props.test.fields.duration?e.props.newDuration(-1):e.props.newDuration(10)}}),s.a.createElement("label",{class:"custom-control-label",for:"switch"},"Duration(minutes):"),s.a.createElement("input",{type:"number",className:"form-control w-25 d-inline ml-2",value:-1===this.props.test.fields.duration?"":this.props.test.fields.duration,onChange:function(t){return e.props.newDuration(""==t.target.value?-1:parseInt(t.target.value))}})),s.a.createElement("label",{className:"mt-3"},"Description:"),s.a.createElement("textarea",{className:"form-control mb-4",id:T.a.desc,rows:"15",value:this.props.test.fields.description,onChange:function(t){return e.props.updateDescription(t.target.value)}}),s.a.createElement("div",{class:"custom-control custom-switch mt-2 d-flex flex-row align-items-center"},s.a.createElement("input",{type:"checkbox",class:"custom-control-input",id:"switch2",checked:1===this.props.test.fields.access,onClick:function(t){return e.props.newAccess((e.props.test.fields.access+1)%2)}}),s.a.createElement("label",{class:"custom-control-label",for:"switch2"},"private")),s.a.createElement("div",{style:{display:1===this.props.test.fields.access?"block":"none"}},s.a.createElement("label",{styles:{display:"block"}},"Access Key:"),s.a.createElement("input",{type:"text",className:"form-control w-25 d-inline ml-2",value:this.props.test.fields.accessKey,onChange:function(t){return e.props.newAccessKey(t.target.value)}})),s.a.createElement("div",{className:"mt-4"},s.a.createElement("label",null,"Link:"),s.a.createElement("input",{className:"ml-2 form-control w-50 d-inline",value:window.location.origin+"/material/student-test/"+this.props.test.pk}),s.a.createElement("button",{className:"material-icons ml-2 p-0 btn btn-light",onClick:function(e){var t=e.target.previousSibling;t.select(),t.setSelectionRange(0,99999),document.execCommand("copy")}},"file_copy"),s.a.createElement("label",{className:"d-block"},"Share this link with the students")),s.a.createElement("div",{className:"float-right mt-2"},s.a.createElement("label",null,"No. of Questions: ",this.props.questions.length),s.a.createElement("br",null),s.a.createElement("label",null,"Marks: ",t)))}}]),a}(n.Component),V=Object(m.b)((function(e){return{test:e.Test,questions:e.Test.questions}}),(function(e){return{updateTitle:function(t){return e(function(e){return{type:"updateTestTitle",payload:e}}(t))},updateDescription:function(t){return e(function(e){return{type:"updateTestDescription",payload:e}}(t))},newDuration:function(t){return e({type:"updateTestDuration",payload:t})},newAccess:function(t){return e({type:"updateTestAccess",payload:t})},newAccessKey:function(t){return e({type:"updateTestAccessKey",payload:t})}}}))(Z),G=function(e){Object(j.a)(a,e);var t=Object(q.a)(a);function a(){return Object(E.a)(this,a),t.apply(this,arguments)}return Object(_.a)(a,[{key:"render",value:function(){var e=this;return s.a.createElement("div",{id:T.a.questionMain,className:"p-1 ml-2 flex-grow-1 mr-1 bg-light pr-4"},void 0===this.props.question||-1===this.props.active?s.a.createElement(V,null):s.a.createElement(s.a.Fragment,null,s.a.createElement("div",{className:"d-flex flex-row"},s.a.createElement("h1",{className:["ml-2 mt-4",T.a.qno].join(" ")},s.a.createElement("span",{className:"mr-4 mt-0 pt-0"},"Q.",this.props.active+1)),s.a.createElement("textarea",{className:["mt-4 form-control",T.a.qtext].join(" "),value:this.props.question.fields.text,onChange:function(t){return e.props.updateActiveQuestionText(t.target.value)},placeholder:"Write your question text here",cols:"80",rows:"6"})),s.a.createElement(K,null),s.a.createElement("br",null),"O"===this.props.question.fields.type||"M"===this.props.question.fields.type?s.a.createElement(z,null):"","F"==this.props.question.fields.type?s.a.createElement(s.a.Fragment,null,s.a.createElement("label",{className:"ml-4 pl-4 mt-4"},"Answer:"),s.a.createElement("input",{className:["ml-4 pl-4 form-control",T.a.ansInp].join(" "),style:{display:"inline"},type:"text",name:"answer",value:this.props.question.fields.answer,onChange:function(t){return e.props.updateAnswer(t.target.value)}})):"",s.a.createElement("div",{className:[T.a.rightpannel,"p-2 mt-4 pr-4"].join(" ")},s.a.createElement("label",null,"Marks:"),s.a.createElement("input",{className:["form-control ml-4",T.a.marksinp].join(" "),value:this.props.question.fields.marks,type:"number",onChange:function(t){return e.props.updateMarks(parseInt(t.target.value))}}),s.a.createElement("br",null),s.a.createElement("label",{className:"mt-4"},"Question Type:"),s.a.createElement("select",{className:"form-control",value:this.props.question.fields.type,onChange:function(t){return e.props.updateType(t.target.value)}},s.a.createElement("option",{value:""},"---------"),s.a.createElement("option",{value:"D"},"Descriptive"),s.a.createElement("option",{value:"O"},"One_Option_Correct"),s.a.createElement("option",{value:"M"},"Multu_Option_Correct"),s.a.createElement("option",{value:"F"},"Fill")))))}}]),a}(n.Component),R=Object(m.b)((function(e){return{ws:e.SocketState.socket,active:e.Test.active,question:e.Test.questions[e.Test.active],test:e.Test}}),(function(e){return{updateActiveQuestionText:function(t){return e(function(e){return{type:"updateActiveQuestionText",payload:e}}(t))},updateAnswer:function(t){return e(H(t))},updateMarks:function(t){return e(function(e){return{type:"updateActiveMarks",payload:e}}(t))},updateType:function(t){return e(function(e){return{type:"updateActiveQuestionType",payload:e}}(t))}}}))(G),Y=a(17),X=a.n(Y),$=function(e){Object(j.a)(a,e);var t=Object(q.a)(a);function a(){return Object(E.a)(this,a),t.apply(this,arguments)}return Object(_.a)(a,[{key:"render",value:function(){var e,t=this;return e=this.props.questions.map((function(e,a){return s.a.createElement("button",{className:["btn btn-dark m-2",X.a.btns].join(" "),key:a,onClick:function(){return t.props.updateActive(a)},disabled:a===t.props.active},a+1)})),s.a.createElement("div",{id:X.a.qBtnsCont}," ",s.a.createElement("button",{className:["btn btn-dark m-2 form-control w-25",X.a.btns].join(" "),onClick:function(){return t.props.updateActive(-1)},disabled:-1===this.props.active},"Test")," ",e)}}]),a}(n.Component),ee=Object(m.b)((function(e){return{active:e.Test.active,questions:e.Test.questions}}),(function(e){return{updateActive:function(t){return e(F(t))}}}))($),te=function(e){Object(j.a)(a,e);var t=Object(q.a)(a);function a(){return Object(E.a)(this,a),t.apply(this,arguments)}return Object(_.a)(a,[{key:"render",value:function(){return s.a.createElement(s.a.Fragment,null,s.a.createElement("div",{id:C.a.sidebarMain,className:"p-1 bg-secondary"},s.a.createElement("h1",{className:"display-4 bg-info text-light pl-2",id:C.a.sideHead},"Questions",s.a.createElement("button",{className:"material-icons p-0 btn btn-primary",id:C.a.addBtn,onClick:this.props.newQuestion},"add")),s.a.createElement(ee,null)),s.a.createElement(R,null))}}]),a}(n.Component),ae=Object(m.b)(null,(function(e){return{newQuestion:function(t){return e((P(),{type:"newQuestion"}))}}}))(te),ne=function(e){Object(j.a)(a,e);var t=Object(q.a)(a);function a(e){var n;return Object(E.a)(this,a),(n=t.call(this,e)).InitilizeBackend=function(){var e=ie(),t={type:"initilization",payload:e=parseInt(e)};n.ws.send(JSON.stringify(t))},n.NewWebSocket=function(){var e="wss://";"http:"==window.location.protocol&&(e="ws://"),n.ws=new WebSocket(e+window.hostName+"/ws/material/testMaker/"),n.ws.onopen=function(){n.props.setSocket(n.ws),n.InitilizeBackend()},n.ws.onmessage=function(e){var t=JSON.parse(e.data);switch(t.type){case"connected":n.props.socketConnected();break;case"saved":if(t.code="SNQ"){var a=U.getState().SocketState.buffer[0];console.log("index: ",a),U.dispatch(function(e,t){return{type:"updatePk",payload:{index:e,pk:t}}}(a,t.key))}n.props.saved();break;case"imageUploaded":n.props.dataBufferShift(),n.props.imageUploaded(t.index,t.image);break;case"dataUploaded":n.props.dataBufferShift();break;case"error":switch(t.code){case"NI":n.props.disconnected(),n.InitilizeBackend();break;default:n.props.disconnected(),n.ws.close()}}},n.ws.onclose=function(e){n.props.disconnected(),setTimeout(n.NewWebSocket,5e3)},n.ws.onerror=function(e){n.props.disconnected(),setTimeout(n.NewWebSocket,15e3)}},n.componentDidMount=function(){n.NewWebSocket()},n.BufferManager=function(){var e=U.getState().Test.questions;if(0!==n.props.isready){if(0!==n.props.buffer.length){var t={type:"questionUpdate",payload:e[n.props.buffer[0]]};return t=JSON.stringify(t),n.props.sendingData(),void n.ws.send(t)}if(0!==n.props.dataBuffer.length){var a=n.props.dataBuffer[0];n.props.sendingData(),n.ws.send(a)}}},n.ws=null,n}return Object(_.a)(a,[{key:"render",value:function(){var e=this;return this.BufferManager(),s.a.createElement(s.a.Fragment,null,s.a.createElement("button",{className:"float-right mr-4 mb-4 mt-1 btn btn-success",onClick:function(){e.props.updateActive(e.props.active)}},"save"))}}]),a}(n.Component),se=Object(m.b)((function(e){return{active:e.Test.active,dataBuffer:e.SocketState.dataBuffer,buffer:e.SocketState.buffer,isready:e.SocketState.isready}}),(function(e){return{setSocket:function(t){return e(function(e){return{type:"setSocket",payload:e}}(t))},socketConnected:function(){return e({type:"connected",payload:null})},sendingData:function(){return e({type:"sendingData",payload:null})},saved:function(){return e({type:"savedData",payload:null})},imageUploaded:function(t,a){return e(J(t,a))},dataBufferShift:function(){return e({type:"dataBufferShift",payload:null})},disconnected:function(){return e({type:"disconnected",payload:null})},updateActive:function(t){return e(F(t))}}}))(ne),ie=function(){var e=window.location.href,t=e.length,a=e.lastIndexOf("/");return a===t-1&&(a=(e=e.slice(0,-1)).lastIndexOf("/")),e.substring(a+1)},re=function(e){Object(j.a)(a,e);var t=Object(q.a)(a);function a(){var e;Object(E.a)(this,a);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(e=t.call.apply(t,[this].concat(s))).fetchData=function(t){fetch(window.base+"/material/api/test/data/"+t+"/",{credentials:window.cred}).then((function(e){return e.json()})).then((function(t){return e.props.updateTestData(t)})).catch((function(e){return alert("Error fetching data: possible reasons unauthorised access aur connection issue ")}))},e.componentDidMount=function(){var t=ie();e.fetchData(t)},e}return Object(_.a)(a,[{key:"render",value:function(){return s.a.createElement("div",{id:x.a.main,className:"p-1 d-flex pt-2"},s.a.createElement(ae,null))}}]),a}(n.Component),oe=Object(m.b)(null,(function(e){return{updateTestData:function(t){return e(function(e){var t=e.questions.map((function(e){return e.changed=0,e}));return e.questions=Object.assign([],t),e.active=-1,{type:"updateTestData",payload:e}}(t))}}}))(re);var ce=function(){return s.a.createElement(s.a.Fragment,null,s.a.createElement(w,null)," ",s.a.createElement(oe,null))};window.base="",window.hostName=window.location.host,window.media_url="https://eduhub.blob.core.windows.net/eduhub/",window.cred="same-origin",r.a.render(s.a.createElement(m.a,{store:U},s.a.createElement(ce,null),s.a.createElement(se,null)),document.getElementById("root"))},8:function(e,t,a){e.exports={navLink:"UserBtn_navLink__3C6qU",userBtn:"UserBtn_userBtn__2502Q",userBtnImg:"UserBtn_userBtnImg__1XDNf",userPannel:"UserBtn_userPannel__SYTvw",userPannelLink:"UserBtn_userPannelLink__squgZ",userData:"UserBtn_userData__ZFyrl",userBtnCont:"UserBtn_userBtnCont__1BfAU"}},9:function(e,t,a){e.exports={topBar:"Top_topBar__1M36g",navLink:"Top_navLink__31pSM",edu:"Top_edu__3lhuD",navCont:"Top_navCont__2D-Nz"}}},[[27,1,2]]]);
//# sourceMappingURL=main.b4900f23.chunk.js.map