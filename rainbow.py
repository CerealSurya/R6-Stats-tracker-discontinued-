def rainbow_func():
    from tkinter import font, END, ttk
    import tkinter as tk
    from PIL import ImageTk, Image
    from Naked.toolshed.shell import execute_js, muterun_js
    import os
    





    

    #Created by @Cereal.Surya
    #And yes I know its bad

    HEIGHT = 700
    WIDTH = 800
    header_size = ('Comic Sans MS', 35)
    smallheader_size = ('Comic Sans MS', 25)
    text_size = ('Comic Sans MS', 15)
    season_size = ('Comic Sans MS', 17)
    mmr_size = ('Comic Sans MS', 10)
    header_color = "#00b377"
    outline_color = '#000000'
    text_color = "#ffffff"
    text_bg = "#4d4d4d"
    header_bg = "#333333"
    faintwhite_color = "#fbfbff"
    searchbarbg = '#d9d9d9'
    searchbarcolor = "#404040"
    root2 = tk.Toplevel() #everything goes inside here
    root2.title('Rainbow Six Siege Stats tracker')
    c5 = tk.PhotoImage(file = 'resources/ranks/c5.png')
    c4 = tk.PhotoImage(file = 'resources/ranks/c4.png') #loading our rank icons
    c3 = tk.PhotoImage(file = 'resources/ranks/c3.png')
    c2 = tk.PhotoImage(file = 'resources/ranks/c2.png')
    c1 = tk.PhotoImage(file = 'resources/ranks/c1.png')

    b5 = tk.PhotoImage(file = 'resources/ranks/b5.png')
    b4 = tk.PhotoImage(file = 'resources/ranks/b4.png')
    b3 = tk.PhotoImage(file = 'resources/ranks/b3.png')
    b2 = tk.PhotoImage(file = 'resources/ranks/b2.png')
    b1 = tk.PhotoImage(file = 'resources/ranks/b1.png')

    s5 = tk.PhotoImage(file = 'resources/ranks/s5.png')
    s4 = tk.PhotoImage(file = 'resources/ranks/s4.png')
    s3 = tk.PhotoImage(file = 'resources/ranks/s3.png')
    s2 = tk.PhotoImage(file = 'resources/ranks/s2.png')
    s1 = tk.PhotoImage(file = 'resources/ranks/s1.png')

    g3 = tk.PhotoImage(file = 'resources/ranks/g3.png')
    g2 = tk.PhotoImage(file = 'resources/ranks/g2.png')
    g1 = tk.PhotoImage(file = 'resources/ranks/g1.png')

    p3 = tk.PhotoImage(file = 'resources/ranks/p3.png')
    p2 = tk.PhotoImage(file = 'resources/ranks/p2.png')
    p1 = tk.PhotoImage(file = 'resources/ranks/p1.png')

    dia = tk.PhotoImage(file = 'resources/ranks/d1.png')
    champ = tk.PhotoImage(file = 'resources/ranks/champ.png')
    unranked = tk.PhotoImage(file = 'resources/ranks/unranked.png')

    cerealemojii1 = tk.PhotoImage(file = 'resources/emojiis/1.png')
    cerealemojii2 = tk.PhotoImage(file = 'resources/emojiis/2.png')
    cerealemojii3 = tk.PhotoImage(file = 'resources/emojiis/3.png')
    cerealemojii4 = tk.PhotoImage(file = 'resources/emojiis/4.png')
    cerealemojii5 = tk.PhotoImage(file = 'resources/emojiis/5.png')
    cerealemojii6 = tk.PhotoImage(file = 'resources/emojiis/6.png')
    prof = tk.PhotoImage(file = 'resources/profile.png')
    



    cerealtitle1 = 'DOGGY DOO DOO'
    cerealtitle2 = 'ACTUAL BOT'
    cerealtitle3 = 'Decent'
    cerealtitle4 = 'Sweaty'
    cerealtitle5 = 'Cracked'
    cerealtitle6 = 'The goat'
    cerealdesc1 = 'Actual booty cheeks\nat the game'
    cerealdesc2 = 'Hot garbage\nat the game'
    cerealdesc3 = 'Ur alright\nat the game'
    cerealdesc4 = "Mans doesn't know\nwhat a shower is"
    cerealdesc5 = 'Bro ur insane'
    cerealdesc6 = 'Your either goated\nor hacking'



    def statsget():
        try:
            checkerr = open('errlog.txt', 'r')
            err = str(checkerr.readline()).strip()
            errmessage = 'error invalid username and or platform'
            if err == errmessage:
                blankwrite()
                top_label['text'] = 'ERROR-\n Could not find player'
                top_label['fg'] = '#cc0000'
                checkerr.close()  
                os.remove("errlog.txt")
        except:               
            f = open("data.txt", "r") #Where we are reading our stats from data.txt
            username = str(f.readline()).strip()
            identifier = str(f.readline()).strip()
            tot_matches = str(f.readline()).strip()
            tot_wins = str(f.readline()).strip()
            tot_losses = str(f.readline()).strip()
            tot_wl = float(f.readline())
            tot_kills = str(f.readline()).strip()
            tot_deaths = str(f.readline()).strip()
            tot_kd = float(f.readline())
            tot_km = str(f.readline()).strip()
            tot_lvl = str(f.readline()).strip()
            tot_xp = str(f.readline()).strip()
            tot_alphapercent = str(f.readline()).strip()
            tot_playtime = int(f.readline())
            rank_playtime = int(f.readline())
            cas_playtime = int(f.readline())
            rank_matches = str(f.readline()).strip()
            rank_wins = str(f.readline()).strip()
            rank_losses = str(f.readline()).strip()
            rank_wl = str(f.readline()).strip()
            rank_kills = str(f.readline()).strip()
            rank_deaths = str(f.readline()).strip()
            rank_kd = str(f.readline()).strip()
            cas_matches = str(f.readline()).strip()
            cas_wins = str(f.readline()).strip()
            cas_losses = str(f.readline()).strip()
            cas_wl = str(f.readline()).strip()
            cas_kills = str(f.readline()).strip()
            cas_deaths = str(f.readline()).strip()
            cas_kd = str(f.readline()).strip()
            pve_matches = str(f.readline()).strip()
            pve_wins = str(f.readline()).strip()
            pve_losses = str(f.readline()).strip()
            pve_wl = str(f.readline()).strip()
            pve_kills = str(f.readline()).strip()
            pve_deaths = str(f.readline()).strip()
            pve_kd = str(f.readline()).strip()
            pve_km = str(f.readline()).strip()
            spec_assist = str(f.readline()).strip()
            spec_melee = str(f.readline()).strip()
            spec_revives = str(f.readline()).strip()
            spec_wallbangs = str(f.readline()).strip()
            spec_blindkills = str(f.readline()).strip()
            spec_suicide = str(f.readline()).strip()
            spec_barricades = str(f.readline()).strip()
            spec_gadgets = str(f.readline()).strip()
            seasonname_0 = str(f.readline()).strip()
            seasonname_1 = str(f.readline()).strip()
            seasonname_2 = str(f.readline()).strip()
            seasonname_3 = str(f.readline()).strip()
            seasonname_4 = str(f.readline()).strip()
            seasonname_5 = str(f.readline()).strip()
            seasonname_6 = str(f.readline()).strip()
            seasonname_7 = str(f.readline()).strip()
            seasonname_8 = str(f.readline()).strip()
            seasonname_9 = str(f.readline()).strip()
            seasonname_10 = str(f.readline()).strip()
            seasonname_11 = str(f.readline()).strip()
            rankname_0 = str(f.readline()).strip()
            mmr_0 = int(f.readline())
            rankname_1 = str(f.readline()).strip()
            mmr_1 = str(f.readline()).strip()
            rankname_2 = str(f.readline()).strip()
            mmr_2 = str(f.readline()).strip()
            rankname_3 = str(f.readline()).strip()
            mmr_3 = str(f.readline()).strip()
            rankname_4 = str(f.readline()).strip()
            mmr_4 = str(f.readline()).strip()
            rankname_5 = str(f.readline()).strip()
            mmr_5 = str(f.readline()).strip()
            rankname_6 = str(f.readline()).strip()
            mmr_6 = str(f.readline()).strip()
            rankname_7 = str(f.readline()).strip()
            mmr_7 = str(f.readline()).strip()
            rankname_8 = str(f.readline()).strip()
            mmr_8 = str(f.readline()).strip()
            rankname_9 = str(f.readline()).strip()
            mmr_9 = str(f.readline()).strip()
            rankname_10 = str(f.readline()).strip()
            mmr_10 = str(f.readline()).strip()
            rankname_11 = str(f.readline()).strip()
            mmr_11 = str(f.readline()).strip()
            color_0 = str(f.readline()).strip()
            color_1 = str(f.readline()).strip()
            color_2 = str(f.readline()).strip()
            color_3 = str(f.readline()).strip()
            color_4 = str(f.readline()).strip()
            color_5 = str(f.readline()).strip()
            color_6 = str(f.readline()).strip()
            color_7 = str(f.readline()).strip()
            color_8 = str(f.readline()).strip()
            color_9 = str(f.readline()).strip()
            color_10 = str(f.readline()).strip()
            color_11 = str(f.readline()).strip()
            f.close()
        try:
            ranktototalhrs = round(rank_playtime / tot_playtime, 2)# defining our factors to determine cereal sweat rating 
            #getting our cereal sweat rating

            if ranktototalhrs <=.2:
                ranktototalhrs_rating = 40
            if ranktototalhrs >.2 and ranktototalhrs <.4:
                ranktototalhrs_rating = 80
            if ranktototalhrs >=.4 and ranktototalhrs <.6:
                ranktototalhrs_rating = 160
            if ranktototalhrs >=.6 and ranktototalhrs <1: #Determining the score for each factor in our cereal rating
                ranktototalhrs_rating = 300
            if ranktototalhrs >= 1:
                ranktototalhrs_rating = 320
        except(ZeroDivisionError):
            ranktototalhrs = 20
        if tot_kd <=.2:
            tot_kd_rating = 40
        if tot_kd >.2 and tot_kd <.4:
            tot_kd_rating=80
        if tot_kd >=.4 and tot_kd <.6:
            tot_kd_rating = 160
        if tot_kd >=.6 and tot_kd <8:
            tot_kd_rating = 300
        if tot_kd>=.8 and tot_kd<1:
            tot_kd_rating = 320
        if tot_kd>=1 and tot_kd <=1.5:
            tot_kd_rating = 400
        if tot_kd > 1.5:
            if mmr_0 > 2900:
                tot_kd_rating = 800
            else:
                tot_kd_rating=450

        if tot_wl <= 30:
            tot_wl_rating = 30
        if tot_wl >30 and tot_wl <40:
            tot_wl_rating=60
        if tot_wl >=40 and tot_wl <50:
            tot_wl_rating=120
        if tot_wl>=50 and tot_wl<60:
            tot_wl_rating = 240
        if tot_wl>=60 and tot_wl<75:
            tot_wl_rating=300
        if tot_wl >=75:
            tot_wl_rating=350

        if mmr_0 <= 1600:
            mmr_rating = 20
        if mmr_0 >1600 and mmr_0<2100:
            mmr_rating=80
        if mmr_0 >=2100 and mmr_0<2600:
            mmr_rating=160
        if mmr_0 >=2600 and mmr_0<3200:
            mmr_rating=200
        if mmr_0 >=3200 and mmr_0<=4400:
            mmr_rating=350
        if mmr_0 >4400:
            mmr_rating=600
        
        print('kd rating- ', tot_kd_rating, 'rank hours ratio rating - ', ranktototalhrs_rating, 'wl rating  -', tot_wl_rating, 'mmr rating - ', mmr_rating)

        rawcerealrating = tot_kd_rating + ranktototalhrs_rating + tot_wl_rating + mmr_rating
        print('Cereal rating-',rawcerealrating)
        if rawcerealrating <= 700:
            finalcerealrating = 1
        if rawcerealrating > 700 and rawcerealrating <= 800:
            finalcerealrating = 2
        if rawcerealrating > 800 and rawcerealrating <= 950:
            finalcerealrating = 3
        if rawcerealrating > 950 and rawcerealrating <= 1325:
            finalcerealrating = 4
        if rawcerealrating > 1325 and rawcerealrating <= 1785:
            finalcerealrating = 5
        if rawcerealrating > 1785:
            finalcerealrating = 6
        
        if finalcerealrating == 1:
            Cerealrating_text['text'] = cerealtitle1
            Cerealrating_desc['text'] = cerealdesc1
            emojii_label['image'] = cerealemojii1
        if finalcerealrating == 2:
            Cerealrating_text['text'] = cerealtitle2
            Cerealrating_desc['text'] = cerealdesc2
            emojii_label['image'] = cerealemojii2
        if finalcerealrating == 3:
            Cerealrating_text['text'] = cerealtitle3
            Cerealrating_desc['text'] = cerealdesc3
            emojii_label['image'] = cerealemojii3
        if finalcerealrating == 4:
            Cerealrating_text['text'] = cerealtitle4
            Cerealrating_desc['text'] = cerealdesc4
            emojii_label['image'] = cerealemojii4
        if finalcerealrating == 5:
            Cerealrating_text['text'] = cerealtitle5
            Cerealrating_desc['text'] = cerealdesc5
            emojii_label['image'] = cerealemojii5
        if finalcerealrating == 6:
            Cerealrating_text['text'] = cerealtitle6
            Cerealrating_desc['text'] = cerealdesc6
            emojii_label['image'] = cerealemojii6

        
        

        
        

        

        tot_playtime = str(tot_playtime).strip()
        rank_playtime = str(rank_playtime).strip()
        cas_playtime = str(cas_playtime).strip()
        tot_kd = str(tot_kd).strip()
        mmr_0 = str(mmr_0).strip()
        tot_wl = str(tot_wl).strip()

        
        overall_column1['text'] = tot_playtime+'h\nTime Played'
        overall_column1_row2['text'] = tot_kills+'\nKills'
        overall_column1_row3['text'] = tot_deaths+'\nDeaths'
        overall_column2['text'] = tot_matches+'\nMatches Played'
        overall_column2_row2['text'] = tot_losses+'\nLosses'
        overall_column2_row3['text'] = tot_wins+'\nWins'
        overall_column3['text'] = tot_km+'\nK/M'
        overall_column3_row2['text'] = tot_kd+'\nK/D'
        overall_column3_row3['text'] = tot_wl+'\nW/L'

        specifics_column1['text'] = spec_assist+'\nAssists'
        specifics_column1_row2['text'] = spec_melee+'\nMelee Kills'
        specifics_column1_row3['text'] = spec_revives+'\nRevives'
        specifics_column1_row4['text'] = spec_wallbangs+'\nWall Bangs'
        specifics_column2['text'] = spec_blindkills+'\nBlind Kills'
        specifics_column2_row2['text'] = spec_suicide+'\nSuicides'
        specifics_column2_row3['text'] = spec_barricades+'\nBarricades Deployed'
        specifics_column2_row4['text'] = spec_gadgets+'\nGadgets destroyed'

        casual_column1['text'] = cas_playtime+'h\nTime Played'
        casual_column1_row2['text'] = cas_kills+'\nKills'
        casual_column1_row3['text'] = cas_deaths+'\nDeaths'
        casual_column1_row4['text'] = cas_kd+'\nK/D'
        casual_column2['text'] = cas_matches+'\nMatches Played'
        casual_column2_row2['text'] = cas_wins+'\nWins'
        casual_column2_row3['text'] = cas_losses+'\nLosses'
        casual_column2_row4['text'] = cas_wl+'\nW/L'

        ranked_column1['text'] = rank_playtime+'h\nTime Played'
        ranked_column1_row2['text'] = rank_kills+'\nKills'
        ranked_column1_row3['text'] = rank_deaths+'\nDeaths'
        ranked_column1_row4['text'] = rank_kd+'\nK/D'
        ranked_column2['text'] = rank_matches+'\nMatches Played'
        ranked_column2_row2['text'] = rank_wins+'\nWins'
        ranked_column2_row3['text'] = rank_losses+'\nLosses'
        ranked_column2_row4['text'] = rank_wl+'\nW/L'

        overall_column0['text'] = 'Overall - '
        specifics_column0['text'] = 'Specifics - '
        Cerealrating_title['text'] = 'Cereal Sweat Rating -' 
        casual_column0['text'] = 'Casual'
        ranked_column0['text'] = 'Ranked'
        

        player_desc['text'] = username +'  ' + tot_playtime+'h'+'\n'+'lvl- '+tot_lvl+'  '+'xp - '+tot_xp
        player_desc['font'] = text_size
        top_label['image'] = top_image

        icon_selector(rankname_0,ranklist_column0_row0_icon,ranklist_column0_row0_mmr,ranklist_column0_row0_title, mmr_0, seasonname_0, color_0)
        icon_selector(rankname_1,ranklist_column0_row1_icon,ranklist_column0_row1_mmr,ranklist_column0_row1_title, mmr_1, seasonname_1, color_1)
        icon_selector(rankname_2,ranklist_column0_row2_icon,ranklist_column0_row2_mmr,ranklist_column0_row2_title, mmr_2, seasonname_2, color_2)
        icon_selector(rankname_3,ranklist_column0_row3_icon,ranklist_column0_row3_mmr,ranklist_column0_row3_title, mmr_3, seasonname_3, color_3)
        icon_selector(rankname_4,ranklist_column1_row0_icon,ranklist_column1_row0_mmr,ranklist_column1_row0_title, mmr_4, seasonname_4, color_4)
        icon_selector(rankname_5,ranklist_column1_row1_icon,ranklist_column1_row1_mmr,ranklist_column1_row1_title, mmr_5, seasonname_5, color_5)
        icon_selector(rankname_6,ranklist_column1_row2_icon,ranklist_column1_row2_mmr,ranklist_column1_row2_title, mmr_6, seasonname_6, color_6)
        icon_selector(rankname_7,ranklist_column1_row3_icon,ranklist_column1_row3_mmr,ranklist_column1_row3_title, mmr_7, seasonname_7, color_7)
        icon_selector(rankname_8,ranklist_column2_row0_icon,ranklist_column2_row0_mmr,ranklist_column2_row0_title, mmr_8, seasonname_8, color_8)
        icon_selector(rankname_9,ranklist_column2_row1_icon,ranklist_column2_row1_mmr,ranklist_column2_row1_title, mmr_9, seasonname_9, color_9)
        icon_selector(rankname_10,ranklist_column2_row2_icon,ranklist_column2_row2_mmr,ranklist_column2_row2_title, mmr_10, seasonname_10, color_10)
        icon_selector(rankname_11,ranklist_column2_row3_icon,ranklist_column2_row3_mmr,ranklist_column2_row3_title, mmr_11, seasonname_11, color_11)

 

        
        

        
        player_profp_l['image'] =  prof





        
    def icon_selector(rank, image, mmrlabel, seasonlabel, mmr, season, color):
        rank = rank
        label = image
        mmrlabel = mmrlabel
        seasonlabel = seasonlabel
        season = season
        mmr = mmr
        color = color

        if rank == 'Copper 5':
            label['image'] = c5
        if rank == 'Copper 4':
            label['image'] = c4
        if rank == 'Copper 3':
            label['image'] = c3
        if rank == 'Copper 2':
            label['image'] = c2
        if rank == 'Copper 1':
            label['image'] = c1
        if rank == 'Bronze 5':
            label['image'] = b5
        if rank == 'Bronze 4':
            label['image'] = b4
        if rank == 'Bronze 3':
            label['image'] = b3
        if rank == 'Bronze 2':
            label['image'] = b2
        if rank == 'Bronze 1':
            label['image'] = b1
        if rank == 'Silver 5':
            label['image'] = s5
        if rank == 'Silver 4':
            label['image'] = s4
        if rank == 'Silver 3':
            label['image'] = s3
        if rank == 'Silver 2':
            label['image'] = s2
        if rank == 'Silver 1':
            label['image'] = s1
        if rank == 'Gold 3':
            label['image'] = g3
        if rank == 'Gold 2':
            label['image'] = g2
        if rank == 'Gold 1':
            label['image'] = g1
        if rank == 'Platinum 3':
            label['image'] = p3
        if rank == 'Platinum 2':
            label['image'] = p2
        if rank == 'Platinum 1':
            label['image'] = p1
        if rank == 'Diamond':
            label['image'] = dia
        if rank == 'Champions':
            label['image'] = champ
        if rank == 'Unranked':
            label['image'] = unranked
        
        mmrlabel['text'] = mmr + ' '+rank
        seasonlabel['text'] = season
        seasonlabel['fg'] = color
        
        
        
    def blankwrite():
        overall_column1['text'] = ''
        overall_column1_row2['text'] = ''
        overall_column1_row3['text'] = ''
        overall_column2['text'] = ''
        overall_column2_row2['text'] = ''
        overall_column2_row3['text'] = ''
        overall_column3['text'] = ''
        overall_column3_row2['text'] = ''
        overall_column3_row3['text'] =''

        specifics_column1['text'] = ' '
        specifics_column1_row2['text'] = ' '
        specifics_column1_row3['text'] = ' '
        specifics_column1_row4['text'] = ' '
        specifics_column2['text'] = ' '
        specifics_column2_row2['text'] = ' '
        specifics_column2_row3['text'] = ' '
        specifics_column2_row4['text'] = ' '

        casual_column1['text'] = ' '
        casual_column1_row2['text'] = ' '
        casual_column1_row3['text'] = ' '
        casual_column1_row4['text'] = ' '
        casual_column2['text'] = ' '
        casual_column2_row2['text'] = ' '
        casual_column2_row3['text'] = ' '
        casual_column2_row4['text'] = ' '

        ranked_column1['text'] = ' '
        ranked_column1_row2['text'] = ' '
        ranked_column1_row3['text'] = ' '
        ranked_column1_row4['text'] = ' '
        ranked_column2['text'] = ' '
        ranked_column2_row2['text'] = ' '
        ranked_column2_row3['text'] = ' '
        ranked_column2_row4['text'] = ' '
        emojii_label['image'] = ''
        ranklist_column0_row0_icon['image'] = ''
        ranklist_column0_row1_icon['image'] = ''
        ranklist_column0_row2_icon['image'] = ''
        ranklist_column0_row3_icon['image'] = ''
        ranklist_column1_row0_icon['image'] = ''
        ranklist_column1_row1_icon['image'] = ''
        ranklist_column1_row2_icon['image'] = ''
        ranklist_column1_row3_icon['image'] = ''
        ranklist_column2_row0_icon['image'] = ''
        ranklist_column2_row1_icon['image'] = ''
        ranklist_column2_row2_icon['image'] = ''
        ranklist_column2_row3_icon['image'] = ''
        ranklist_column0_row0_icon['bg'] = text_bg
        ranklist_column0_row1_icon['bg'] = text_bg
        ranklist_column0_row2_icon['bg'] = text_bg
        ranklist_column0_row3_icon['bg'] = text_bg
        ranklist_column1_row0_icon['bg'] = text_bg
        ranklist_column1_row1_icon['bg'] = text_bg
        ranklist_column1_row2_icon['bg'] = text_bg
        ranklist_column1_row3_icon['bg'] = text_bg
        ranklist_column2_row0_icon['bg'] = text_bg
        ranklist_column2_row1_icon['bg'] = text_bg
        ranklist_column2_row2_icon['bg'] = text_bg
        ranklist_column2_row3_icon['bg'] = text_bg
        overall_column0['text'] = ''
        specifics_column0['text'] = ''
        Cerealrating_title['text'] = ''
        Cerealrating_text['text'] = ''
        Cerealrating_desc['text'] = ''
        casual_column0['text'] = ''
        ranked_column0['text'] = ''
        ranklist_column0_row0_title['text'] = ''
        ranklist_column0_row0_mmr['text'] = ''
        ranklist_column0_row1_title['text'] = ''
        ranklist_column0_row1_mmr['text'] = ''
        ranklist_column0_row2_title['text'] = ''
        ranklist_column0_row2_mmr['text'] = ''
        ranklist_column0_row3_title['text'] = ''
        ranklist_column0_row3_mmr['text'] = ''
        ranklist_column1_row0_title['text'] = ''
        ranklist_column1_row0_mmr['text'] = ''
        ranklist_column1_row1_title['text'] = ''
        ranklist_column1_row1_mmr['text'] = ''
        ranklist_column1_row2_title['text'] = ''
        ranklist_column1_row2_mmr['text'] = ''
        ranklist_column1_row3_title['text'] = ''
        ranklist_column1_row3_mmr['text'] = ''
        ranklist_column2_row0_title['text'] = ''
        ranklist_column2_row0_mmr['text'] = ''
        ranklist_column2_row1_title['text'] = ''
        ranklist_column2_row1_mmr['text'] = ''
        ranklist_column2_row2_title['text'] = ''
        ranklist_column2_row2_mmr['text'] = ''
        ranklist_column2_row3_title['text'] = ''
        ranklist_column2_row3_mmr['text'] = ''
        player_profp_l['bg'] = header_bg
        player_profp_l['image'] = ''
        top_label['fg'] = text_color
        top_label['image'] = ''
        
        

        player_desc['text'] = ''
        player_desc['font'] = text_size
        
        

    
    def searchfunc(entry): #function that executes whenever we send a playername and platform
        enterdata = open('enter.txt', 'w+')
        username = entry
        platform = select.get()
        enterdata.writelines('%s \n %s' % (username, platform))
        enterdata.close()
        success = execute_js('rainbow_api.js')
        statsget()
        if not success:
            print('its actually successful, its mind games')
        

    canvas = tk.Canvas(master = root2, width = WIDTH, height = HEIGHT)
    canvas.pack()





    background_label = tk.Frame(root2, bg = '#404040')
    background_label.place(relwidth=1, relheight=1)

    top_image = tk.PhotoImage(file="resources/newheader.png")
    top_label = tk.Label(master = background_label, text = 'ENTER USERNAME -->', bg ='#404040', fg = text_color, font = ('Comic Sans MS', 55) )
    top_label.place(relwidth=1, relheight=.45)

    
    player_card = tk.Label(master =background_label, bg = header_bg)
    player_card.place(rely = .3, relx = .12, relwidth=.5, relheight=.23)


    searchbar = tk.Frame(background_label, bg = searchbarbg, bd = 4)
    searchbar.place(relwidth = .20, relx=.8, height=50) 


    player_profp_l = tk.Label(master =player_card,bg=header_bg)
    player_profp_l.place(rely =0.05, relx=.132, width=100, height=100) 

    player_desc = tk.Label(master = player_card, bg = header_bg,fg = text_color, font =text_size )
    player_desc.place( rely = .57, relwidth = .4, relheight = .33)
    


    ranklist_label = tk.Label(background_label, bg = text_bg, bd = 5 ) #Our rank list label parent creation
    ranklist_label.place(relx = .27, rely = .75, relwidth = .33, relheight = .24)

    ranklist_column0 = tk.Label(ranklist_label,bg = text_bg, fg = text_color, font = text_size, bd=0 )
    ranklist_column0.place(relwidth=.33, relheight=1)

    ranklist_column0_row0 = tk.Label(ranklist_column0, bg = text_bg, bd=0)
    ranklist_column0_row0.place(relwidth=1, relheight = .21)
    ranklist_column0_row0_title = tk.Label(ranklist_column0_row0, bg = text_bg, fg = text_color, font =season_size, text = 'Season-', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column0_row0_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column0_row0_mmr = tk.Label(ranklist_column0_row0, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column0_row0_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column0_row0_icon = tk.Label(master = ranklist_column0_row0)
    ranklist_column0_row0_icon.place(width=50, height=50)

    ranklist_column0_row1 = tk.Label(ranklist_column0, bg = text_bg, bd=0)
    ranklist_column0_row1.place(rely=.24,relwidth=1, relheight = .21)
    ranklist_column0_row1_title = tk.Label(ranklist_column0_row1, bg = text_bg, fg = text_color, font =season_size, text = 'Season-1', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column0_row1_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column0_row1_mmr = tk.Label(ranklist_column0_row1, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column0_row1_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column0_row1_icon = tk.Label(master = ranklist_column0_row1)
    ranklist_column0_row1_icon.place(width=50, height=50)

    ranklist_column0_row2 = tk.Label(ranklist_column0, bg = text_bg, bd=0)
    ranklist_column0_row2.place(rely=.48,relwidth=1, relheight = .21)
    ranklist_column0_row2_title = tk.Label(ranklist_column0_row2, bg = text_bg, fg = text_color, font =season_size, text = 'Season-2', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column0_row2_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column0_row2_mmr = tk.Label(ranklist_column0_row2, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column0_row2_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column0_row2_icon = tk.Label(master = ranklist_column0_row2)
    ranklist_column0_row2_icon.place(width=50, height=50)

    ranklist_column0_row3 = tk.Label(ranklist_column0, bg = text_bg, bd=0)
    ranklist_column0_row3.place(rely=.73,relwidth=1, relheight = .21)
    ranklist_column0_row3_title = tk.Label(ranklist_column0_row3, bg = text_bg, fg = text_color, font =season_size, text = 'Season-3', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column0_row3_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column0_row3_mmr = tk.Label(ranklist_column0_row3, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column0_row3_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column0_row3_icon = tk.Label(master = ranklist_column0_row3)
    ranklist_column0_row3_icon.place(width=50, height=50)

    ranklist_column1 = tk.Label(ranklist_label,bg = text_bg, fg = text_color, font = text_size, bd=0 )
    ranklist_column1.place(relx=.33,relwidth=.33, relheight=1)

    ranklist_column1_row0 = tk.Label(ranklist_column1, bg = text_bg, bd=0)
    ranklist_column1_row0.place(relwidth=1, relheight = .21)
    ranklist_column1_row0_title = tk.Label(ranklist_column1_row0, bg = text_bg, fg = text_color, font =season_size, text = 'Season-4', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column1_row0_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column1_row0_mmr = tk.Label(ranklist_column1_row0, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column1_row0_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column1_row0_icon = tk.Label(master = ranklist_column1_row0)
    ranklist_column1_row0_icon.place(width=50, height=50)

    ranklist_column1_row1 = tk.Label(ranklist_column1, bg = text_bg, bd=0)
    ranklist_column1_row1.place(rely = .24,relwidth=1, relheight = .21)
    ranklist_column1_row1_title = tk.Label(ranklist_column1_row1, bg = text_bg, fg = text_color, font =season_size, text = 'Season-5', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column1_row1_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column1_row1_mmr = tk.Label(ranklist_column1_row1, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column1_row1_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column1_row1_icon = tk.Label(master = ranklist_column1_row1)
    ranklist_column1_row1_icon.place(width=50, height=50)

    ranklist_column1_row2 = tk.Label(ranklist_column1, bg = text_bg, bd=0)
    ranklist_column1_row2.place(rely = .48,relwidth=1, relheight = .21)
    ranklist_column1_row2_title = tk.Label(ranklist_column1_row2, bg = text_bg, fg = text_color, font =season_size, text = 'Season-6', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column1_row2_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column1_row2_mmr = tk.Label(ranklist_column1_row2, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column1_row2_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column1_row2_icon = tk.Label(master = ranklist_column1_row2)
    ranklist_column1_row2_icon.place(width=50, height=50)

    ranklist_column1_row3 = tk.Label(ranklist_column1, bg = text_bg, bd=0)
    ranklist_column1_row3.place(rely = .73,relwidth=1, relheight = .21)
    ranklist_column1_row3_title = tk.Label(ranklist_column1_row3, bg = text_bg, fg = text_color, font =season_size, text = 'Season-7', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column1_row3_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column1_row3_mmr = tk.Label(ranklist_column1_row3, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column1_row3_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column1_row3_icon = tk.Label(master = ranklist_column1_row3)
    ranklist_column1_row3_icon.place(width=50, height=50)

    ranklist_column2 = tk.Label(ranklist_label,bg = text_bg, fg = text_color, font = text_size, bd=0 )
    ranklist_column2.place(relx=.66,relwidth=.33, relheight=1)

    ranklist_column2_row0 = tk.Label(ranklist_column2, bg = text_bg, bd=0)
    ranklist_column2_row0.place(relwidth=1, relheight = .21)
    ranklist_column2_row0_title = tk.Label(ranklist_column2_row0, bg = text_bg, fg = text_color, font =season_size, text = 'Season-8', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column2_row0_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column2_row0_mmr = tk.Label(ranklist_column2_row0, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column2_row0_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column2_row0_icon = tk.Label(master = ranklist_column2_row0)
    ranklist_column2_row0_icon.place(width=50, height=50)

    ranklist_column2_row1 = tk.Label(ranklist_column2, bg = text_bg, bd=0)
    ranklist_column2_row1.place(rely=.24,relwidth=1, relheight = .21)
    ranklist_column2_row1_title = tk.Label(ranklist_column2_row1, bg = text_bg, fg = text_color, font =season_size, text = 'Season-9', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column2_row1_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column2_row1_mmr = tk.Label(ranklist_column2_row1, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column2_row1_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column2_row1_icon = tk.Label(master = ranklist_column2_row1)
    ranklist_column2_row1_icon.place(width=50, height=50)

    ranklist_column2_row2 = tk.Label(ranklist_column2, bg = text_bg, bd=0)
    ranklist_column2_row2.place(rely=.48,relwidth=1, relheight = .21)
    ranklist_column2_row2_title = tk.Label(ranklist_column2_row2, bg = text_bg, fg = text_color, font =season_size, text = 'Season-10', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column2_row2_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column2_row2_mmr = tk.Label(ranklist_column2_row2, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column2_row2_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column2_row2_icon = tk.Label(master = ranklist_column2_row2)
    ranklist_column2_row2_icon.place(width=50, height=50)

    ranklist_column2_row3 = tk.Label(ranklist_column2, bg = text_bg, bd=0)
    ranklist_column2_row3.place(rely=.73,relwidth=1, relheight = .21)
    ranklist_column2_row3_title = tk.Label(ranklist_column2_row3, bg = text_bg, fg = text_color, font =season_size, text = 'Season-11', justify = 'left', anchor='nw' ) # fg is going to need to be equal to the matching season color in data.txt
    ranklist_column2_row3_title.place(relx=.24, relwidth=1, relheight=.65)
    ranklist_column2_row3_mmr = tk.Label(ranklist_column2_row3, bg=text_bg, fg=text_color, font=mmr_size, text='2345 mmr', justify = 'left', anchor='nw')
    ranklist_column2_row3_mmr.place(relx=.24,rely=.65, relwidth=1, relheight=.35)
    ranklist_column2_row3_icon = tk.Label(master = ranklist_column2_row3)
    ranklist_column2_row3_icon.place(width=50, height=50)






    player_search = tk.Entry(searchbar, font=text_size, bg = searchbarcolor, fg = text_color, bd = 1) #my searchbar
    player_search.place(relx=.13, relwidth=0.75, relheight=1)

    select = tk.StringVar()
    select.set('PC')

    platform_choose = tk.OptionMenu(searchbar ,select, 'PC')
    platform_choose.config(bg = searchbarcolor)
    platform_choose['menu'].config(bg = searchbarcolor)
    platform_choose.config(activebackground = faintwhite_color)
    platform_choose['menu'].config(activebackground = faintwhite_color)
    platform_choose.config(fg = text_color)
    platform_choose['menu'].config(fg = text_color)
    platform_choose.config(font = ('Arial', 10))
    platform_choose['menu'].config(font = ('Arial', 10)) 
    platform_choose.place(relwidth=.13, relheight=1)

    search = tk.Button(searchbar, text="--->", font = text_size,bg = searchbarcolor,bd = 0,fg = faintwhite_color, command = lambda: searchfunc(player_search.get())) #the search button
    search.place(relx=0.84, relheight=1, relwidth=.16)


    overall_label = tk.Label(background_label, bg = outline_color, bd = 5 ) #overall stats box
    overall_label.place(relx = .02, rely = .54, relwidth = .23, relheight = .45)

    overall_column0 = tk.Label(overall_label, bg = header_bg, anchor='nw', font =header_size, fg = header_color, text = "Overall-", bd = 3) 
    overall_column0.place(relheight = .3, relwidth = 1)#Overall stats header column

    overall_column1 = tk.Label(overall_label, bg = text_bg, text = "12hr\nTime Played:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    overall_column1.place(rely = .3,relwidth =1, relheight = .2 ) #overall stats time played

    overall_column1_row2 = tk.Label(overall_column1,bg = text_bg,text = "12\nKills:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    overall_column1_row2.place(relx = .42, relwidth = .3) #overall stats kills

    overall_column1_row3 = tk.Label(overall_column1,bg = text_bg,text = "5\nDeaths:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    overall_column1_row3.place(relx = .73, relwidth = .95) #overall stats deaths

    overall_column2 = tk.Label(overall_label, bg = text_bg, anchor='nw', font =text_size, fg = text_color, text = "150\nMatches Played:", justify = 'left')
    overall_column2.place(rely = .501,relwidth =1, relheight = .2 ) #overall stats Matches played

    overall_column2_row2 = tk.Label(overall_column2,bg =text_bg,text = "50\nLosses:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    overall_column2_row2.place(relx = .42, relwidth = .3) #overall stats losses

    overall_column2_row3 = tk.Label(overall_column2,bg = text_bg,text = "15\nWins:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    overall_column2_row3.place(relx = .73, relwidth = .3) #overall stats wins

    overall_column3 = tk.Label(overall_label, bg = text_bg, anchor='nw', font =text_size, fg = text_color, text = "2\nKills/Match:", justify = 'left')
    overall_column3.place(rely = .701,relwidth =1, relheight = .3 ) #overall stats Kills per match

    overall_column3_row2 = tk.Label(overall_column3, bg = text_bg, anchor='nw', font =text_size, fg = text_color, text = "5\nK/D Ratio:", justify = 'left')
    overall_column3_row2.place(relx = .42, relwidth =.3) #overall stats K/D ratio

    overall_column3_row3 = tk.Label(overall_column3,bg = text_bg,text = "15\nW/L Ratio:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    overall_column3_row3.place(relx = .73, relwidth = .3) #overall stats win/loss ratio




    specifics_label = tk.Label(background_label, bg = outline_color, bd = 5 ) #Our specifics label parent creation
    specifics_label.place(relx = .27, rely = .54, relwidth = .33, relheight = .178)

    specifics_column0 = tk.Label(specifics_label, bg = header_bg, anchor='nw', font =smallheader_size, fg = header_color, text = "Specifics -") 
    specifics_column0.place(relheight = .31, relwidth = 1)#specifics stats header column

    specifics_column1 = tk.Label(specifics_label, bg = text_bg, anchor='nw', font =text_size, fg = text_color, text = "124\nKill Assists:", justify = 'left') 
    specifics_column1.place(rely = .3,relheight = .36, relwidth = 1)#specifics stats Kill Assists

    specifics_column1_row2 = tk.Label(specifics_column1,bg = text_bg,text = "15\nMelee Kills:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    specifics_column1_row2.place(relx = .25, relwidth = .2) #specifics stats melee Kills
    
    specifics_column1_row3 = tk.Label(specifics_column1,bg = text_bg,text = "21\nRevives:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    specifics_column1_row3.place(relx = .55, relwidth = .2) #specifics stats revives

    specifics_column1_row4 = tk.Label(specifics_column1,bg = text_bg,text = "85\nWall Bangs:", anchor = 'nw', font = text_size, fg = text_color, justify = 'left' )
    specifics_column1_row4.place(relx = .8, relwidth = .2) #specifics stats Penetration Kills

    specifics_column2 = tk.Label(specifics_label, bg = text_bg, anchor='nw', font =text_size, fg = text_color, text = "200\nBlind Kills", justify = 'left')
    specifics_column2.place(rely = .66,relheight = .36, relwidth = 1) #specifics stats blind kills

    specifics_column2_row2 = tk.Label(specifics_column2,bg = text_bg,text = "10\nSuicides", anchor = 'nw', font = text_size, fg = text_color, justify = 'left')
    specifics_column2_row2.place(relx = .25, relwidth = .2) #specifics stats suicides

    specifics_column2_row3 = tk.Label(specifics_column2,bg = text_bg,text = "5\nBarricades Deployed", anchor = 'nw', font = ('Comic Sans MS', 12), fg = text_color, justify = 'left')
    specifics_column2_row3.place(relx = .55, relwidth = .2) #specifics stats barricades deployed

    specifics_column2_row4 = tk.Label(specifics_column2,bg = text_bg,text = "12\nGadgets Destroyed", anchor = 'nw', font = ('Comic Sans MS', 12), fg = text_color, justify = 'left')
    specifics_column2_row4.place(relx = .8, relwidth = .2) #Gadgets destroyed

    

    Cerealrating_title = tk.Label(player_card, bg = header_bg, fg = header_color, anchor = 'nw', justify = 'left', font = smallheader_size, text = 'Cereal Sweat Rating-')
    Cerealrating_title.place(relx = .4, rely=.05,relwidth = 1, relheight =1)

    Cerealrating_text = tk.Label(player_card, bg = header_bg, fg = text_color, anchor = 'n', justify = 'center', font = ('Comic Sans MS', 26))
    Cerealrating_text.place(relx = .58, relheight = .4, rely = .3, relwidth = .4) 

    Cerealrating_desc = tk.Label(player_card, bg = header_bg, fg = text_color, anchor = 'n', justify = 'center', font = text_size)
    Cerealrating_desc.place(relx = .58, relheight = .4, rely = .53, relwidth = .4) 

    emojii_label = tk.Label(master =player_card, bg = header_bg)
    emojii_label.place(relx = .4, height = 150, width = 200, rely = .25) #For the other emojiis they need to be png, width = 200, height = 150, and placed at the same location

    


    casual_label = tk.Label(background_label, bg = outline_color, bd = 5) # The Casual Label parent
    casual_label.place(relx = .615,rely = .54, relwidth = .165, relheight = .45)

    casual_column0 = tk.Label(casual_label, bg = header_bg, fg = header_color, anchor = 'nw', justify = 'left', font = header_size, text = 'Casual-') # THe Casual Title
    casual_column0.place(relwidth = 1, relheight = .25)

    casual_column1 = tk.Label(casual_label, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '20h\nTime Played:' ) #Casual TimePlayed
    casual_column1.place(rely = .25, relwidth = .5, relheight = .75)

    casual_column1_row2 = tk.Label(casual_column1, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '200\nKills') #Casual Kills
    casual_column1_row2.place(rely = .24, relwidth = 1, relheight = .1875)

    casual_column1_row3 = tk.Label(casual_column1, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '50\nDeaths') #Casual Deaths
    casual_column1_row3.place(rely = .48, relwidth = 1, relheight = .1875)

    casual_column1_row4 = tk.Label(casual_column1, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '2.75\nK/D') #Casual K/D
    casual_column1_row4.place(rely = .72, relwidth = 1, relheight = .1875)

    casual_column2 = tk.Label(casual_label, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '800\nMatches Played:' ) #Casual Matches Played
    casual_column2.place(rely = .25,relx = .5, relwidth = .5, relheight = .75)

    casual_column2_row2 = tk.Label(casual_column2, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '20\nMatches Won:') #Casual Matches won
    casual_column2_row2.place(rely = .24, relwidth = 1, relheight = .1875)

    casual_column2_row3 = tk.Label(casual_column2, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '780\nMatches Lost') #Casual Matches Lost
    casual_column2_row3.place(rely = .48, relwidth = 1, relheight = .1875)

    casual_column2_row4 = tk.Label(casual_column2, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '75%\nWin/Loss') #Casual Win/ Loss
    casual_column2_row4.place(rely = .72, relwidth = 1, relheight = .1875)



    ranked_label = tk.Label(background_label, bg = outline_color, bd =5)
    ranked_label.place(relx = .815, rely = .54, relwidth = .165, relheight = .45)

    ranked_column0 = tk.Label(ranked_label, bg = header_bg, fg = header_color, anchor = 'nw', justify = 'left', font = header_size, text = 'Ranked-') # THe Casual Title
    ranked_column0.place(relwidth = 1, relheight = .25)

    ranked_column1 = tk.Label(ranked_label, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '50h\nTime Played:' ) #ranked TimePlayed
    ranked_column1.place(rely = .25, relwidth = .5, relheight = .75)

    ranked_column1_row2 = tk.Label(ranked_column1, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '21\nKills') #ranked Kills
    ranked_column1_row2.place(rely = .24, relwidth = 1, relheight = .1875)

    ranked_column1_row3 = tk.Label(ranked_column1, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '80\nDeaths') #ranked Deaths
    ranked_column1_row3.place(rely = .48, relwidth = 1, relheight = .1875)

    ranked_column1_row4 = tk.Label(ranked_column1, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '0.5\nK/D') #ranked K/D
    ranked_column1_row4.place(rely = .72, relwidth = 1, relheight = .1875)

    ranked_column2 = tk.Label(ranked_label, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '300\nMatches Played:' ) #ranked Matches Played
    ranked_column2.place(rely = .25,relx = .5, relwidth = .5, relheight = .75)

    ranked_column2_row2 = tk.Label(ranked_column2, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '150\nMatches Won:') #ranked Matches won
    ranked_column2_row2.place(rely = .24, relwidth = 1, relheight = .1875)

    ranked_column2_row3 = tk.Label(ranked_column2, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '150\nMatches Lost') #ranked Matches Lost
    ranked_column2_row3.place(rely = .48, relwidth = 1, relheight = .1875)

    ranked_column2_row4 = tk.Label(ranked_column2, bg = text_bg, fg = text_color, anchor = 'nw', justify = 'left', font = text_size, text = '50%\nWin/Loss') #ranked Win/ Loss
    ranked_column2_row4.place(rely = .72, relwidth = 1, relheight = .1875)


    

    blankwrite()

    root2.mainloop()



if __name__ == "__main__":
    rainbow_func()
