
// The only dependency is r6api.js ~1.4.1

var mostrecent = 18 // adjust the variable to the most recent season
// 18 = steel wave, so 19 would be the season after steel wave, and so on so forth





const slowAndSteady = new Promise(function(resolve, reject) {
    throw new Error('Somethin just happen right now :(');


});



const fs = require('fs');
    

async function api_call(){
    promisecheck()
    
    try {
        // read contents of the file
        const data = fs.readFileSync('enter.txt', 'UTF-8');
    
        // split the contents by new line
        const lines = data.split(/\r?\n/);
    
        // print all lines'
        var profilename = lines[0]
        if (lines[1] == ' PC'){var platformon = 'uplay'}
        else if(lines[1] == ' Xbox'){var platformon = 'xbl'}
        else if(lines[1] == ' PSN'){var platformon = 'psn'};
        console.log(profilename, platformon)
        
    } catch (err) {
        console.error(err);
    };


    const R6API = require('r6api.js');
    const r6api = new R6API(EMAIL, PASSWORD); // put ur ubisoft login credentials here or create a dummy account from
                                                // https://temp-mail.org/en then copy ur email and go to https://account.ubisoft.com/en-GB/login to create a new account
                                                //and put ur credentials there
    var errormessage = 'error invalid username and or platform';
//huilrkga;lkj


        const username = profilename,
    platform = platformon; // Put a try and catch over here to filter out, invalid usernames. If it is an invalid username with that platform run a check for different platforms
                                //If those don't work then just return something to the data.txt, saying that it is invalid. And then that displays something on the GUI

    
    try{
        const id = await r6api.getId(platform, username).then(el => el[0].userId);
    }
    catch(err) {
        fs.writeFile('errlog.txt', errormessage, function (err) {
        if (err) return console.log(err);   //writing our stats to the txt file
        console.log(errormessage);
        fs.close()
        process.exit();
        });
        
    
    }
        
    const id = await r6api.getId(platform, username).then(el => el[0].userId);
    const stats = await r6api.getStats(platform, id).then(el => el[0]);
    const level = await r6api.getLevel(platform, id).then(el => el[0]);
    const timeplayed = await r6api.getPlaytime(platform, id).then(el => el[0]);
    const rank = await r6api.getRank(platform, id, {seasons: 'all'}).then(el => el[0]);
    if (rank.seasons[mostrecent].regions.ncsa.max.mmr >= rank.seasons[mostrecent].regions.emea.max.mmr && rank.seasons[mostrecent].regions.ncsa.max.mmr >= rank.seasons[mostrecent].regions.apac.max.mmr){
        var mmr_0 = rank.seasons[mostrecent-0].regions.ncsa.current.mmr;
        var mmr_1 = rank.seasons[mostrecent-1].regions.ncsa.max.mmr;
        var mmr_2 = rank.seasons[mostrecent-2].regions.ncsa.max.mmr;
        var mmr_3 = rank.seasons[mostrecent-3].regions.ncsa.max.mmr;
        var mmr_4 = rank.seasons[mostrecent-4].regions.ncsa.max.mmr;
        var mmr_5 = rank.seasons[mostrecent-5].regions.ncsa.max.mmr;
        var mmr_6 = rank.seasons[mostrecent-6].regions.ncsa.max.mmr; 
        var mmr_7 = rank.seasons[mostrecent-7].regions.ncsa.max.mmr;
        var mmr_8 = rank.seasons[mostrecent-8].regions.ncsa.max.mmr;
        var mmr_9 = rank.seasons[mostrecent-9].regions.ncsa.max.mmr;
        var mmr_10 = rank.seasons[mostrecent-10].regions.ncsa.max.mmr;
        var mmr_11 = rank.seasons[mostrecent-11].regions.ncsa.max.mmr;
        var name_0 = rank.seasons[mostrecent-0].regions.ncsa.current.name;
        var name_1 = rank.seasons[mostrecent-1].regions.ncsa.max.name;
        var name_2 = rank.seasons[mostrecent-2].regions.ncsa.max.name;
        var name_3 = rank.seasons[mostrecent-3].regions.ncsa.max.name;
        var name_4 = rank.seasons[mostrecent-4].regions.ncsa.max.name;
        var name_5 = rank.seasons[mostrecent-5].regions.ncsa.max.name;
        var name_6 = rank.seasons[mostrecent-6].regions.ncsa.max.name;
        var name_7 = rank.seasons[mostrecent-7].regions.ncsa.max.name; 
        var name_8 = rank.seasons[mostrecent-8].regions.ncsa.max.name;
        var name_9 = rank.seasons[mostrecent-9].regions.ncsa.max.name;
        var name_10 = rank.seasons[mostrecent-10].regions.ncsa.max.name;
        var name_11 = rank.seasons[mostrecent-11].regions.ncsa.max.name;

        

    }
    else if(rank.seasons[mostrecent].regions.ncsa.max.mmr <= rank.seasons[mostrecent].regions.emea.max.mmr && rank.seasons[mostrecent].regions.emea.max.mmr >= rank.seasons[mostrecent].regions.apac.max.mmr){
        var mmr_0 = rank.seasons[mostrecent-0].regions.emea.current.mmr;
        var mmr_1 = rank.seasons[mostrecent-1].regions.emea.max.mmr;
        var mmr_2 = rank.seasons[mostrecent-2].regions.emea.max.mmr;
        var mmr_3 = rank.seasons[mostrecent-3].regions.emea.max.mmr;
        var mmr_4 = rank.seasons[mostrecent-4].regions.emea.max.mmr;
        var mmr_5 = rank.seasons[mostrecent-5].regions.emea.max.mmr;
        var mmr_6 = rank.seasons[mostrecent-6].regions.emea.max.mmr;
        var mmr_7 = rank.seasons[mostrecent-7].regions.emea.max.mmr;
        var mmr_8 = rank.seasons[mostrecent-8].regions.emea.max.mmr;
        var mmr_9 = rank.seasons[mostrecent-9].regions.emea.max.mmr;
        var mmr_10 = rank.seasons[mostrecent-10].regions.emea.max.mmr;
        var mmr_11 = rank.seasons[mostrecent-11].regions.emea.max.mmr;
        var name_0 = rank.seasons[mostrecent-0].regions.emea.current.name;
        var name_1 = rank.seasons[mostrecent-1].regions.emea.max.name;
        var name_2 = rank.seasons[mostrecent-2].regions.emea.max.name;
        var name_3 = rank.seasons[mostrecent-3].regions.emea.max.name;
        var name_4 = rank.seasons[mostrecent-4].regions.emea.max.name;
        var name_5 = rank.seasons[mostrecent-5].regions.emea.max.name;
        var name_6 = rank.seasons[mostrecent-6].regions.emea.max.name;
        var name_7 = rank.seasons[mostrecent-7].regions.emea.max.name; 
        var name_8 = rank.seasons[mostrecent-8].regions.emea.max.name;
        var name_9 = rank.seasons[mostrecent-9].regions.emea.max.name;
        var name_10 = rank.seasons[mostrecent-10].regions.emea.max.name;
        var name_11 = rank.seasons[mostrecent-11].regions.emea.max.name;
    }
    else{
        var mmr_0 = rank.seasons[mostrecent-0].regions.apac.current.mmr;
        var mmr_1 = rank.seasons[mostrecent-1].regions.apac.max.mmr;
        var mmr_2 = rank.seasons[mostrecent-2].regions.apac.max.mmr;
        var mmr_3 = rank.seasons[mostrecent-3].regions.apac.max.mmr;
        var mmr_4 = rank.seasons[mostrecent-4].regions.apac.max.mmr;
        var mmr_5 = rank.seasons[mostrecent-5].regions.apac.max.mmr;
        var mmr_6 = rank.seasons[mostrecent-6].regions.apac.max.mmr;
        var mmr_7 = rank.seasons[mostrecent-7].regions.apac.max.mmr;
        var mmr_8 = rank.seasons[mostrecent-8].regions.apac.max.mmr;
        var mmr_9 = rank.seasons[mostrecent-9].regions.apac.max.mmr;
        var mmr_10 = rank.seasons[mostrecent-10].regions.apac.max.mmr;
        var mmr_11 = rank.seasons[mostrecent-11].regions.apac.max.mmr;
        var name_0 = rank.seasons[mostrecent-0].regions.apac.current.name;
        var name_1 = rank.seasons[mostrecent-1].regions.apac.max.name;
        var name_2 = rank.seasons[mostrecent-2].regions.apac.max.name;
        var name_3 = rank.seasons[mostrecent-3].regions.apac.max.name;
        var name_4 = rank.seasons[mostrecent-4].regions.apac.max.name;
        var name_5 = rank.seasons[mostrecent-5].regions.apac.max.name;
        var name_6 = rank.seasons[mostrecent-6].regions.apac.max.name;
        var name_7 = rank.seasons[mostrecent-7].regions.apac.max.name; 
        var name_8 = rank.seasons[mostrecent-8].regions.apac.max.name;
        var name_9 = rank.seasons[mostrecent-9].regions.apac.max.name;
        var name_10 = rank.seasons[mostrecent-10].regions.apac.max.name;
        var name_11 = rank.seasons[mostrecent-11].regions.apac.max.name;
    };


    
    var seasonname_0 = rank.seasons[mostrecent-0].name;
    var seasonname_1 = rank.seasons[mostrecent-1].name;
    var seasonname_2 = rank.seasons[mostrecent-2].name;
    var seasonname_3 = rank.seasons[mostrecent-3].name;
    var seasonname_4 = rank.seasons[mostrecent-4].name;
    var seasonname_5 = rank.seasons[mostrecent-5].name;
    var seasonname_6 = rank.seasons[mostrecent-6].name;
    var seasonname_7 = rank.seasons[mostrecent-7].name;
    var seasonname_8 = rank.seasons[mostrecent-8].name;
    var seasonname_9 = rank.seasons[mostrecent-9].name;
    var seasonname_10 = rank.seasons[mostrecent-10].name;
    var seasonname_11 = rank.seasons[mostrecent-11].name;
    
    var color_0 = rank.seasons[mostrecent-0].color;
    var color_1 = rank.seasons[mostrecent-1].color;
    var color_2 = rank.seasons[mostrecent-2].color;
    var color_3 = rank.seasons[mostrecent-3].color;
    var color_4 = rank.seasons[mostrecent-4].color;
    var color_5 = rank.seasons[mostrecent-5].color;
    var color_6 = rank.seasons[mostrecent-6].color;
    var color_7 = rank.seasons[mostrecent-7].color;
    var color_8 = rank.seasons[mostrecent-8].color;
    var color_9 = rank.seasons[mostrecent-9].color;
    var color_10 = rank.seasons[mostrecent-10].color;
    var color_11 = rank.seasons[mostrecent-11].color;


    var mmr_0 = mmr_0.toFixed();
    var mmr_1 = mmr_1.toFixed();
    var mmr_2 = mmr_2.toFixed();
    var mmr_3 = mmr_3.toFixed();
    var mmr_4 = mmr_4.toFixed();
    var mmr_5 = mmr_5.toFixed();
    var mmr_6 = mmr_6.toFixed();
    var mmr_7 = mmr_7.toFixed();
    var mmr_8 = mmr_8.toFixed();
    var mmr_9 = mmr_9.toFixed();
    var mmr_10 = mmr_10.toFixed();
    var mmr_11 = mmr_11.toFixed();
    
    
    var identifier = `${stats.id}`
    var gen_matches = `${stats.pvp.general.matches}`;
    var gen_wins = `${stats.pvp.general.wins}`;
    var gen_losses = `${stats.pvp.general.losses}`;
    var numerator_wl = gen_wins +0.5;
    var gen_wl = (numerator_wl/ gen_matches );
    var gen_wl = gen_wl * 10;
    var gen_wl = gen_wl.toFixed(2) //Make sure you add the % percent to it in python
    var gen_kills = `${stats.pvp.general.kills}`;
    var gen_deaths = `${stats.pvp.general.deaths}`;
    var gen_kd = gen_kills / gen_deaths;
    var gen_kd = gen_kd.toFixed(2);
    var gen_km = gen_kills / gen_matches
    var gen_km = gen_km.toFixed(2)
    var gen_lvl = `${level.level}`;
    var gen_xp = `${level.xp}`;
    var gen_alphapack = `${level.lootboxProbability.percent}`;
    var gen_playtime = `${timeplayed.general}`;
    var gen_playtime = gen_playtime / 3600;
    var gen_playtime = gen_playtime.toFixed();

    var ran_playtime = `${timeplayed.ranked}`;
    var ran_playtime = ran_playtime / 3600
    var ran_playtime = ran_playtime.toFixed()
    var ran_matches = `${stats.pvp.queue.ranked.matches}`;
    var ran_wins = `${stats.pvp.queue.ranked.wins}`;
    var ran_losses = `${stats.pvp.queue.ranked.losses}`;
    var ran_numerator = ran_wins +0.5;
    var ran_wl = (ran_numerator / ran_matches);
    var ran_wl = ran_wl *10;
    var ran_wl = ran_wl.toFixed(2); // Make sure you add the % percent to it in python
    var ran_kills = `${stats.pvp.queue.ranked.kills}`;
    var ran_deaths = `${stats.pvp.queue.ranked.deaths}`;
    var ran_kd = ran_kills / ran_deaths;
    var ran_kd = ran_kd.toFixed(2);
    var ran_km = ran_kills / ran_matches;
    var ran_km = ran_km.toFixed(2);

    var cas_playtime = `${timeplayed.casual}`;
    var cas_playtime =  cas_playtime / 3600
    var cas_playtime = cas_playtime.toFixed()
    var cas_matches = `${stats.pvp.queue.casual.matches}`;
    var cas_wins = `${stats.pvp.queue.casual.wins}`;
    var cas_losses = `${stats.pvp.queue.casual.losses}`;
    var cas_numerator = cas_wins +0.5;
    var cas_wl = (cas_numerator / cas_matches);
    var cas_wl = cas_wl *10;
    var cas_wl = cas_wl.toFixed(2); // Make sure you add the % percent to it in python
    var cas_kills = `${stats.pvp.queue.casual.kills}`;
    var cas_deaths = `${stats.pvp.queue.casual.deaths}`;
    var cas_kd = cas_kills / cas_deaths;
    var cas_kd = cas_kd.toFixed(2);
    var cas_km = cas_kills / cas_matches;
    var cas_km = cas_km.toFixed(2);

    var pve_matches = `${stats.pve.general.matches}`;
    var pve_wins = `${stats.pve.general.wins}`;
    var pve_losses = `${stats.pve.general.losses}`;
    var pve_numerator = pve_wins +0.5;
    var pve_wl = (pve_numerator / pve_matches);
    var pve_wl = pve_wl *10;
    var pve_wl = pve_wl.toFixed(2); // Make sure you add the % percent to it in python
    var pve_kills = `${stats.pve.general.kills}`;
    var pve_deaths = `${stats.pve.general.deaths}`;
    var pve_kd = pve_kills / pve_deaths;
    var pve_kd = pve_kd.toFixed(2);
    var pve_km = pve_kills / pve_matches;
    var pve_km = pve_km.toFixed(2);

    var spec_assist = `${stats.pvp.general.assists}`;
    var spec_melee = `${stats.pvp.general.meleeKills}`;
    var spec_revives = `${stats.pvp.general.revives}`;
    var spec_wallbangs = `${stats.pvp.general.penetrationKills}`;
    var spec_blindkills = `${stats.pvp.general.blindKills}`;
    var spec_suicide = `${stats.pvp.general.suicides}`;
    var spec_barricades = `${stats.pvp.general.barricadesDeployed}`;
    var spec_gadgets = `${stats.pvp.general.gadgetsDestroyed}`; // grabbing our stats
    


    var statistics = `${username}`+'\n'+identifier+'\n'+gen_matches+'\n'+gen_wins+'\n'+gen_losses+'\n'+gen_wl+'\n'+gen_kills+'\n'+ //combining all the stats into one variable
    gen_deaths+'\n'+gen_kd +'\n'+gen_km+'\n'+ gen_lvl + '\n' + gen_xp + '\n' + gen_alphapack +'\n' + gen_playtime+'\n'+ran_playtime+'\n'+cas_playtime+'\n'+
    ran_matches+'\n'+ran_wins+'\n'+ran_losses+'\n'+ran_wl+'\n'+ran_kills+'\n'+ran_deaths+'\n'+ran_kd+
    '\n'+cas_matches+'\n'+cas_wins+'\n'+cas_losses+'\n'+cas_wl+'\n'+cas_kills+'\n'+cas_deaths+'\n'+cas_kd+'\n'+pve_matches+'\n'+pve_wins+'\n'+pve_losses+'\n'+
    pve_wl+'\n'+pve_kills+'\n'+pve_deaths+'\n'+pve_kd+'\n'+pve_km+'\n'+spec_assist+'\n'+spec_melee+'\n'+spec_revives+'\n'+spec_wallbangs+'\n'+spec_blindkills+'\n'+spec_suicide+'\n'+
    spec_barricades+'\n'+spec_gadgets+'\n'+seasonname_0+'\n'+seasonname_1+'\n'+seasonname_2+'\n'+seasonname_3+'\n'+seasonname_4+'\n'+seasonname_5+'\n'+seasonname_6+'\n'+seasonname_7+'\n'+
    seasonname_8+'\n'+seasonname_9+'\n'+seasonname_10+'\n'+seasonname_11+'\n'+name_0+'\n'+mmr_0+'\n'+name_1+'\n'+mmr_1+'\n'+name_2+'\n'+mmr_2+'\n'+name_3+'\n'+mmr_3+'\n'+name_4+'\n'+mmr_4+'\n'+name_5+'\n'+mmr_5+'\n'+
    name_6+'\n'+mmr_6+'\n'+name_7+'\n'+mmr_7+'\n'+name_8+'\n'+mmr_8+'\n'+name_9+'\n'+mmr_9+'\n'+name_10+'\n'+mmr_10+'\n'+name_11+'\n'+mmr_11+'\n'+color_0+'\n'+color_1+'\n'+color_2+'\n'+color_3+'\n'+color_4+'\n'+color_5+'\n'+color_6+'\n'+
    color_7+'\n'+color_8+'\n'+color_9+'\n'+color_10+'\n'+color_11;

    
    var datawrite = statistics;
    fs.writeFile('data.txt', datawrite, function (err) {
    if (err) return console.log(err);   //writing our stats to the txt file
    console.log('\nWrote it to file data.txt');
    process.exit();
    });
    fs.close()
    console.log(datawrite);

    
    

}

api_call();






function promisecheck() {
    let promise = new Promise(function(resolve, reject) {
        setTimeout(() => resolve({msg: 'uhhhh, idk what just happened'}), 1000); //promise check for our async
    });
    
    promise.then((result) => {
        console.log("Success", result);
    }).catch((error) => {
        console.log("Error", error);
    });
}

