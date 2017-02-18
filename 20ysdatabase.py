#20 years of records
#WELCOME
def welcome():
    print("------------------------------------------------------------------------------------------------------------\n")
    print("This small program is a sort of record-database of the last 20 years about different sports and competitions")
    print("You can find informations just typing here the name of the sport you're interested in")
    print("After this, you will be redirected into the main page of the sport you have chosen")
    print("You will be able then to see the different competitions of that sport, and to navigate between them")
    print("------------------------------------------------------------------------------------------------------------\n")
def choice():
    user_choice=input("Type here the sport you want to look for. E.g. 'football' or 'tennis'...")
    if user_choice=="football":
        football()
    else:
        print("The sport you're looking for is not available now. Try again!")
        return choice()
    
#Football
class Football:
    ligue_name = ""
    ligue_year = ""
    ligue_winner = ""
    ligue_top_scorers = ""
    def show_league(self):
        print("===============================================================================================================================================")
        print("[Ligue name]: "+self.ligue_name)
        print("[Ligue year]: "+self.ligue_year)
        print("[Ligue winner]: "+self.ligue_winner)
        print("[Ligue top scorers]:\n"+"\n".join(list(self.ligue_top_scorers)))
        print("================================================================================================================================================")

def football(): #Aka "Football-database"
    print("----------------------------------------------\n")
    print("Welcome in the football-database!!")
    print("You can look for:")
    print("(1)English Premier League last 20s;")
    print("(2)Italian Serie A last 20s;")
    print("(3)French Ligue 1 last 20s;")
    print("(4)German Bundesliga 1 last 20s;")
    print("(5)Spanish LaLiga last 20s;")
    print("(6)Uefa Champions League last 20s;")
    print("(7)Europa League last 20s;")
    print("(8)Home")
    print("----------------------------------------------\n")
    def func_choice():
        football_choice=input("Type here the name of the competition you're interested in, by typing its index number. E.g. '1' is Premier League\n...")
        if football_choice=="1":
            def premier_database():
                print("------------------------------------------------\n")
                print("This is the Premier League database:")
                print("You can now look for:")
                print("(1997)Premier League")
                print("(1998)Premier League")
                print("(1999)Premier League")
                print("(2000)Premier League")
                print("(2001)Premier League")
                print("(2002)Premier League")
                print("(2003)Premier League")
                print("(2004)Premier League")
                print("(2005)Premier League")
                print("(2006)Premier League")
                print("(2007)Premier League")
                print("(2008)Premier League")
                print("(2009)Premier League")
                print("(2010)Premier League")
                print("(2011)Premier League")
                print("(2012)Premier League")
                print("(2013)Premier League")
                print("(2014)Premier League")
                print("(2015)Premier League")
                print("(2016)Premier League")
                print("----------------------------------------------\n")
            def func_premier_choice():
                premier_choice=input("You can choose here the year of the competition, to look for its stats. E.g.'2001'opens 2001 Premier League stats; press 'b' to go back\n...")
                def back_to_prdata():
                    input("Press any button to go back...")
                    return func_premier_choice()
                if premier_choice=="1997":
                    PremierLeague1997.show_league()
                    back_to_prdata()
                elif premier_choice=="1998":
                    PremierLeague1998.show_league()
                    back_to_prdata()
                elif premier_choice=="1999":
                    PremierLeague1999.show_league()
                    back_to_prdata()
                elif premier_choice=="2000":
                    PremierLeague2000.show_league()
                    back_to_prdata()
                elif premier_choice=="2001":
                    PremierLeague2001.show_league()
                    back_to_prdata()
                elif premier_choice=="2002":
                    PremierLeague2002.show_league()
                    back_to_prdata()
                elif premier_choice=="2003":
                    PremierLeague2003.show_league()
                    back_to_prdata()
                elif premier_choice=="2004":
                    PremierLeague2004.show_league()
                    back_to_prdata()
                elif premier_choice=="2005":
                    PremierLeague2005.show_league()
                    back_to_prdata()
                elif premier_choice=="2006":
                    PremierLeague2006.show_league()
                    back_to_prdata()
                elif premier_choice=="2007":
                    PremierLeague2007.show_league()
                    back_to_prdata()
                elif premier_choice=="2008":
                    PremierLeague2008.show_league()
                    back_to_prdata()
                elif premier_choice=="2009":
                    PremierLeague2009.show_league()
                    back_to_prdata()
                elif premier_choice=="2010":
                    PremierLeague2010.show_league()
                    back_to_prdata()
                elif premier_choice=="2011":
                    PremierLeague2011.show_league()
                    back_to_prdata()
                elif premier_choice=="2012":
                    PremierLeague2012.show_league()
                    back_to_prdata()
                elif premier_choice=="2013":
                    PremierLeague2013.show_league()
                    back_to_prdata()
                elif premier_choice=="2014":
                    PremierLeague2014.show_league()
                    back_to_prdata()
                elif premier_choice=="2015":
                    PremierLeague2015.show_league()
                    back_to_prdata()
                elif premier_choice=="2016":
                    PremierLeague2016.show_league()
                    back_to_prdata()
                elif premier_choice=="b":
                    return football()
                else:
                    print("The value is not correct. Try again with a valid value")
                    return func_premier_choice()
            premier_database()
            func_premier_choice()
        elif football_choice=="2":
            def seriea_database():
                print("------------------------------------------------\n")
                print("This is the Serie A database:")
                print("You can now look for:")
                print("(1997)Serie A")
                print("(1998)Serie A")
                print("(1999)Serie A")
                print("(2000)Serie A")
                print("(2001)Serie A")
                print("(2002)Serie A")
                print("(2003)Serie A")
                print("(2004)Serie A")
                print("(2005)Serie A")
                print("(2006)Serie A")
                print("(2007)Serie A")
                print("(2008)Serie A")
                print("(2009)Serie A")
                print("(2010)Serie A")
                print("(2011)Serie A")
                print("(2012)Serie A")
                print("(2013)Serie A")
                print("(2014)Serie A")
                print("(2015)Serie A")
                print("(2016)Serie A")
                print("----------------------------------------------\n")
            def func_seriea_choice():
                seriea_choice=input("You can choose here the year of the competition, to look for its stats. E.g.'2001'opens 2001 Serie A stats; press 'b' to go back\n...")
                def back_to_serieadata():
                    input("Press a button to go back")
                    return func_seriea_choice()
                if seriea_choice=="1997":
                    SerieA1997.show_league()
                    back_to_serieadata()
                elif seriea_choice=="1998":
                    SerieA1998.show_league()
                    back_to_serieadata()
                elif seriea_choice=="1999":
                    SerieA1999.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2000":
                    SerieA2000.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2001":
                    SerieA2001.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2002":
                    SerieA2002.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2003":
                    SerieA2003.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2004":
                    SerieA2004.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2005":
                    SerieA2005.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2006":
                    SerieA2006.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2007":
                    SerieA2007.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2008":
                    SerieA2008.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2009":
                    SerieA2009.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2010":
                    SerieA2010.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2011":
                    SerieA2011.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2012":
                    SerieA2012.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2013":
                    SerieA2013.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2014":
                    SerieA2014.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2015":
                    SerieA2015.show_league()
                    back_to_serieadata()
                elif seriea_choice=="2016":
                    Serie2016.show_league()
                    back_to_serieadata()
                elif seriea_choice=="b":
                    return football()
                else:
                    print("The value is not correct. Try again with a valid value")
                    return func_seriea_choice()
            seriea_database()
            func_seriea_choice()
        elif football_choice=="3":
            def ligue1_database():
                print("------------------------------------------------\n")
                print("This is the Ligue 1 database:")
                print("You can now look for:")
                print("(1997)Ligue 1")
                print("(1998)Ligue 1")
                print("(1999)Ligue 1")
                print("(2000)Ligue 1")
                print("(2001)Ligue 1")
                print("(2002)Ligue 1")
                print("(2003)Ligue 1")
                print("(2004)Ligue 1")
                print("(2005)Ligue 1")
                print("(2006)Ligue 1")
                print("(2007)Ligue 1")
                print("(2008)Ligue 1")
                print("(2009)Ligue 1")
                print("(2010)Ligue 1")
                print("(2011)Ligue 1")
                print("(2012)Ligue 1")
                print("(2013)Ligue 1")
                print("(2014)Ligue 1")
                print("(2015)Ligue 1")
                print("(2016)Ligue 1")
                print("----------------------------------------------\n")
            def func_ligue1_choice():
                ligue1_choice=input("You can choose here the year of the competition, to look for its stats. E.g.'2001'opens 2001 Ligue 1 stats; press 'b' to go back\n...")
                def back_to_ligue1data():
                    input("Press a button to go back")
                    return ligue1_database()
                if ligue1_choice=="1997":
                    Ligue1_1997.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="1998":
                    Ligue1_1998.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="1999":
                    Ligue1_1999.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2000":
                    Ligue1_2000.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2001":
                    Ligue1_2001.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2002":
                    Ligue1_2002.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2003":
                    Ligue1_2003.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2004":
                    Ligue1_2004.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2005":
                    Ligue1_2005.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2006":
                    Ligue1_2006.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2007":
                    Ligue1_2007.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2008":
                    Ligue1_2008.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2009":
                    Ligue1_2009.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2010":
                    Ligue1_2010.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2011":
                    Ligue1_2011.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2012":
                    Ligue1_2012.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2013":
                    Ligue1_2013.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2014":
                    Ligue1_2014.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2015":
                    Ligue1_2015.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="2016":
                    Ligue1_2016.show_league()
                    back_to_ligue1data()
                elif ligue1_choice=="b":
                    return football()
                else:
                    print("The value is not correct. Try again with a valid value")
                    return func_ligue1_choice()
            ligue1_database()
            func_ligue1_choice()
        elif football_choice=="4":
            def bundesliga_database():
                print("------------------------------------------------\n")
                print("This is the Bundesliga database:")
                print("You can now look for:")
                print("(1997)Bundesliga")
                print("(1998)Bundesliga")
                print("(1999)Bundesliga")
                print("(2000)Bundesliga")
                print("(2001)Bundesliga")
                print("(2002)Bundesliga")
                print("(2003)Bundesliga")
                print("(2004)Bundesliga")
                print("(2005)Bundesliga")
                print("(2006)Bundesliga")
                print("(2007)Bundesliga")
                print("(2008)Bundesliga")
                print("(2009)Bundesliga")
                print("(2010)Bundesliga")
                print("(2011)Bundesliga")
                print("(2012)Bundesliga")
                print("(2013)Bundesliga")
                print("(2014)Bundesliga")
                print("(2015)Bundesliga")
                print("(2016)Bundesliga")
                print("----------------------------------------------\n")
            def func_bundes_choice():
                bundes_choice=input("You can choose here the year of the competition, to look for its stats. E.g.'2001'opens 2001 Bundesliga stats; press 'b' to go back\n...")
                def back_bundesdata():
                    input("Press any button to go back...")
                    return func_bundes_choice()
                if bundes_choice=="1997":
                    Bundesliga_1997.show_league()
                    back_bundesdata()
                elif bundes_choice=="1998":
                    Bundesliga_1998.show_league()
                    back_bundesdata()
                elif bundes_choice=="1999":
                    Bundesliga_1999.show_league()
                    back_bundesdata()
                elif bundes_choice=="2000":
                    Bundesliga_2000.show_league()
                    back_bundesdata()
                elif bundes_choice=="2001":
                    Bundesliga_2001.show_league()
                    back_bundesdata()
                elif bundes_choice=="2002":
                    Bundesliga_2002.show_league()
                    back_bundesdata()
                elif bundes_choice=="2003":
                    Bundesliga_2003.show_league()
                    back_bundesdata()
                elif bundes_choice=="2004":
                    Bundesliga_2004.show_league()
                    back_bundesdata()
                elif bundes_choice=="2005":
                    Bundesliga_2005.show_league()
                    back_bundesdata()
                elif bundes_choice=="2006":
                    Bundesliga_2006.show_league()
                    back_bundesdata()
                elif bundes_choice=="2007":
                    Bundesliga_2007.show_league()
                    back_bundesdata()
                elif bundes_choice=="2008":
                    Bundesliga_2008.show_league()
                    back_bundesdata()
                elif bundes_choice=="2009":
                    Bundesliga_2009.show_league()
                    back_bundesdata()
                elif bundes_choice=="2010":
                    Bundesliga_2010.show_league()
                    back_bundesdata()
                elif bundes_choice=="2011":
                    Bundesliga_2011.show_league()
                    back_bundesdata()
                elif bundes_choice=="2012":
                    Bundesliga_2012.show_league()
                    back_bundesdata()
                elif bundes_choice=="2013":
                    Bundesliga_2013.show_league()
                    back_bundesdata()
                elif bundes_choice=="2014":
                    Bundesliga_2014.show_league()
                    back_bundesdata()
                elif bundes_choice=="2015":
                    Bundesliga_2015.show_league()
                    back_bundesdata()
                elif bundes_choice=="2016":
                    Bundesliga_2016.show_league()
                    back_bundesdata()
                elif bundes_choice=="b":
                    return football()
                else:
                    print("The value is not correct. Try again with a valid value")
                    return func_bundes_choice()
            bundesliga_database()
            func_bundes_choice()
        elif football_choice=="5":
            def laliga_database():
                print("------------------------------------------------\n")
                print("This is the LaLiga database:")
                print("You can now look for:")
                print("(1997)LaLiga")
                print("(1998)LaLiga")
                print("(1999)LaLiga")
                print("(2000)LaLiga")
                print("(2001)LaLiga")
                print("(2002)LaLiga")
                print("(2003)LaLiga")
                print("(2004)LaLiga")
                print("(2005)LaLiga")
                print("(2006)LaLiga")
                print("(2007)LaLiga")
                print("(2008)LaLiga")
                print("(2009)LaLiga")
                print("(2010)LaLiga")
                print("(2011)LaLiga")
                print("(2012)LaLiga")
                print("(2013)LaLiga")
                print("(2014)LaLiga")
                print("(2015)LaLiga")
                print("(2016)LaLiga")
                print("----------------------------------------------\n")
            def func_laliga_choice():
                laliga_choice=input("You can choose here the year of the competition, to look for its stats. E.g.'2001'opens 2001 LaLiga stats; press 'b' to go back\n...")
                def back_to_laligadata():
                    input("Press a button to go back")
                    return func_laliga_choice()
                if laliga_choice=="1997":
                    LaLiga_1997.show_league()
                    back_to_laligadata()
                elif laliga_choice=="1998":
                    LaLiga_1998.show_league()
                    back_to_laligadata()
                elif laliga_choice=="1999":
                    LaLiga_1999.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2000":
                    LaLiga_2000.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2001":
                    LaLiga_2001.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2002":
                    LaLiga_2002.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2003":
                    LaLiga_2003.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2004":
                    LaLiga_2004.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2005":
                    LaLiga_2005.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2006":
                    LaLiga_2006.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2007":
                    LaLiga_2007.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2008":
                    LaLiga_2008.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2009":
                    LaLiga_2009.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2010":
                    LaLiga_2010.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2011":
                    LaLiga_2011.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2012":
                    LaLiga_2012.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2013":
                    LaLiga_2013.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2014":
                    LaLiga_2014.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2015":
                    LaLiga_2015.show_league()
                    back_to_laligadata()
                elif laliga_choice=="2016":
                    LaLiga_2016.show_league()
                    back_to_laligadata()
                elif laliga_choice=="b":
                    return football()
                else:
                    print("The value is not correct. Try again with a valid value")
                    return func_laliga_choice()
            laliga_database()
            func_laliga_choice()
        elif football_choice=="6":
            def ucl_database():
                print("------------------------------------------------\n")
                print("This is the UEFA Champions League database:")
                print("You can now look for:")
                print("(1997)UEFA Champions League")
                print("(1998)UEFA Champions League")
                print("(1999)UEFA Champions League")
                print("(2000)UEFA Champions League")
                print("(2001)UEFA Champions League")
                print("(2002)UEFA Champions League")
                print("(2003)UEFA Champions League")
                print("(2004)UEFA Champions League")
                print("(2005)UEFA Champions League")
                print("(2006)UEFA Champions League")
                print("(2007)UEFA Champions League")
                print("(2008)UEFA Champions League")
                print("(2009)UEFA Champions League")
                print("(2010)UEFA Champions League")
                print("(2011)UEFA Champions League")
                print("(2012)UEFA Champions League")
                print("(2013)UEFA Champions League")
                print("(2014)UEFA Champions League")
                print("(2015)UEFA Champions League")
                print("(2016)UEFA Champions League")
                print("----------------------------------------------\n")
            def func_ucl_choice():
                ucl_choice=input("You can choose here the year of the competition, to look for its stats. E.g.'2001'opens 2001 UEFA Champions League stats; press 'b' to go back\n...")
                def back_to_ucldata():
                    input("Press a button to go back")
                    return func_ucl_choice()
                if ucl_choice=="1997":
                    UCL_1997.show_league()
                    back_to_ucldata()
                elif ucl_choice=="1998":
                    UCL_1998.show_league()
                    back_to_ucldata()
                elif ucl_choice=="1999":
                    UCL_1999.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2000":
                    UCL_2000.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2001":
                    UCL_2001.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2002":
                    UCL_2002.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2003":
                    UCL_2003.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2004":
                    UCL_2004.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2005":
                    UCL_2005.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2006":
                    UCL_2006.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2007":
                    UCL_2007.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2008":
                    UCL_2008.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2009":
                    UCL_2009.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2010":
                    UCL_2010.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2011":
                    UCL_2011.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2012":
                    UCL_2012.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2013":
                    UCL_2013.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2014":
                    UCL_2014.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2015":
                    UCL_2015.show_league()
                    back_to_ucldata()
                elif ucl_choice=="2016":
                    UCL_2016.show_league()
                    back_to_ucldata()
                elif ucl_choice=="b":
                    return football()
                else:
                    print("The value is not correct. Try again with a valid value")
                    return func_ucl_choice()
            ucl_database()
            func_ucl_choice()
        elif football_choice=="7":
            def uel_database():
                print("------------------------------------------------\n")
                print("This is the UEFA Europa League database:")
                print("You can now look for:")
                print("(1997)UEFA Europa League")
                print("(1998)UEFA Europa League")
                print("(1999)UEFA Europa League")
                print("(2000)UEFA Europa League")
                print("(2001)UEFA Europa League")
                print("(2002)UEFA Europa League")
                print("(2003)UEFA Europa League")
                print("(2004)UEFA Europa League")
                print("(2005)UEFA Europa League")
                print("(2006)UEFA Europa League")
                print("(2007)UEFA Europa League")
                print("(2008)UEFA Europa League")
                print("(2009)UEFA Europa League")
                print("(2010)UEFA Europa League")
                print("(2011)UEFA Europa League")
                print("(2012)UEFA Europa League")
                print("(2013)UEFA Europa League")
                print("(2014)UEFA Europa League")
                print("(2015)UEFA Europa League")
                print("(2016)UEFA Europa League")
                print("----------------------------------------------\n")
            def func_uel_choice():
                uel_choice=input("You can choose here the year of the competition, to look for its stats. E.g.'2001'opens 2001 UEFA Europa League stats; press 'b' to go back\n...")
                def back_to_ueldata():
                    input("Press a button to go back")
                    return func_uel_choice()
                if uel_choice=="1997":
                    UEL_1997.show_league()
                    back_to_ueldata()
                elif uel_choice=="1998":
                    UEL_1998.show_league()
                    back_to_ueldata()
                elif uel_choice=="1999":
                    UEL_1999.show_league()
                    back_to_ueldata()
                elif uel_choice=="2000":
                    UEL_2000.show_league()
                    back_to_ueldata()
                elif uel_choice=="2001":
                    UEL_2001.show_league()
                    back_to_ueldata()
                elif uel_choice=="2002":
                    UEL_2002.show_league()
                    back_to_ueldata()
                elif uel_choice=="2003":
                    UEL_2003.show_league()
                    back_to_ueldata()
                elif uel_choice=="2004":
                    UEL_2004.show_league()
                    back_to_ueldata()
                elif uel_choice=="2005":
                    UEL_2005.show_league()
                    back_to_ueldata()
                elif uel_choice=="2006":
                    UEL_2006.show_league()
                    back_to_ueldata()
                elif uel_choice=="2007":
                    UEL_2007.show_league()
                    back_to_ueldata()
                elif uel_choice=="2008":
                    UEL_2008.show_league()
                    back_to_ueldata()
                elif uel_choice=="2009":
                    UEL_2009.show_league()
                    back_to_ueldata()
                elif uel_choice=="2010":
                    UEL_2010.show_league()
                    back_to_ueldata()
                elif uel_choice=="2011":
                    UEL_2011.show_league()
                    back_to_ueldata()
                elif uel_choice=="2012":
                    UEL_2012.show_league()
                    back_to_ueldata()
                elif uel_choice=="2013":
                    UEL_2013.show_league()
                    back_to_ueldata()
                elif uel_choice=="2014":
                    UEL_2014.show_league()
                    back_to_ueldata()
                elif uel_choice=="2015":
                    UEL_2015.show_league()
                    back_to_ueldata()
                elif uel_choice=="2016":
                    UEL_2016.show_league()
                    back_to_ueldata()
                elif uel_choice=="b":
                    return football()
                else:
                    print("The value is not correct. Try again with a valid value")
                    return func_uel_choice()
            uel_database()
            func_uel_choice()
        elif football_choice=="8":
            return choice()
        else:
            print("The value is not correct. Try again!")
            return func_choice()
    func_choice()

#Premier League Stats
PremierLeague1997 = Football()
PremierLeague1997.ligue_name = "Premier League - English Football League"
PremierLeague1997.ligue_year = "1997"
PremierLeague1997.ligue_winner = "Arsenal"
PremierLeague1997.ligue_top_scorers = ["(1) Dion Dublin(Coventry City), 18 goals","(2) Chris Sutton(Blackburn), 18 goals","(3) Michael Owen(Liverpool), 18 goals"]
PremierLeague1998 = Football()
PremierLeague1998.ligue_name = "Premier League - English Football League"
PremierLeague1998.ligue_year = "1998"
PremierLeague1998.ligue_winner = "Manchester Utd"
PremierLeague1998.ligue_top_scorers = ["(1) Jimmy Floyd Hasselbaink(Leeds United), 18 goals","(2) Michael Owen(Newcastle Utd), 18 goals","(3) Dwight Yorke(Manchester Utd), 18 goals"]
PremierLeague1999 = Football()
PremierLeague1999.ligue_name = "Premier League - English Football League"
PremierLeague1999.ligue_year = "1999"
PremierLeague1999.ligue_winner = "Manchester Utd"
PremierLeague1999.ligue_top_scorers = ["(1) Kevin Phillips(Sunderland), 30 goals","(2) Alan Shearer(Newcastle Utd), 23 goals","(3) Dwight Yorke(Manchester Utd), 20 goals"]
PremierLeague2000 = Football()
PremierLeague2000.ligue_name = "Premier League - English Football League"
PremierLeague2000.ligue_year = "2000"
PremierLeague2000.ligue_winner = "Manchester Utd"
PremierLeague2000.ligue_top_scorers = ["(1) Jimmy Floyd Hasselbaink(Chelsea), 23 goals","(2)Marcus Stewart(Ipswich Town), 19 goals","(3) Thierry Henry(Arsenal), 17 goals"]
PremierLeague2001 = Football()
PremierLeague2001.ligue_name = "Premier League - English Football League"
PremierLeague2001.ligue_year = "2001"
PremierLeague2001.ligue_winner = "Arsenal"
PremierLeague2001.ligue_top_scorers = ["(1) Thierry Henry(Arsenal), 24 goals","(2) Jimmy Floyd Hasselbaink(Chelsea), 23 goals","(3) Alan Shearer(Newcastle Utd), 23 goals"]
PremierLeague2002 = Football()
PremierLeague2002.ligue_name = "Premier League - English Football League"
PremierLeague2002.ligue_year = "2002"
PremierLeague2002.ligue_winner = "Manchester Utd"
PremierLeague2002.ligue_top_scorers = ["(1) Ruud van Nistelrooy(Manchester Utd), 25 goals","(2) Thierry Henry(Arsenal), 24 goals","(3) James Beattie(Southampton), 23 goals"]
PremierLeague2003 = Football()
PremierLeague2003.ligue_name = "Premier League - English Football League"
PremierLeague2003.ligue_year = "2003"
PremierLeague2003.ligue_winner = "Arsenal"
PremierLeague2003.ligue_top_scorers = ["(1) Thierry Henry(Arsenal), 30 goals","(2) Alan Shearer(Newcastle Utd), 22 goals","(3) Ruud van Nistelrooy(Manchester Utd), 20 goals"]
PremierLeague2004 = Football()
PremierLeague2004.ligue_name = "Premier League - English Football League"
PremierLeague2004.ligue_year = "2004"
PremierLeague2004.ligue_winner = "Chelsea"
PremierLeague2004.ligue_top_scorers = ["(1) Thierry Henry(Arsenal), 25 goals","(2) Andy Johnson(Crystal Palace), 21 goals","(3) Robert Pires(Arsenal), 14 goals"]
PremierLeague2005 = Football()
PremierLeague2005.ligue_name = "Premier League - English Football League"
PremierLeague2005.ligue_year = "2005"
PremierLeague2005.ligue_winner = "Chelsea"
PremierLeague2005.ligue_top_scorers = ["(1) Thierry Henry(Arsenal), 27 goals","(2) Ruud van Nistelrooy(Manchester Utd), 21 goals","(3) Darren Bent(Charlton), 18 goals"]
PremierLeague2006 = Football()
PremierLeague2006.ligue_name = "Premier League - English Football League"
PremierLeague2006.ligue_year = "2006"
PremierLeague2006.ligue_winner = "Manchester Utd"
PremierLeague2006.ligue_top_scorers = ["(1) Didier Drogba(Chelsea), 20 goals","(2) Benni McCarthy(Blackburn), 18 goals","(3) Cristiano Ronaldo(Manchester Utd), 17 goals"]
PremierLeague2007 = Football()
PremierLeague2007.ligue_name = "Premier League - English Football League"
PremierLeague2007.ligue_year = "2007"
PremierLeague2007.ligue_winner = "Manchester Utd"
PremierLeague2007.ligue_top_scorers = ["(1) Cristiano Ronaldo(Manchester Utd), 31 goals","(2) Emmanuel Adebayor(Arsenal), 24 goals","(3) Fernando Torres(Liverpool), 24 goals"]
PremierLeague2008 = Football()
PremierLeague2008.ligue_name = "Premier League - English Football League"
PremierLeague2008.ligue_year = "2008"
PremierLeague2008.ligue_winner = "Manchester Utd"
PremierLeague2008.ligue_top_scorers = ["(1) Nicolas Anelka(Chelsea), 19 goals","(2) Cristiano Ronaldo(Manchester Utd), 18 goals","(3) Steven Gerrard(Liverpool), 16 goals"]
PremierLeague2009 = Football()
PremierLeague2009.ligue_name = "Premier League - English Football League"
PremierLeague2009.ligue_year = "2009"
PremierLeague2009.ligue_winner = "Chelsea"
PremierLeague2009.ligue_top_scorers = ["(1) Didier Drogba(Chelsea), 29 goals","(2) Wayne Rooney (Manchester Utd), 26 goals","(3) Darren Bent(Sunderland), 24 goals"]
PremierLeague2010 = Football()
PremierLeague2010.ligue_name = "Premier League - English Football League"
PremierLeague2010.ligue_year = "2010"
PremierLeague2010.ligue_winner = "Manchester Utd"
PremierLeague2010.ligue_top_scorers = ["(1) Dimitar Berbatov(Manchester Utd), 21 goals","(2) Carlos Tevez(Manchester City), 21 goals","(3) Robin van Persie(Arsenal), 18 goals"]
PremierLeague2011 = Football()
PremierLeague2011.ligue_name = "Premier League - English Football League"
PremierLeague2011.ligue_year = "2011"
PremierLeague2011.ligue_winner = "Manchester City"
PremierLeague2011.ligue_top_scorers = ["(1) Robin van Persie(Arsenal), 30 goals","(2) Wayne Rooney(Manchester Utd), 27 goals","(3) Sergio Aguero(Manchester City), 23 goals"]
PremierLeague2012 = Football()
PremierLeague2012.ligue_name = "Premier League - English Football League"
PremierLeague2012.ligue_year = "2012"
PremierLeague2012.ligue_winner = "Manchester Utd"
PremierLeague2012.ligue_top_scorers = ["(1) Robin van Persie(Manchester Utd), 26 goals","(2) Luis Suarez(Liverpool), 23 goals","(3) Gareth Bale(Tottenham), 21 goals"]
PremierLeague2013 = Football()
PremierLeague2013.ligue_name = "Premier League - English Football League"
PremierLeague2013.ligue_year = "2013"
PremierLeague2013.ligue_winner = "Manchester City"
PremierLeague2013.ligue_top_scorers = ["(1) Luis Suarez(Livepool), 31 goals","(2) Daniel Sturridge(Liverpool), 22 goals","(3) Yaya Touré(Manchester City), 20 goals"]
PremierLeague2014 = Football()
PremierLeague2014.ligue_name = "Premier League - English Football League"
PremierLeague2014.ligue_year = "2014"
PremierLeague2014.ligue_winner = "Chelsea"
PremierLeague2014.ligue_top_scorers = ["(1) Sergio Aguero(Manchester City), 26 goals","(2) Harry Kane(Tottenham), 21 goals","(3) Diego Costa(Chelsea), 20 goals"]
PremierLeague2015 = Football()
PremierLeague2015.ligue_name = "Premier League - English Football League"
PremierLeague2015.ligue_year = "2015"
PremierLeague2015.ligue_winner = "Leicester City"
PremierLeague2015.ligue_top_scorers = ["(1) Harry Kane(Tottenham), 25 goals","(2) Sergio Aguero(Manchester City), 24 goals","(3) Jamie Vardy(Leicester City), 24 goals"]
PremierLeague2016 = Football()
PremierLeague2016.ligue_name = "Premier League - English Football League"
PremierLeague2016.ligue_year = "2016"
PremierLeague2016.ligue_winner = "N.D."
PremierLeague2016.ligue_top_scorers = "N.D."
#Serie A Stats:
SerieA1997 = Football()
SerieA1997.ligue_name = "Serie A - Italian Football League"
SerieA1997.ligue_year = "1997"
SerieA1997.ligue_winner = "Juventus"
SerieA1997.ligue_top_scorers = ["(1) Oliver Bierhoff(Udinese), 27 goals","(2) Ronaldo(Inter), 25 goals","(3) Roberto Baggio(Bologna), 22 goals"]
SerieA1998 = Football()
SerieA1998.ligue_name = "Serie A - Italian Football League"
SerieA1998.ligue_year = "1998"
SerieA1998.ligue_winner = "Milan"
SerieA1998.ligue_top_scorers = ["(1) Marcio Amoroso(Udinese), 22 goals","(2) Gabriel Batistuta(Fiorentina), 21 goals","(3) Oliver Bierhoff(Milan), 19 goals"]
SerieA1999 = Football()
SerieA1999.ligue_name = "Serie A - Italian Football League"
SerieA1999.ligue_year = "1999"
SerieA1999.ligue_winner = "Lazio"
SerieA1999.ligue_top_scorers = ["(1) Andrij Shevchenko(Milan), 24 goals","(2) Gabriel Batistuta(Fiorentina), 23 goals","(3) Hernan Crespo(Parma), 22 goals"]
SerieA2000 = Football()
SerieA2000.ligue_name = "Serie A - Italian Football League"
SerieA2000.ligue_year = "2000"
SerieA2000.ligue_winner = "Roma"
SerieA2000.ligue_top_scorers = ["(1) Hernan Crespo(Lazio), 26 goals","(2) Andrij Shevchenko(Milan), 24 goals","(3) Enrico Chiesa(Fiorentina), 22 goals"]
SerieA2001 = Football()
SerieA2001.ligue_name = "Serie A - Italian Football League"
SerieA2001.ligue_year = "2001"
SerieA2001.ligue_winner = "Juventus"
SerieA2001.ligue_top_scorers = ["(1) Dario Hubner(Piacenza), 24 goals","(2) David Trezeguet(Juventus), 24 goals","(3) Christian Vieri(Inter), 22 goals"]
SerieA2002 = Football()
SerieA2002.ligue_name = "Serie A - Italian Football League"
SerieA2002.ligue_year = "2002"
SerieA2002.ligue_winner = "Juventus"
SerieA2002.ligue_top_scorers = ["(1) Christian Vieri(Inter), 24 goals","(2) Adrian Mutu(Parma), 18 goals","(3) Filippo Inzaghi(Milan), 17 goals"]
SerieA2003 = Football()
SerieA2003.ligue_name = "Serie A - Italian Football League"
SerieA2003.ligue_year = "2003"
SerieA2003.ligue_winner = "Milan"
SerieA2003.ligue_top_scorers = ["(1) Andrij Shevchenko(Milan), 24 goals","(2) Alberto Gilardino(Parma), 23 goals","(3) Francesco Totti(Roma), 20 goals"]
SerieA2004 = Football()
SerieA2004.ligue_name = "Serie A - Italian Football League"
SerieA2004.ligue_year = "2004"
SerieA2004.ligue_winner = "Juventus (Revoked)"
SerieA2004.ligue_top_scorers = ["(1) Cristiano Lucarelli(Livorno), 24 goals","(2) Alberto Gilardino(Parma), 23 goals","(3) Vincenzo Montella(Roma), 21 goals"]
SerieA2005 = Football()
SerieA2005.ligue_name = "Serie A - Italian Football League"
SerieA2005.ligue_year = "2005"
SerieA2005.ligue_winner = "Juventus (Revoked) ---> Inter"
SerieA2005.ligue_top_scorers = ["(1) Luca Toni(Fiorentina), 31 goals","(2) David Trezeguet(Juventus), 23 goals","(3) David Suazo(Cagliari), 22 goals"]
SerieA2006 = Football()
SerieA2006.ligue_name = "Serie A - Italian Football League"
SerieA2006.ligue_year = "2006"
SerieA2006.ligue_winner = "Inter"
SerieA2006.ligue_top_scorers = ["(1) Francesco Totti(Roma), 26 goals","(2) Cristiano Lucarelli(Livorno), 20 goals","(3) Christian Riganò(Messina), 19 goals"]
SerieA2007 = Football()
SerieA2007.ligue_name = "Serie A - Italian Football League"
SerieA2007.ligue_year = "2007"
SerieA2007.ligue_winner = "Inter"
SerieA2007.ligue_top_scorers = ["(1) Alessandro Del Piero(Juventus), 21 goals","(2) David Trezeguet(Juventus), 20 goals","(3) Marco Borriello(Genoa), 19 goals"]
SerieA2008 = Football()
SerieA2008.ligue_name = "Serie A - Italian Football League"
SerieA2008.ligue_year = "2008"
SerieA2008.ligue_winner = "Inter"
SerieA2008.ligue_top_scorers = ["(1) Zlatan Ibrahimovic(Inter), 25 goals","(2) Marco Di Vaio(Bologna), 24 goals","(3) Diego Milito(Genoa), 24 goals"]
SerieA2009 = Football()
SerieA2009.ligue_name = "Serie A - Italian Football League"
SerieA2009.ligue_year = "2009"
SerieA2009.ligue_winner = "Inter"
SerieA2009.ligue_top_scorers = ["(1) Antonio Di Natale(Udinese), 29 goals","(2) Diego Milito(Inter), 22 goals","(3) Giampaolo Pazzini(Sampdoria), 19 goals"]
SerieA2010 = Football()
SerieA2010.ligue_name = "Serie A - Italian Football League"
SerieA2010.ligue_year = "2010"
SerieA2010.ligue_winner = "Milan"
SerieA2010.ligue_top_scorers = ["(1) Antonio Di Natale(Udinese), 28 goals","(2) Edinson Cavani(Napoli), 26 goals","(3) Samuel Eto'o(Inter), 21 goals"]
SerieA2011 = Football()
SerieA2011.ligue_name = "Serie A - Italian Football League"
SerieA2011.ligue_year = "2011"
SerieA2011.ligue_winner = "Juventus"
SerieA2011.ligue_top_scorers = ["(1) Zlatan Ibrahimovic(Milan), 28 goals","(2) Diego Milito(Inter), 24 goals","(3) Edinson Cavani(Napoli), 23 goals"]
SerieA2012 = Football()
SerieA2012.ligue_name = "Serie A - Italian Football League"
SerieA2012.ligue_year = "2012"
SerieA2012.ligue_winner = "Juventus"
SerieA2012.ligue_top_scorers = ["(1) Edinson Cavani(Napoli), 29 goals","(2) Antonio Di Natale(Udinese), 23 goals","(3) Stephan El Shaarawy(Milan), 16 goals"]
SerieA2013 = Football()
SerieA2013.ligue_name = "Serie A - Italian Football League"
SerieA2013.ligue_year = "2013"
SerieA2013.ligue_winner = "Juventus"
SerieA2013.ligue_top_scorers = ["(1) Ciro Immobile(Torino), 22 goals","(2) Luca Toni(Hellas Verona), 20 goals","(3) Carlos Tevez(Juventus), 19 goals"]
SerieA2014 = Football()
SerieA2014.ligue_name = "Serie A - Italian Football League"
SerieA2014.ligue_year = "2014"
SerieA2014.ligue_winner = "Juventus"
SerieA2014.ligue_top_scorers = ["(1) Luca Toni(Hellas Verona), 22 goals","(2) Mauro Icardi(Inter), 22 goals","(3) Carlos Tevez(Juventus), 20 goals"]
SerieA2015 = Football()
SerieA2015.ligue_name = "Serie A - Italian Football League"
SerieA2015.ligue_year = "2015"
SerieA2015.ligue_winner = "Juventus"
SerieA2015.ligue_top_scorers = ["(1) Gonzalo Higuain(Napoli), 36 goals","(2) Paulo Dybala(Juventus), 19 goals","(3) Carlos Bacca(Milan), 18 goals"]
SerieA2016 = Football()
SerieA2016.ligue_name = "Serie A - Italian Football League"
SerieA2016.ligue_year = "2016"
SerieA2016.ligue_winner = "N.D."
SerieA2016.ligue_top_scorers = "N.D."
#Ligue 1
Ligue1_1997 = Football()
Ligue1_1997.ligue_name = "Ligue 1 - French Football League"
Ligue1_1997.ligue_year = "1997"
Ligue1_1997.ligue_winner = "Lens"
Ligue1_1997.ligue_top_scorers = ["(1) Stéphane Guivarc'h(Auxerre), 21 goals","(2) David Trezeguet(Monaco), 18 goals","(3) Victor Ikpeba(Monaco), 16 goals"]
Ligue1_1998 = Football()
Ligue1_1998.ligue_name = "Ligue 1 - French Football League"
Ligue1_1998.ligue_year = "1998"
Ligue1_1998.ligue_winner = "Bordeaux"
Ligue1_1998.ligue_top_scorers = ["(1) Sylvain Wiltord(Bordeaux), 22 goals","(2) Alain Cavéglia(O.Lyon), 17 goals ","(3) Lilian Laslandes(Bordeaux), 15 goals"]
Ligue1_1999 = Football()
Ligue1_1999.ligue_name = "Ligue 1 - French Football League"
Ligue1_1999.ligue_year = "1999"
Ligue1_1999.ligue_winner = "Monaco"
Ligue1_1999.ligue_top_scorers = ["(1) Sonny Anderson(O.Lyon), 23 goals","(2) David Trezeguet(Monaco), 22 goals","(3) Marco Simone(Monaco), 21 goals"]
Ligue1_2000 = Football()
Ligue1_2000.ligue_name = "Ligue 1 - French Football League"
Ligue1_2000.ligue_year = "2000"
Ligue1_2000.ligue_winner = "Nantes"
Ligue1_2000.ligue_top_scorers = ["(1) Sonny Anderson(O.Lyon), 22 goals;","(2) Pauleta(Bordeaux), 20 goals","(3) Frédéric Néè(Bastia), 16 goals"]
Ligue1_2001 = Football()
Ligue1_2001.ligue_name = "Ligue 1 - French Football League"
Ligue1_2001.ligue_year = "2001"
Ligue1_2001.ligue_winner = "O.Lyon"
Ligue1_2001.ligue_top_scorers = ["(1) Djibril Cissé(Auxerre), 22 goals","(2) Pauleta(Bordeaux), 22 goals","(3) Jean-Claude Darcheville(Lorient), 19 goals"]
Ligue1_2002 = Football()
Ligue1_2002.ligue_name = "Ligue 1 - French Football League"
Ligue1_2002.ligue_year = "2002"
Ligue1_2002.ligue_winner = "O.Lyon"
Ligue1_2002.ligue_top_scorers = ["(1) Shabani Nonda(Monaco), 26 goals","(2) Pauleta(Bordeaux), 23 goals","(3) Didier Drogba(Guingamp), 17 goals"]
Ligue1_2003 = Football()
Ligue1_2003.ligue_name = "Ligue 1 - French Football League"
Ligue1_2003.ligue_year = "2003"
Ligue1_2003.ligue_winner = "O.Lyon"
Ligue1_2003.ligue_top_scorers = ["(1) Djibril Cissé(Auxerre), 26 goals","(2) Alexander Frei(Stade Rennes), 20 goals","(3) Didier Drogba(Olympique Marseille), 19 goals"]
Ligue1_2004 = Football()
Ligue1_2004.ligue_name = "Ligue 1 - French Football League"
Ligue1_2004.ligue_year = "2004"
Ligue1_2004.ligue_winner = "O.Lyon"
Ligue1_2004.ligue_top_scorers = ["(1) Alexander Frei(Stade Rennes), 20 goals","(2) Mickael Pagis(Strasbourg Alsace), 15 goals","(3) Pauleta(Paris SG), 14 goals"]
Ligue1_2005 = Football()
Ligue1_2005.ligue_name = "Ligue 1 - French Football League"
Ligue1_2005.ligue_year = "2005"
Ligue1_2005.ligue_winner = "O.Lyon"
Ligue1_2005.ligue_top_scorers = ["(1) Pauleta(Paris SG), 21 goals","(2) Fred(O.Lyon), 14 goals","(3) Peter Odemwingie(Lille), 14 goals"]
Ligue1_2006 = Football()
Ligue1_2006.ligue_name = "Ligue 1 - French Football League"
Ligue1_2006.ligue_year = "2006"
Ligue1_2006.ligue_winner = "O.Lyon"
Ligue1_2006.ligue_top_scorers = ["(1) Pauleta(Paris SG), 15 goals","(2) Steve Savidan(Valenciennes), 13 goals","(3) Ismael Bangoura(Le Mans), 12 goals"]
Ligue1_2007 = Football()
Ligue1_2007.ligue_name = "Ligue 1 - French Football League"
Ligue1_2007.ligue_year = "2007"
Ligue1_2007.ligue_winner = "O.Lyon"
Ligue1_2007.ligue_top_scorers = ["(1) Karim Benzema(O.Lyon), 20 goals","(2) Mamadou Niang(Olympique Marseille), 18 goals","(3) Bafétimbi Gomis(Saint-Étienne), 16 goals"]
Ligue1_2008 = Football()
Ligue1_2008.ligue_name = "Ligue 1 - French Football League"
Ligue1_2008.ligue_year = "2008"
Ligue1_2008.ligue_winner = "Bordeaux"
Ligue1_2008.ligue_top_scorers =  ["(1) André-Pierre Gignac(Toulouse), 24 goals","(2) Guillaume Hoarau(Paris SG), 17 goals","(3) Karim Benzema(O.Lyon), 17 goals"] 
Ligue1_2009 = Football()
Ligue1_2009.ligue_name = "Ligue 1 - French Football League"
Ligue1_2009.ligue_year = "2009"
Ligue1_2009.ligue_winner = "O.Marseille"
Ligue1_2009.ligue_top_scorers = ["(1) Mamadou Niang(Olympique Marseille), 18 goals","(2) Kevin Gameiro(Lorient), 17 goals","(3) Lisandro Lopez(O.Lyon), 15 goals"]
Ligue1_2010 = Football()
Ligue1_2010.ligue_name = "Ligue 1 - French Football League"
Ligue1_2010.ligue_year = "2010"
Ligue1_2010.ligue_winner = "Lille"
Ligue1_2010.ligue_top_scorers = ["(1) Moussa Sow(Lille), 25 goals","(2) Kevin Gameiro(Lorient), 22 goals","(3) Youssef El-Arabi(Caen), 17 goals"]
Ligue1_2011 = Football()
Ligue1_2011.ligue_name = "Ligue 1 - French Football League"
Ligue1_2011.ligue_year = "2011"
Ligue1_2011.ligue_winner = "Montpellier"
Ligue1_2011.ligue_top_scorers = ["(1) Nenê(Paris SG), 21 goals","(2) Olivier Giroud(Montpellier), 21 goals","(3) Eden Hazard(Lille), 20 goals"] 
Ligue1_2012 = Football()
Ligue1_2012.ligue_name = "Ligue 1 - French Football League"
Ligue1_2012.ligue_year = "2012"
Ligue1_2012.ligue_winner = "Paris SG"
Ligue1_2012.ligue_top_scorers = ["(1) Zlatan Ibrahimovic(Paris SG), 30 goals","(2) Pierre-Emerick Aubameyang(Saint-Étienne), 19 goals","(3) Dario Cvitanich(Nice), 19 goals"]
Ligue1_2013 = Football()
Ligue1_2013.ligue_name = "Ligue 1 - French Football League"
Ligue1_2013.ligue_year = "2013"
Ligue1_2013.ligue_winner = "Paris SG"
Ligue1_2013.ligue_top_scorers = ["(1) Zlatan Ibrahimovic(Paris SG), 26 goals","(2) Vincent Aboubakar(Lorient), 16 goals","(3) Edinson Cavani(Paris SG), 16 goals"]
Ligue1_2014 = Football()
Ligue1_2014.ligue_name = "Ligue 1 - French Football League"
Ligue1_2014.ligue_year = "2014"
Ligue1_2014.ligue_winner = "Paris SG"
Ligue1_2014.ligue_top_scorers = ["(1) Alexandre Lacazette(O.Lyon), 27 goals","(2) André-Pierre Gignac(Olympique Marseille), 21 goals","(3) Zlatan Ibrahimovic(Paris SG), 19 goals"]
Ligue1_2015 = Football()
Ligue1_2015.ligue_name = "Ligue 1 - French Football League"
Ligue1_2015.ligue_year = "2015"
Ligue1_2015.ligue_winner = "Paris SG"
Ligue1_2015.ligue_top_scorers = ["(1) Zlatan Ibrahimovic(Paris SG), 38 goals","(2) Alexandre Lacazette(O.Lyon), 21 goals","(3) Edinson Cavani(Paris SG), 19 goals"]
Ligue1_2016 = Football()
Ligue1_2016.ligue_name = "Ligue 1 - French Football League"
Ligue1_2016.ligue_year = "2016"
Ligue1_2016.ligue_winner = "N.D."
Ligue1_2016.ligue_top_scorers = "N.D."
#Bundesliga:
Bundesliga_1997 = Football()
Bundesliga_1997.ligue_name = "Bundesliga - German Football League"
Bundesliga_1997.ligue_year = "1997"
Bundesliga_1997.ligue_winner = "Kaiserslautern"
Bundesliga_1997.ligue_top_scorers = ["(1) Ulf Kirsten(Bayer Leverkusen), 22 goals","(2) Olaf Marschall(Kaiserslautern), 21 goals","(3) Stéphane Chapuisat(Borussia Dortmund), 14 goals"]
Bundesliga_1998 = Football()
Bundesliga_1998.ligue_name = "Bundesliga - German Football League"
Bundesliga_1998.ligue_year = "1998"
Bundesliga_1998.ligue_winner = "Bayern Munchen"
Bundesliga_1998.ligue_top_scorers = ["(1) Michael Preetz(Hertha Berliner), 23 goals","(2) Ulf Kirsten(Bayer Leverkusen), 19 goals","(3) Oliver Neuville(Hansa Rostock, 14 goals"]
Bundesliga_1999 = Football()
Bundesliga_1999.ligue_name = "Bundesliga - German Football League"
Bundesliga_1999.ligue_year = "1999"
Bundesliga_1999.ligue_winner = "Bayern Munchen"
Bundesliga_1999.ligue_top_scorers = ["(1) Martin Max(Munchen 1860), 19 goals","(2) Ulf Kirsten(Bayer Leverkusen), 17 goals","(3) Giovane Élber(Bayern Munchen), 14 goals"]
Bundesliga_2000 = Football()
Bundesliga_2000.ligue_name = "Bundesliga - German Football League"
Bundesliga_2000.ligue_year = "2000"
Bundesliga_2000.ligue_winner = "Bayern Munchen"
Bundesliga_2000.ligue_top_scorers = ["(1) Sergej Barbarez(Hamburger), 22 goals","(2) Ebbe Sand(Schalke 04), 22 goals","(3) Claudio Pizarro(Bayern Munchen), 19 goals"]
Bundesliga_2001 = Football()
Bundesliga_2001.ligue_name = "Bundesliga - German Football League"
Bundesliga_2001.ligue_year = "2001"
Bundesliga_2001.ligue_winner = "Borussia Dortmund"
Bundesliga_2001.ligue_top_scorers = ["(1) Màrcio Amoroso(Borussia Dortmund), 18 goals","(2) Martin Max(Munchen 1860), 18 goals","(3) Michael Ballack(Bayer Leverkusen), 17 goals"]
Bundesliga_2002 = Football()
Bundesliga_2002.ligue_name = "Bundesliga - German Football League"
Bundesliga_2002.ligue_year = "2002"
Bundesliga_2002.ligue_winner = "Bayern Munchen"
Bundesliga_2002.ligue_top_scorers = ["(1) Giovane Élber(Bayern Munchen), 21 goals","(2) Thomas Christiansen(Bochum), 21 goals","(3) Aìlton(Werder 1899), 16 goals"]
Bundesliga_2003 = Football()
Bundesliga_2003.ligue_name = "Bundesliga - German Football League"
Bundesliga_2003.ligue_year = "2003"
Bundesliga_2003.ligue_winner = "Werder 1899"
Bundesliga_2003.ligue_top_scorers = ["(1) Aìlton(Werder 1899), 28 goals","(2) Roy Makaay(Bayern Munchen), 23 goals","(3) Martin Max(Hansa Rostock), 20 goals"]
Bundesliga_2004 = Football()
Bundesliga_2004.ligue_name = "Bundesliga - German Football League"
Bundesliga_2004.ligue_year = "2004"
Bundesliga_2004.ligue_winner = "Bayern Munchen"
Bundesliga_2004.ligue_top_scorers = ["(1) Marek Mintàl(Nurnberg), 24 goals","(2) Rooy Makaay(Bayern Munchen), 22 goals","(3) Dimitar Berbaton(Bayer Leverkusen), 20 goals"]
Bundesliga_2005 = Football()
Bundesliga_2005.ligue_name = "Bundesliga - German Football League"
Bundesliga_2005.ligue_year = "2005"
Bundesliga_2005.ligue_winner = "Bayern Munchen"
Bundesliga_2005.ligue_top_scorers = ["(1) Miroslav Klose(Werder 1899), 25 goals","(2) Dimitar Berbatov(Bayer Leverkusen), 21 goals","(3) Halil Altintop(Kaiserslautern), 20 goals"]
Bundesliga_2006 = Football()
Bundesliga_2006.ligue_name = "Bundesliga - German Football League"
Bundesliga_2006.ligue_year = "2006"
Bundesliga_2006.ligue_winner = "Stuttgart"
Bundesliga_2006.ligue_top_scorers = ["(1) Theofanis Gekas(Bochum), 20 goals","(2) Alexander Frei(Borussia Dortmund), 16 goals","(3) Roy Makaay(Bayern Munchen), 16 goals"]
Bundesliga_2007 = Football()
Bundesliga_2007.ligue_name = "Bundesliga - German Football League"
Bundesliga_2007.ligue_year = "2007"
Bundesliga_2007.ligue_winner = "Bayern Munchen"
Bundesliga_2007.ligue_top_scorers = ["(1) Luca Toni(Bayern Munchen), 24 goals","(2) Mario Gomez(Stuttgart), 19 goals","(3) Kevin Kurànyi(Schalke 04), 15 goals"]
Bundesliga_2008 = Football()
Bundesliga_2008.ligue_name = "Bundesliga - German Football League"
Bundesliga_2008.ligue_year = "2008"
Bundesliga_2008.ligue_winner = "Wolfsburg"
Bundesliga_2008.ligue_top_scorers = ["(1) Grafite(Wolfsburg), 28 goals","(2) Edin Dzeko(Wolfsburg), 26 goals","(3) Mario Gomez(Stuttgart), 24 goals"]
Bundesliga_2009 = Football()
Bundesliga_2009.ligue_name = "Bundesliga - German Football League"
Bundesliga_2009.ligue_year = "2009"
Bundesliga_2009.ligue_winner = "Bayern Munchen"
Bundesliga_2009.ligue_top_scorers = ["(1) Edin Dzeko(Wolfsburg), 22 goals","(2) Stefan Kießling(Bayer Leverkusen), 21 goals","(3) Lucas Barrios(Borussia Dortmund), 19 goals"]
Bundesliga_2010 = Football()
Bundesliga_2010.ligue_name = "Bundesliga - German Football League"
Bundesliga_2010.ligue_year = "2010"
Bundesliga_2010.ligue_winner = "Borussia Dortmund"
Bundesliga_2010.ligue_top_scorers = ["(1) Mario Gomez(Bayern Munchen), 28 goals","(2) Papis Cissé(Freiburg), 22 goals","(3) Milivoje Novakovic(Koln), 17 goals"]
Bundesliga_2011 = Football()
Bundesliga_2011.ligue_name = "Bundesliga - German Football League"
Bundesliga_2011.ligue_year = "2011"
Bundesliga_2011.ligue_winner = "Borussia Dortmund"
Bundesliga_2011.ligue_top_scorers = ["(1) Klaas-Jan Huntelaar(Schalke 04), 29 goals","(2) Mario Gomez(Bayern Munchen), 26 goals","(3) Robert Lewandowski(Borussia Dortmund), 22 goals"]
Bundesliga_2012 = Football()
Bundesliga_2012.ligue_name = "Bundesliga - German Football League"
Bundesliga_2012.ligue_year = "2012"
Bundesliga_2012.ligue_winner = "Bayern Munchen"
Bundesliga_2012.ligue_top_scorers = ["(1) Stefan Kießling(Bayer Leverkusen), 25 goals","(2) Robert Lewandowski(Borussia Dortmund), 24 goals","(3) Alexander Meier(E.Frankfurt), 16 goals"]
Bundesliga_2013 = Football()
Bundesliga_2013.ligue_name = "Bundesliga - German Football League"
Bundesliga_2013.ligue_year = "2013"
Bundesliga_2013.ligue_winner = "Bayern Munchen"
Bundesliga_2013.ligue_top_scorers = ["(1) Robert Lewandowski(Borussia Dortmund), 20 goals","(2) Mario Mandzukic(Bayern Munchen), 18 goals","(3) Josip Drmic(Nurnberg), 17 goals"]
Bundesliga_2014 = Football()
Bundesliga_2014.ligue_name = "Bundesliga - German Football League"
Bundesliga_2014.ligue_year = "2014"
Bundesliga_2014.ligue_winner = "Bayern Munchen"
Bundesliga_2014.ligue_top_scorers = ["(1) Alexander Meier(E.Frankfurt), 19 goals","(2) Robert Lewandowski(Bayern Munchen), 17 goals","(3) Arjen Robben(Bayern Munchen), 17 goals"]
Bundesliga_2015 = Football()
Bundesliga_2015.ligue_name = "Bundesliga - German Football League"
Bundesliga_2015.ligue_year = "2015"
Bundesliga_2015.ligue_winner = "Bayern Munchen"
Bundesliga_2015.ligue_top_scorers = ["(1) Robert Lewandowski(Bayern Munchen), 30 goals","(2) Pierre-Emerick Aubameyang(Borussia Dortmund), 25 goals","(3) Thomas Muller(Bayern Munchen), 20 goals"]
Bundesliga_2016 = Football()
Bundesliga_2016.ligue_name = "Bundesliga - German Football League"
Bundesliga_2016.ligue_year = "2016"
Bundesliga_2016.ligue_winner = "N.D."
Bundesliga_2016.ligue_top_scorers = "N.D."
#Liga
LaLiga_1997 = Football()
LaLiga_1997.ligue_name = "LaLiga - Spain Football Division"
LaLiga_1997.ligue_year = "1997"
LaLiga_1997.ligue_winner = "Barcelona"
LaLiga_1997.ligue_top_scorers = ["(1) Christian Vieri(Atlético Madrid), 24 goals","(2) Rivaldo(Barcelona), 19 goals","(3) Luis Enrique(Barcelona), 18 goals"]
LaLiga_1998 = Football()
LaLiga_1998.ligue_name = "LaLiga - Spain Football Division"
LaLiga_1998.ligue_year = "1998"
LaLiga_1998.ligue_winner = "Barcelona"
LaLiga_1998.ligue_top_scorers = ["(1) Raùl(Real Madrid), 25 goals","(2) Rivaldo(Barcelona), 24 goals","(3) Claudio Lòpez(Valencia), 21 goals"]
LaLiga_1999 = Football()
LaLiga_1999.ligue_name = "LaLiga - Spain Football Division"
LaLiga_1999.ligue_year = "1999"
LaLiga_1999.ligue_winner = "Deportivo"
LaLiga_1999.ligue_top_scorers = ["(1) Salva Ballesta(Racing Santander), 27 goals","(2) Catanha(Màlaga), 24 goals","(3) Jimmi Floyd Hasselbaink(Atlético Madrid), 24 goals"]
LaLiga_2000 = Football()
LaLiga_2000.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2000.ligue_year = "2000"
LaLiga_2000.ligue_winner = "Real Madrid"
LaLiga_2000.ligue_top_scorers = ["(1) Raùl(Real Madrid), 24 goals","(2) Rivaldo(Barcelona), 23 goals","(3) Javi Moreno(Alavés), 22 goals"]                                 
LaLiga_2001 = Football()
LaLiga_2001.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2001.ligue_year = "2001"
LaLiga_2001.ligue_winner = "Valencia"
LaLiga_2001.ligue_top_scorers = ["(1) Raùl(Real Madrid), 24 goals","(2) Rivaldo(Barcelona), 23 goals","(3) Javi Moreno(Alavès), 22 goals"]
LaLiga_2002 = Football()
LaLiga_2002.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2002.ligue_year = "2002"
LaLiga_2002.ligue_winner = "Real Madrid"
LaLiga_2002.ligue_top_scorers = ["(1) Diego Tristàn(Deportivo), 20 goals","(2) Patrick Kluivert(Barcelona), 18 goals","(3) Morientes(Real Madrid), 18 goals"]
LaLiga_2003 = Football()
LaLiga_2003.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2003.ligue_year = "2003"
LaLiga_2003.ligue_winner = "Valencia"
LaLiga_2003.ligue_top_scorers = ["(1) Roy Makaay(Deportivo), 29 goals","(2) Nihat Kahveci(Real Sociedad), 23 goals","(3) Ronaldo(Real Madrid), 23 goals"]
LaLiga_2004 = Football()
LaLiga_2004.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2004.ligue_year = "2004"
LaLiga_2004.ligue_winner = "Barcelona"
LaLiga_2004.ligue_top_scorers = ["(1) Ronaldo(Real Madrid), 24 goals","(2) Jùlio Baptista(Sevilla), 20 goals","(3) Raùl Tamudo(Espanyol), 20 goals"]
LaLiga_2005 = Football()
LaLiga_2005.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2005.ligue_year = "2005"
LaLiga_2005.ligue_winner = "Barcelona"
LaLiga_2005.ligue_top_scorers = ["(1) Samuel Eto'o(Barcelona), 26 goals","(2) David Villa(Valencia), 25 goals","(3) Ronaldinho(Barcelona), 17 goals"]
LaLiga_2006 = Football()
LaLiga_2006.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2006.ligue_year = "2006"
LaLiga_2006.ligue_winner = "Real Madrid"
LaLiga_2006.ligue_top_scorers = ["(1) Ruud van Nistelrooy(Real Madrid), 25 goals","(2) Diego Milito(Real Zaragoza), 23 goals","(3) Frédéric Kanouté(Sevilla), 21 goals"] 
LaLiga_2007 = Football()
LaLiga_2007.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2007.ligue_year = "2007"
LaLiga_2007.ligue_winner = "Real Madrid"
LaLiga_2007.ligue_top_scorers = ["(1) Daniel Guiza(Mallorca), 27 goals","(2) Lùis Fabiano(Sevilla), 24 goals","(3)Sergio Aguero(Atlético Madrid), 19 goals"]
LaLiga_2008 = Football()
LaLiga_2008.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2008.ligue_year = "2008"
LaLiga_2008.ligue_winner = "Barcelona"
LaLiga_2008.ligue_top_scorers = ["(1) Diego Forlàn(Atletico Madrid), 32 goals","(2) Samuel Eto'o(Barcelona), 30 goals","(3) David Villa(Valencia), 28 goals"]
LaLiga_2009 = Football()
LaLiga_2009.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2009.ligue_year = "2009"
LaLiga_2009.ligue_winner = "Barcelona"
LaLiga_2009.ligue_top_scorers = ["(1) Lionel Messi(Barcelona), 34 goals","(2) Gonzalo Higuain(Real Madrid), 27 goals","(3) Cristiano Ronaldo(Real Madrid), 26 goals"]
LaLiga_2010 = Football()
LaLiga_2010.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2010.ligue_year = "2010"
LaLiga_2010.ligue_winner = "Barcelona"
LaLiga_2010.ligue_top_scorers = ["(1) Cristiano Ronaldo(Real Madrid), 40 goals","(2) Lionel Messi(Barcelona), 31 goals","(3) Sergio Aguero(Atlético Madrid), 20 goals"]
LaLiga_2011 = Football()
LaLiga_2011.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2011.ligue_year = "2011"
LaLiga_2011.ligue_winner = "Real Madrid"
LaLiga_2011.ligue_top_scorers = ["(1) Lionel Messi(Barcelona), 50 goals","(2) Cristiano Ronaldo(Real Madrid), 46 goals","(3) Radamel Falcao(Atlético Madrid), 24 goals"]
LaLiga_2012 = Football()
LaLiga_2012.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2012.ligue_year = "2012"
LaLiga_2012.ligue_winner = "Barcelona"
LaLiga_2012.ligue_top_scorers = ["(1) Lionel Messi(Barcelona), 46 goals","(2) Cristiano Ronaldo(Real Madrid), 34 goals","(3) Radamel Falcao(Atlético Madrid), 28 goals"]
LaLiga_2013 = Football()
LaLiga_2013.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2013.ligue_year = "2013"
LaLiga_2013.ligue_winner = "Atlético Madrid"
LaLiga_2013.ligue_top_scorers = ["(1) Cristiano Ronaldo(Real Madrid), 31 goals","(2) Lionel Messi(Barcelona), 28 goals","(3) Diego Costa(Atlético Madrid), 27 goals"]
LaLiga_2014 = Football()
LaLiga_2014.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2014.ligue_year = "2014"
LaLiga_2014.ligue_winner = "Barcelona"
LaLiga_2014.ligue_top_scorers = ["(1) Cristiano Ronaldo(Real Madrid), 48 goals","(2) Lionel Messi(Barcelona), 43 goals","(3) Antoine Griezmann(Atlético Madrid), 22 goals"]
LaLiga_2015 = Football()
LaLiga_2015.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2015.ligue_year = "2015"
LaLiga_2015.ligue_winner = "Barcelona"
LaLiga_2015.ligue_top_scorers = ["(1) Luis Suàrez(Barcelona), 40 goals","(2) Cristiano Ronaldo(Real Madrid), 35 goals","(3) Lionel Messi(Barcelona), 26 goals"]
LaLiga_2016 = Football()
LaLiga_2016.ligue_name = "LaLiga - Spain Football Division"
LaLiga_2016.ligue_year = "2016"
LaLiga_2016.ligue_winner = "N.D."
LaLiga_2016.ligue_top_scorers = "N.D."
#UEFA Champions League:
UCL_1997 = Football()
UCL_1997.ligue_name = "UEFA Champions League"
UCL_1997.ligue_year = "1997"
UCL_1997.ligue_winner = "Real Madrid"
UCL_1997.ligue_top_scorers = ["(1) Alessandro Del Piero(Juventus), 10 goals","(2) Thierry Henry(Monaco), 7 goals","(3) Serhij Rebrov(Dynamo Kyiv), 6 goals"]
UCL_1998 = Football()
UCL_1998.ligue_name = "UEFA Champions League"
UCL_1998.ligue_year = "1998"
UCL_1998.ligue_winner = "Manchester Utd"
UCL_1998.ligue_top_scorers = ["(1) Andriy Shevchenko(Dynamo Kyiv), 8 goals","(2) Dwight Yorke(Manchester Utd), 8 goals","(3) Zlatko Zahovic(Porto), 7 goals"]
UCL_1999 = Football()
UCL_1999.ligue_name = "UEFA Champions League"
UCL_1999.ligue_year = "1999"
UCL_1999.ligue_winner = "Real Madrid"
UCL_1999.ligue_top_scorers = ["(1) Jardel(Porto), 10 goals","(2) Rivaldo(Barcelona), 10 goals","(3) Raùl(Real Madrid), 10 goals"]
UCL_2000 = Football()
UCL_2000.ligue_name = "UEFA Champions League"
UCL_2000.ligue_year = "2000"
UCL_2000.ligue_winner = "Bayern Munchen"
UCL_2000.ligue_top_scorers = ["(1) Raùl(Real Madrid), 7 goals","(2) Marco Simone(Monaco), 6 goals","(3) Rivaldo(Barcelona), 6 goals"]
UCL_2001 = Football()
UCL_2001.ligue_name = "UEFA Champions League"
UCL_2001.ligue_year = "2001"
UCL_2001.ligue_winner = "Real Madrid"
UCL_2001.ligue_top_scorers = ["(1) Ruud van Nistelrooy(Manchester Utd), 10 goals","(2) David Trezeguet(Juventus), 8 goals","(3) Ole Gunnar Solskjaer(Manchester Utd), 7 goals"]
UCL_2002 = Football()
UCL_2002.ligue_name = "UEFA Champions League"
UCL_2002.ligue_year = "2002"
UCL_2002.ligue_winner = "Milan"
UCL_2002.ligue_top_scorers = ["(1) Ruud van Nistelrooy(Manchester Utd), 12 goals","(2) Filippo Inzaghi(Milan), 10 goals","(3) Roy Makaay(Deportivo), 9 goals"]
UCL_2003 = Football()
UCL_2003.ligue_name = "UEFA Champions League"
UCL_2003.ligue_year = "2003"
UCL_2003.ligue_winner = "Porto"
UCL_2003.ligue_top_scorers = ["(1) Fernando Morientes(Monaco), 9 goals","(2) Dado Prso(Monaco), 7 goals","(3) Roy Makaay(Bayern Munchen), 6 goals"]
UCL_2004 = Football()
UCL_2004.ligue_name = "UEFA Champions League"
UCL_2004.ligue_year = "2004"
UCL_2004.ligue_winner = "Liverpool"
UCL_2004.ligue_top_scorers = ["(1) Ruud van Nistelrooy(Manchester Utd), 8 goals","(2) Adriano(Inter), 7 goals","(3) Roy Makaay(Bayern Munchen), 7 goals"]
UCL_2005 = Football()
UCL_2005.ligue_name = "UEFA Champions League"
UCL_2005.ligue_year = "2005"
UCL_2005.ligue_winner = "Barcelona"
UCL_2005.ligue_top_scorers = ["(1) Andrij Shevchenko(Milan), 9 goals","(2) Ronaldinho(Barcelona), 7 goals","(3) David Trezeguet(Juventus), 6 goals"]
UCL_2006 = Football()
UCL_2006.ligue_name = "UEFA Champions League"
UCL_2006.ligue_year = "2006"
UCL_2006.ligue_winner = "Milan"
UCL_2006.ligue_top_scorers = ["(1) Kakà(Milan), 10 goals","(2) Peter Crouch(Liverpool), 6 goals","(3) Ruud van Nistelrooy(Real Madrid), 6 goals"]
UCL_2007 = Football()
UCL_2007.ligue_name = "UEFA Champions League"
UCL_2007.ligue_year = "2007"
UCL_2007.ligue_winner = "Manchester Utd"
UCL_2007.ligue_top_scorers = ["(1) Cristiano Ronaldo(Manchester Utd), 8 goals","(2) Lionel Messi(Barcelona), 6 goals","(3) Fernando Torres(Liverpool), 6 goals"]
UCL_2008 = Football()
UCL_2008.ligue_name = "UEFA Champions League"
UCL_2008.ligue_year = "2008"
UCL_2008.ligue_winner = "Barcelona"
UCL_2008.ligue_top_scorers = ["(1) Lionel Messi(Barcelona), 9 goals","(2) Steven Gerrard(Liverpool), 7 goals","(3) Miroslav Klose(Bayern Monaco), 7 goals"]
UCL_2009 = Football()
UCL_2009.ligue_name = "UEFA Champions League"
UCL_2009.ligue_year = "2009"
UCL_2009.ligue_winner = "Inter"
UCL_2009.ligue_top_scorers = ["(1) Lionel Messi(Barcelona), 8 goals","(2) Cristiano Ronaldo(Real Madrid), 7 goals","(3) Ivica Olic(Bayern Munchen), 7 goals"]
UCL_2010 = Football()
UCL_2010.ligue_name = "UEFA Champions League"
UCL_2010.ligue_year = "2010"
UCL_2010.ligue_winner = "Barcelona"
UCL_2010.ligue_top_scorers = ["(1) Lionel Messi(Barcelona), 12 goals","(2) Mario Gomez(Bayern Munchen), 8 goals","(3) Samuel Eto'o(Inter), 8 goals"]
UCL_2011 = Football()
UCL_2011.ligue_name = "UEFA Champions League"
UCL_2011.ligue_year = "2011"
UCL_2011.ligue_winner = "Chelsea"
UCL_2011.ligue_top_scorers = ["(1) Lionel Messi(Barcelona), 14 goals","(2) Mario Gomez(Bayern Munchen), 12 goals","(3) Cristiano Ronaldo(Real Madrid), 10 goals"]
UCL_2012 = Football()
UCL_2012.ligue_name = "UEFA Champions League"
UCL_2012.ligue_year = "2012"
UCL_2012.ligue_winner = "Bayern Munchen"
UCL_2012.ligue_top_scorers = ["(1) Cristiano Ronaldo(Real Madrid), 12 goals","(2) Robert Lewandowski(Borussia Dortmund), 10 goals","(3) Burak Yilmaz(Galatasaray), 8 goals"]
UCL_2013 = Football()
UCL_2013.ligue_name = "UEFA Champions League"
UCL_2013.ligue_year = "2013"
UCL_2013.ligue_winner = "Real Madrid"
UCL_2013.ligue_top_scorers = ["(1) Cristiano Ronaldo(Real Madrid), 17 goals","(2) Zlatan Ibrahimovic(Paris SG), 10 goals","(3) Diego Costa(Atlético Madrid), 8 goals"]
UCL_2014 = Football()
UCL_2014.ligue_name = "UEFA Champions League"
UCL_2014.ligue_year = "2014"
UCL_2014.ligue_winner = "Barcelona"
UCL_2014.ligue_top_scorers = ["(1) Neymar(Barcelona), 10 goals","(2) Cristiano Ronaldo(Real Madrid), 10 goals","(3) Lionel Messi(Barcelona), 10 goals"] 
UCL_2015 = Football()
UCL_2015.ligue_name = "UEFA Champions League"
UCL_2015.ligue_year = "2015"
UCL_2015.ligue_winner = "Real Madrid"
UCL_2015.ligue_top_scorers = ["(1) Cristiano Ronaldo(Real Madrid), 16 goals","(2) Robert Lewandowski(Bayern Munchen), 9 goals","(3) Luis Suarez(Barcelona), 8 goals"]
UCL_2016 = Football()
UCL_2016.ligue_name = "UEFA Champions League"
UCL_2016.ligue_year = "2016"
UCL_2016.ligue_winner = "N.D."
UCL_2016.ligue_top_scorers = "N.D."
#Europa League:
UEL_1997 = Football()
UEL_1997.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_1997.ligue_year = "1997"
UEL_1997.ligue_winner = "Inter"
UEL_1997.ligue_top_scorers = ["(1) Shota Arveladze(Ajax), 7 goals","(2) Stéphane Guivarc'h(Auxerre), 7 goals","(3) Ronaldo(Inter), 6 goals"]
UEL_1998 = Football()
UEL_1998.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_1998.ligue_year = "1998"
UEL_1998.ligue_winner = "Parma"
UEL_1998.ligue_top_scorers = ["(1) Enrico Chiesa(Parma), 8 goals","(2) Darko Kovacevic(Real Sociedad), 8 goals","(3) Alain Caveglia(O.Lyon), 7 goals"]
UEL_1999 = Football()
UEL_1999.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_1999.ligue_year = "1999"
UEL_1999.ligue_winner = "Galatasaray"
UEL_1999.ligue_top_scorers = ["(1) Darko Kovacevic(Juventus), 10 goals","(2) Thierry Henry(Arsenal), 7 goals","(3) Pascal Nouma(Lens), 7 goals"]
UEL_2000 = Football()
UEL_2000.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2000.ligue_year = "2000"
UEL_2000.ligue_winner = "Liverpool"
UEL_2000.ligue_top_scorers = ["(1) Goran Drulic(Red Star Belgrade), 6 goals","(2) Marcin Kuzba(Lausanne), 6 goals","(3) Javi Moreno(Alavés), 6 goals"]
UEL_2001 = Football()
UEL_2001.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2001.ligue_year = "2001"
UEL_2001.ligue_winner = "Feyenoord"
UEL_2001.ligue_top_scorers = ["(1) Pierre Van Hooijdonk(Feyenoord), 8 goals","(2) Mohamed Kallon(Inter), 6 goals","(3) Richard Núñez(Grasshopper), 6 goals"]
UEL_2002 = Football()
UEL_2002.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2002.ligue_year = "2002"
UEL_2002.ligue_winner = "Porto"
UEL_2002.ligue_top_scorers = ["(1) Derlei(Porto), 12 goals","(2) Henrik Larsoon(Celtic), 11 goals","(3) Maciej Zurawski(Wisla Krakòv), 8 goals"]
UEL_2003 = Football()
UEL_2003.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2003.ligue_year = "2003"
UEL_2003.ligue_winner = "Valencia"
UEL_2003.ligue_top_scorers = ["(1) Sonny Anderson(Villareal), 7 goals","(2) Mateja Kezman(PSV), 6 goals","(3) Alan Shearer(Newcastle Utd), 6 goals"]
UEL_2004 = Football()
UEL_2004.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2004.ligue_year = "2004"
UEL_2004.ligue_winner = "CSKA Moskow"
UEL_2004.ligue_top_scorers = ["(1) Alan Shearer(Newcastle Utd)","(2) Liédson(Sporting CP)","(3) Cacau(Stuttgart), 7 goals"]
UEL_2005 = Football()
UEL_2005.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2005.ligue_year = "2005"
UEL_2005.ligue_winner = "Seville"
UEL_2005.ligue_top_scorers = ["(1) Matìas Delgado(Basilea), 7 goals","(2) Javier Saviola(Seville), 6 goals","(3) Mark Viduka(Middlesbrough), 6 goals"]
UEL_2006 = Football()
UEL_2006.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2006.ligue_year = "2006"
UEL_2006.ligue_winner = "Seville"
UEL_2006.ligue_top_scorers = ["(1) Walter Pandiani(Espanyol), 11 goals","(2) Claudiu Niculescu(Dinamo Bucuresti), 8 goals","(3) Shota Arveladze(AZ Alkmaar), 7 goals"]
UEL_2007 = Football()
UEL_2007.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2007.ligue_year = "2007"
UEL_2007.ligue_winner = "Zenit Saint Petersburg"
UEL_2007.ligue_top_scorers = ["(1) Pavel Pogrebnjak(Zenit Saint Petersburg), 10 goals","(2) Luca Toni(Bayern Munchen), 10 goals","(3) Stefan Kießling (Bayer Leverkusen), 7 goals"]
UEL_2008 = Football()
UEL_2008.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2008.ligue_year = "2008"
UEL_2008.ligue_winner = "Shakhtar Donetsk"
UEL_2008.ligue_top_scorers = ["(1) Vàgner Love(CSKA Moskow), 11 goals","(2) Ivica Olic(Hamburger), 9 goals","(3) Fabio Quagliarella(Udinese), 8 goals"]
UEL_2009 = Football()
UEL_2009.ligue_name = "UEFA Europa League"
UEL_2009.ligue_year = "2009"
UEL_2009.ligue_winner = "Atlético Madrid"
UEL_2009.ligue_top_scorers = ["(1) Claudio Pizarro(Werder 1899), 9 goals","(2) Oscar Cardozo(Benfica), 9 goals","(3) Jonathan Legear(Anderlecht), 6 goals"]
UEL_2010 = Football()
UEL_2010.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2010.ligue_year = "2010"
UEL_2010.ligue_winner = "Porto"
UEL_2010.ligue_top_scorers = ["(1) Radamel Falcao(Porto), 17 goals","(2) Giuseppe Rossi(Villareal), 11 goals","(3) Tomàs Necid(CSKA Moscow), 6 goals"]
UEL_2011 = Football()
UEL_2011.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2011.ligue_year = "2011"
UEL_2011.ligue_winner = "Atlético Madrid"
UEL_2011.ligue_top_scorers = ["(1) Radamel Falcao(Atlético Madrid), 12 goals","(2) Klaas-Jan Huntelaar(Schalke 04), 10 goals","(3) Adriàn Lòpez(Atlético Madrid), 8 goals"]
UEL_2012 = Football()
UEL_2012.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2012.ligue_year = "2012"
UEL_2012.ligue_winner = "Chelsea"
UEL_2012.ligue_top_scorers = ["(1) Libor Kozàk(Lazio), 8 goals","(2) Edinson Cavani(Napoli), 7 goals","(3) Oscar Cardozo(Benfica), 7 goals"]
UEL_2013 = Football()
UEL_2013.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2013.ligue_year = "2013"
UEL_2013.ligue_winner = "Seville"
UEL_2013.ligue_top_scorers = ["(1) Jonathan Soriano(Salzburg), 8 goals","(2) Paco Alcàcer(Valencia), 7 goals","(3) Roman Bezjak(Ludogorec), 6 goals"]
UEL_2014 = Football()
UEL_2014.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2014.ligue_year = "2014"
UEL_2014.ligue_winner = "Seville"
UEL_2014.ligue_top_scorers = ["(1) Alan(Salzburg), 8 goals","(2) Romelu Lukaku(Everton), 8 goals","(3) Carlos Bacca(Seville), 7 goals"]
UEL_2015 = Football()
UEL_2015.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2015.ligue_year = "2015"
UEL_2015.ligue_winner = "Seville"
UEL_2015.ligue_top_scorers = ["(1) Aritz Aduriz(Athletic Bilbao), 10 goals","(2) Cédric Bakambu(Villareal), 9 goals","(3) Pierre-Emerick Aubameyang(Borussia Dortmund), 8 goals"]
UEL_2016 = Football()
UEL_2016.ligue_name = "UEFA Europa League (UEFA Cup)"
UEL_2016.ligue_year = "2016"
UEL_2016.ligue_winner = "N.D."
UEL_2016.ligue_top_scorers = "N.D."
welcome()
choice()
        
    
    
