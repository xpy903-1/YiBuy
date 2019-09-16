/*
* 购物车的功能脚本
* */
var cartData = null; // 已经加载的数据
var totalPrice = 0; // 总金额
$(ev=>{
    // 文档加载就绪 $(document).ready(ev=>{})

    $.ajax('carts.json',{ // a：资源  b：参数
        type: "get",
        dataType: 'json',
        success: function (data) {
            // data 是 json 对象类型
            cartData = data;

            $('.user_name').text(data.user.name);
            // each 迭代函数
            $.each(data.cart, (i, item)=>{
                // 计算总金额 = 数量 X 金额
                totalPrice += item.goods.price*item.cnt;

                let tr = '<tr>';
                tr += "<td><input type='checkbox' id='goods_"+item.goods.id+"'></td>";
                tr += "<td>"+item.goods.name+"</td>";
                tr += "<td>"+item.goods.price+"</td>";

                let cnt_str=
                    '<span class="btn sub">-</span>'+
                    '<input name="cnt" size="3" value="'+item.cnt+'">'+
                    '<span class="btn add">+</span>';

                tr += "<td>"+cnt_str+"</td>"
                    +"<td><span class='btn del' index='"+ i +"'>X</span></td>"
                    + "</tr>";

                $('tbody').append(tr)
            });
            $('.totalPrice').text(totalPrice);

            init_even()
        }
    })
});
function init_even() {
    // 初始化事件
    // 减号的标签点击事件
    $('.sub').click(ev=>{
       let sub_e = ev.target;
       //获取到它的下一个兄弟节点
       let cntObj = $(sub_e).next();
       // 取出cntObj的数值
       if(cntObj.val() <= 1){
           alert("至少购买一件");
           return;
       }
        cntObj.val(cntObj.val()-1);
        cntChange(cntObj[0].index,cntObj.val())
    });
    $('.add').click(ev=>{
        // 获取上一个兄弟标签
        let cntObj = $(ev.target).prev();
        if(cntObj.val() >= 20){
            return
        }
         cntObj.val(parseInt(cntObj.val()) +1);
        cntChange(cntObj[0].index,cntObj.val())
    });
    // 设置数量变化的监听
    $(":text[name='cnt']").each((i,element)=>{
        console.log(i,element);
        element.index = i;
        //设置数据发生变化的事件
        $(element).on('input',ev=>{
            if(ev.target.value <= 0)
                ev.target.value = 1;
            if(ev.target.value > 20)
                ev.target.value = 20;
            cntChange(ev.target.index,ev.target.value)
        });
    });

    // 设置删除事件
    $('.del').click(ev=>{
        // 读取自定义的标签属性
        console.log($(ev.target).attr('index'));
        let index = parseInt($(ev.target).attr('index'));

        // 删除数据
        delete cartData.cart[index];
        // 删除 UI
        $(ev.target).parent().parent().remove();
        // 刷新总价格
        refreshTotal();
    });

    //设置全选事件监听
    //设置每个商品胡勾选时间监听
    $('.checkbox').change(ev =>{
        // 获取checkbox的勾选状态checked：
        // true 勾选 false 非勾选
        // 判断是否为全选checkbox
        let checked = ev.target.checked;
        console.log(checked,ev.target.name);
        let goods_id = ev.target.id;
        if(ev.target.name ==="checkAll"){
            // 全选标签
            if(checked){
                $(':checkbox[id]').each((i,element)=> {
                    element.checked = true
                })
            }else {
                // 取消全选
                $(':checkbox[id]').each((i,element)=>{
                    element.checked = false
                })
            }
        }else {
                let isSelectAll = true;
                $('.checkbox[id]').each((i,element)=>{
                    if(!element.checked){
                        isSelectAll = false;
                    }
                });
                $('[name="checkAll"]')[0].checked=isSelectAll
            }
        }
    )
}

function cntChange(index,value) {
        index = parseInt(index);
        // 更新指定位置的商品的数量
        cartData.cart[index].cnt = parseInt(value);

        refreshTotal()
    }

// 改变数量改变金额
function refreshTotal(){
    totalPrice = 0;
        cartData.cart.forEach(item=>{
            totalPrice += item.goods.price * item.cnt;
        });
        $('.totalPrice').text(totalPrice)
}

