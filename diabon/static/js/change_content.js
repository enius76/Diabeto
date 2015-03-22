$(document).ready(function(){
    /*$("#catalogue-tri a.change_load").click(function(){
        //on recup l'url de la page dans une variable 'page'
        page=$(this).attr("href");
        $.ajax({
            url: page,
            cache:false,
            success:function(html){
                afficher_apropos(html);
            },
            error:function(XMLHttpRequest,textStatus,errorThrown){
                alert(textStatus);
            }
        })
        return false;
    });*/

    /*$("#articles-tri a.change_load").click(function(){
        //on recup l'url de la page dans une variable 'page'
        page=$(this).attr("href");
        $.ajax({
            url: page,
            cache:false,
            success:function(html){
                afficher_articles(html);
            },
            error:function(XMLHttpRequest,textStatus,errorThrown){
                alert(textStatus);
            }
        })

        //on change sa classe pour qu'il soit actif
        $(".change_load").removeClass('actif');
        $(this).addClass('actif');
        
        return false;
    });*/

    $("#releves-tri a.change_load").click(function(){
        //on recup l'url de la page dans une variable 'page'
        page=$(this).attr("href");
        $.ajax({
            url: page,
            cache:false,
            success:function(html){
                afficher_releves(html);
            },
            error:function(XMLHttpRequest,textStatus,errorThrown){
                alert(textStatus);
            }
        })

        //on change sa classe pour qu'il soit actif
        $(".change_load").removeClass('actif');
        $(this).addClass('actif');
        
        return false;
    });
}); 

function afficher_apropos(data){
    $(".tri-result").fadeOut(300,function(){
        $(".tri-result").empty();
        $(".tri-result").append(data);
        $(".tri-result").fadeIn(500);
    })
}

function afficher_articles(data){
    $(".conseils-articles").fadeOut(300,function(){
        $(".conseils-articles").empty();
        $(".conseils-articles").append(data);
        $(".conseils-articles").fadeIn(500);
    })
}

function afficher_releves(data){
    $("#table-releve-container").fadeOut(300,function(){
        $("#table-releve-container").empty();
        $("#table-releve-container").append(data);
        $("#table-releve-container").fadeIn(500);
    })
}