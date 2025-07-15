#this code is to help the user figure out their course scheudle
#reference: the UC Merced Spring 2023 Courses Catalog

#dictionary of Spring 2024 UC Merced Classes Catalog

#available subjects: ANTH, ENGR, MATH, ME
#available class number: 001 to 999
#available class types: LECT, DISC, LAB, SEM
#available days: MON, TUES, WEDS, THURS, FRI
#available times to start: 7:30 to 19:30 (every 30 mins)

#Anthropology Courses
anth = {
    "num_anth" : {
        "anth_001" : {
            "lect_001_anth" :{
                "TUES 1" : "10:30",
                "THURS 1" : "10:30"
            },
            "disc_001_anth" : {
                "WEDS 1" : "9:30",
                "WEDS 2" : "10:30",
                "WEDS 3" : "11:30",
                "WEDS 4" : "12:30",
                "WEDS 5" : "13:30",
                "WEDS 6" : "14:30",
                "WEDS 7" : "15:30",
                "WEDS 8" : "16:30"
            }
        },
        "anth_003" : {
            "lect_003_anth" : {
                "TUES 1" : "9:00",
                "THURS 1" : "9:00"
            },
            "disc_003_anth" : {
                "THURS 1" : "16:30",
                "THURS 2" : "17:30",
                "FRI 1" : "10:30",
                "FRI 2" : "11:30",
                "FRI 3" : "12:30",
                "FRI 4" : "13:30",
                "FRI 5" : "14:30",
                "FRI 6" : "15:30",
                "FRI 7" : "16:30"
            }
        },
        "anth_010" : {
            "lect_010_anth" : {
                "TUES 1" : "11:30",
                "THURS 1" : "11:30"
            }
        },
        "anth_116" : {
            "lect_116_anth" : {
                "TUES 1" : "13:30",
                "THURS 1" : "13:30"
            }
        },
        "anth_126" : {
            "lect_126_anth" : {
                "TUES 1" : "15:00",
                "THURS 1" : "15:00"
            }
        },
        "anth_131" : {
            "lect_131_anth" : {
                "TUES 1" : "8:00"
            }
        },
        "anth_149" : {
            "lect_149_anth" : {
                "MON 1" : "10:30",
                "WEDS 1" : "10:30",
                "FRI 1" : "10:30"
            }
        },
        "anth_152" : {
            "lect_152_anth" : {
                "MON 1" : "11:30"
            }
        },
        "anth_162" : {
            "lect_162_anth" : {
                "MON 1" : "13:30",
                "WEDS 1" : "13:30"
            }
        },
        "anth_169" : {
            "lect_169_anth" : {
                "MON 1" : "12:00",
                "WEDS 1" : "12:00"
            }
        },
        "anth_170" : {
            "lect_170_anth" : {
                "TUES 1" : "9:00",
                "THURS 1" : "9:00"
            },
            "disc_170_anth" : {
                "WEDS 1" : "14:30",
                "WEDS 2" : "15:30"
            }
        },
        "anth_179" : {
            "lect_179_anth" : {
                "MON 1" : "13:30",
                "WEDS 1" : "13:30"
            }
        }
    }
}



#Engineering Courses
engr = {
    "num_engr" : {
        "engr_045" : {
            "lect_045_engr" : {
                "MON 1" : "12:30",
                "WEDS 1" : "12:30",
                "FRI 1" : "12:30"
            },
            "lab_045_engr" : {
                "MON 1" : "13:30",
                "TUES 1" : "17:30",
                "THURS 1" : "12:30",
                "TUES 2" : "11:00"
            }
        },
        "engr_057" : {
            "lect_057_engr" : {
                "MON 1" : "9:30",
                "WEDS 1" : "9:30"
            },
            "disc_057_engr" : {
                "WEDS 1" : "13:30",
                "WEDS 2" : "15:30",
                "WEDS 3" : "11:30",
                "WEDS 4" : "10:30",
                "WEDS 5" : "12:30"
            }
        },
        "engr_065" : {
            "lect_065_engr" : {
                "MON 1" : "13:30",
                "WEDS 1" : "13:30"
            },
            "lab_065_engr" : {
                "TUES 1" : "9:00",
                "TUES 2" : "12:00",
                "THURS 1" : "12:00",
                "TUES 3" : "15:00",
                "THURS 2" : "15:00",
                "WEDS 1" : "15:00",
                "MON 1" : "15:00"
            }
        },
        "engr_080" : {
            "lect_080_engr" : {
                "TUES 1" : "15:00",
                "THURS 1" : "15:00"
            },
            "disc_080_engr" : {
                "FRI 1" : "16:30"
            }
        },
        "engr_091" : {
            "sem_091_engr" : {
                "THURS 1" : "15:30"
            }
        },
        "engr_120" : {
            "lect_120_engr" : {
                "TUES 1" : "15:00",
                "THURS 1" : "15:00"
            },
            "lab_120_engr" : {
                "THURS 1" : "10:30",
                "WEDS 1" : "14:00",
                "WEDS 2" : "8:00",
                "FRI 1" : "13:30",
                "WEDS 3" : "11:00",
                "FRI 2" : "10:30"
            }
        },
        "engr_130" : {
            "lect_130_engr" : {
                "TUES 1" : "9:00",
                "THURS 1" : "9:00"
            }
        },
        "engr_135" : {
            "lect_135_engr" : {
                "TUES 1" : "15:00",
                "THURS 1" : "15:00"
            },
            "lab_135_engr" : {
                "TUES 1" : "8:30",
                "WEDS 1" : "13:30",
                "FRI 1" : "8:30",
                "THURS 1" : "8:30"
            }
        },
        "engr_140" : {
            "lect_140_engr" : {
                "MON 1" : "9:00",
                "WEDS 1" : "9:00"
            },
            "lab_140_engr" : {
                "FRI 1" : "7:30",
                "FRI 1" : "13:30",
                "THURS 1" : "13:30",
                "TUES 1" : "16:30"
            }
        },
        "engr_151" : {
            "lect_151_engr" : {
                "TUES 1" : "12:00",
                "THURS 1" : "12:00"
            },
            "lab_151_engr" : {
                "MON 1" : "8:00",
                "WEDS 1" : "8:00",
                "TUES 1" : "8:00",
                "TUES 2" : "14:30"
            }
        },
        "engr_155" : {
            "lect_155_engr" : {
                "TUES 1" : "12:00",
                "THURS 1" : "12:00"
            }
        },
        "engr_156" : {
            "lect_156_engr" : {
                "MON 1" : "10:30"
            },
            "lab_156_engr" : {
                "FRI 1" : "9:30",
                "FRI 2" : "11:30"
            }
        },
        "engr_170" : {
            "lect_170_engr" : {
                "TUES 1" : "10:30",
                "THURS 1" : "10:30"
            }
        },
        "engr_180" : {
            "lect_180_engr" : {
                "MON 1" : "9:00",
                "WEDS 1" : "9:00"
            },
            "lab_180_engr" : {
                "FRI 1" : "10:30",
                "THURS 1" : "16:30"
            }
        },
        "engr_193" : {
            "lect_193_engr" : {
                "MON 1" : "15:30"
            }
        },
        "engr_194" : {
            "lect_194_engr" : {
                "WEDS 1" : "15:30"
            }
        },
        "engr_270" : {
            "lect_270_engr" : {
                "TUES 1" : "10:30",
                "THURS 1" : "10:30"
            }
        }
    }        
}



#Mathematics Courses
math = {
    "num_math" : {
        "math_011" : {
            "lect_011_math" : {
                "MON 1" : "16:30",
                "WEDS 1" : "16:30",
                "FRI 1" : "16:30",
                "MON 2" : "10:30",
                "WEDS 2" : "10:30",
                "FRI 2" : "10:30",
                "MON 3" : "15:30",
                "WEDS 3" : "15:30",
                "FRI 3" : "15:30",
            },
            "disc_011_math" : {
                "TUES 1" : "17:30",
                "WEDS 1" : "10:30",
                "MON 1" : "11:30",
                "TUES 2" : "19:30",
                "WEDS 2" : "14:30",
                "THURS 1" : "15:30",
                "WEDS 3" : "17:30",
                "THURS 2" : "18:30",
                "FRI 1" : "8:30",
                "THURS 3" : "18:30",
                "TUES 3" : "17:30",
                "TUES 4" : "18:30",
                "FRI 2" : "8:30",
                "FRI 3" : "18:30"
            }
        },
        "math_012" : {
            "lect_012_math" : {
                "MON 1" : "14:30",
                "WEDS 1" : "14:30",
                "FRI 1" : "14:30"
            },
            "disc_012_math" : {
                "FRI 1" : "17:30",
                "MON 1" : "12:30",
                "FRI 2" : "8:30",
                "FRI 3" : "15:30",
                "MON 2" : "18:30",
                "WEDS 1" : "19:30",
                "FRI 4" : "12:30"
            }
        },
        "math_015" : {
            "lect_015_math" : {
                "FRI 1" : "14:30"
            },
            "disc_015_math" : {
                "FRI 1" : "15:30",
                "FRI 2" : "17:30"
            }
        },
        "math_021" : {
            "lect_021_math" : {
                "MON 1" : "11:30",
                "WEDS 1" : "11:30",
                "FRI 1" : "11:30",
                "MON 2" : "9:30",
                "WEDS 2" : "9:30",
                "FRI 2" : "9:30",
                "MON 3" : "8:30",
                "WEDS 3" : "8:30",
                "FRI 3" : "8:30"
            },
            "disc_021_math" : {
                "WEDS 1" : "16:30",
                "FRI 1" : "16:30",
                "THURS 1" : "18:30",
                "MON 1" : "15:30",
                "FRI 2" : "14:30",
                "THURS 2" : "14:30",
                "MON 2" : "16:30",
                "FRI 3" : "15:30",
                "FRI 4" : "16:30",
                "MON 3" : "18:30",
                "TUES 1" : "7:30",
                "TUES 2" : "18:30"
            }
        },
        "math_022" : {
            "lect_022_math" : {
                "MON 1" : "12:30",
                "WEDS 1" : "12:30",
                "FRI 1" : "12:30",
                "MON 2" : "12:30",
                "WEDS 2" : "12:30",
                "FRI 2" : "12:30"
            },
            "disc_022_math" : {
                "TUES 1" : "15:30",
                "TUES 2" : "16:30",
                "MON 1" : "19:30",
                "MON 2" : "13:30",
                "TUES 3" : "15:30",
                "THURS 1" : "11:30",
                "THURS 2" : "13:30",
                "THURS 3" : "15:30",
                "THURS 4" : "17:30",
                "TUES 4" : "14:30",
                "FRI 1" : "13:30",
                "FRI 2" : "11:30"
            }
        },
        "math_023" : {
            "lect_023_math" : {
                "MON 1" : "10:30",
                "WEDS 1" : "10:30",
                "FRI 1" : "10:30",
                "MON 2" : "11:30",
                "WEDS 2" : "11:30",
                "FRI 2" : "11:30"
            },
            "disc_023_math" : {
                "FRI 1" : "11:30",
                "TUES 1" : "15:30",
                "TUES 2" : "17:30",
                "TUES 3" : "11:30",
                "TUES 4" : "13:30",
                "THURS 1" : "19:30",
                "MON 1" : "15:30",
                "MON 2" : "17:30",
                "TUES 5" : "17:30"
            }
        },
        "math_024" : {
            "lect_024_math" : {
                "TUES 1" : "13:30",
                "THURS 1" : "13:30",
                "TUES 2" : "16:00",
                "THURS 2" : "16:00"
            },
            "disc_024_math" : {
                "MON 1" : "17:30",
                "THURS 1" : "15:30",
                "WEDS 1" : "17:30",
                "WEDS 2" : "15:30",
                "FRI 1" : "14:30",
                "THURS 2" : "18:30",
                "TUES 1" : "19:30",
                "MON 2" : "11:30",
                "WEDS 3" : "17:30"
            }
        },
        "math_032" : {
            "lect_032_math" : {
                "MON 1" : "12:30",
                "TUES 1" : "12:30",
                "WEDS 1" : "12:30",
                "MON 2" : "13:30",
                "TUES 2" : "13:30",
                "WEDS 2" : "13:30",
            },
            "disc_032_math" : {
                "THURS 1" : "13:30",
                "WEDS 1" : "17:30",
                "THURS 2" : "15:30",
                "FRI 1" : "16:30",
                "FRI 2" : "14:30",
                "WEDS 2" : "9:30",
                "WEDS 3" : "11:30",
                "MON 1" : "17:30"
            }
        },
        "math_125" : {
            "lect_125_math" : {
                "MON 1" : "12:30",
                "WEDS 1" : "13:30"
            },
            "disc_125_math" : {
                "FRI 1" : "12:30"
            }
        },
        "math_126" : {
            "lect_126_math" : {
                "MON 1" : "10:30",
                "WEDS 1" : "10:30"
            },
            "disc_126_math" : {
                "FRI 1" : "9:30",
                "FRI 2" : "11:30"
            }
        },
        "math_131" : {
            "lect_131_math" : {
                "TUES 1" : "13:30",
                "THURS 1" : "13:30"
            },
            "disc_131_math" : {
                "FRI 1" : "8:30",
                "FRI 2" : "17:30",
                "MON 1" : "9:30",
                "TUES 1" : "16:30"
            }
        },
        "math_132" : {
            "lect_132_math" : {
                "TUES 1" : "15:00",
                "THURS 1" : "15:00"
            },
            "disc_132_math" : {
                "FRI 1" : "16:30",
                "FRI 2" : "15:30"
            }
        },
        "math_140" : {
            "lect_140_math" : {
                "TUES 1" : "9:00",
                "THURS 1" : "9:00"
            },
            "disc_140_math" : {
                "THURS 1" : "10:30"
            }
        },
        "math_141" : {
            "lect_141_math" : {
                "MON 1" : "16:30",
                "WEDS 1" : "16:30"
            },
            "disc_141_math" : {
                "MON 1" : "18:30",
                "WEDS 1" : "18:30",
                "WEDS 2" : "9:30"
            }
        },
        "math_150" : {
            "lect_150_math" : {
                "MON 1" : "15:00",
                "WEDS 1" : "15:00"
            },
            "disc_150_math" : {
                "THURS 1" : "11:30",
                "THURS 2" : "12:30"
            }
        },
        "math_181" : {
            "lect_181_math" : {
                "MON 1" : "12:00",
                "WEDS 1" : "12:00"
            },
            "disc_181_math" : {
                "WEDS 1" : "13:30"
            }
        },
        "math_222" : {
            "lect_222_math" : {
                "TUES 1" : "13:30",
                "THURS 1" : "13:30"
            },
            "disc_222_math" : {
                "THURS 1" : "9:30"
            }
        },
        "math_224" : {
            "lect_224_math" : {
                "MON 1" : "9:00",
                "WEDS 1" : "9:00"
            },
            "disc_224_math" : {
                "MON 1" : "10:30"
            }
        },
        "math_232" : {
            "lect_232_math" : {
                "TUES 1" : "10:30",
                "THURS 1" : "10:30"
            },
            "disc_232_math" : {
                "WEDS 1" : "12:30"
            }
        },
        "math_234" : {
            "lect_232_math" : {
                "MON 1" : "12:00",
                "WEDS 1" : "12:00"
            }
        },
        "math_291" : {
            "sem_291_math" : {
                "TUES 1" : "15:00"
            }
        }
    }
}



#Mechanical Engineering Courses
me = {
    "num_me" : {
        "me_001" : {
            "lect_001_me" : {
                "WEDS 1" : "15:30"
            }
        },
        "me_021" : {
            "lect_021_me" : {
                "MON 1" : "11:30"
            },
            "lab_021_me" : {
                "THURS 1" : "10:30",
                "TUES 1" : "19:30",
                "TUES 2" : "16:30",
                "WEDS 1" : "19:30",
            }
        },
        "me_120" : {
            "lect_120_me" : {
                "MON 1" : "12:00",
                "WEDS 1" : "12:00"
            }
        },
        "me_135" : {
            "lect_135_me" : {
                "TUES 1" : "16:30",
                "THURS 1" : "16:30"
            },
            "lab_135_me" : {
                "WEDS 1" : "16:30",
                "MON 1" : "19:30"
            }
        },
        "me_137" : {
            "lect_137_me" : {
                "MON 1" : "10:30"
            },
            "lab_137_me" : {
                "MON 1" : "16:30",
                "WEDS 1" : "16:30",
                "TUES 1" : "16:30",
                "THURS 1" : "16:30",
                "TUES 2" : "19:30",
                "THURS 2" : "19:30"
            }
        },
        "me_140" : {
            "lect_140_me" : {
                "MON 1" : "9:00",
                "WEDS 1" : "9:00"
            },
            "lab_140_me" : {
                "MON 1" : "16:30",
                "FRI 1" : "13:00",
                "TUES 1" : "9:30",
                "TUES 2" : "13:30"
            }
        },
        "me_141" : {
            "lect_141_me" : {
                "TUES 1" : "15:30",
                "THURS 1" : "15:30"
            },
            "lab_141_me" : {
                "FRI 1" : "8:30"
            }
        },
        "me_143" : {
            "lect_143_me" : {
                "MON 1" : "13:30",
                "WEDS 1" : "13:30"
            },
            "lab_143_me" : {
                "THURS 1" : "9:00",
                "THURS 2" : "13:30"
            }
        },
        "me_144" : {
            "lect_144_me" : {
                "WEDS 1" : "10:30"
            },
            "lab_144_me" : {
                "FRI 1" : "10:30",
                "FRI 2" : "16:30"
            }
        },
        "me_149" : {
            "lect_149_me" : {
                "FRI 1" : "9:30"
            },
            "lab_149_me" : {
                "MON 1" : "16:30",
                "TUES 1" : "10:30"
            }
        },
        "me_202" : {
            "lect_202_me" : {
                "TUES 1" : "11:30",
                "THURS 1" : "11:30"
            }
        },
        "me_210" : {
            "lect_210_me" : {
                "MON 1" : "10:30",
                "WEDS 1" : "10:30"
            }
        },
        "me_237" : {
            "lect_237_me" : {
                "TUES 1" : "13:30",
                "THURS 1" : "13:30"
            }
        },
        "me_290" : {
            "sem_237_me" : {
                "TUES 1" : "9:00",
                "THURS 1" : "9:00",
                "TUES 2" : "16:30",
                "THURS 2" : "16:30",
            }
        }
    }
}





print('Welcome to the Course Schedule Optimzer')

def current_status():
    #asks the user for input regarding their current school status
    subject = input('Please state the class you are looking for; only ANTH, ENGR, MATH, ME (all lowercase)')
    class_number = input('Please state the class number you are looking for; only 001 to 999 ')
    class_type = input('Please state the type of class you are looking for; only LECT,DISC,LAB,SEM (all lowercase)')

    
    #show the user their current answer choices
    print('\nYou are looking for a {} {} {} class.'.format(subject, class_number, class_type))
    print('NOTE: LECT are ~1 hour, DISC are ~2 hours, LAB are ~3 hours.\n')

    
    #print the different choices with day and time (only if chosen correctly)
    if subject == "anth":
        temp_subject = subject
        subject = anth
        print("Here are the available days and their weekly times.")
        print(subject["num_" + temp_subject][temp_subject + "_" + class_number][class_type + "_" + class_number + "_" + temp_subject])
    elif subject == "engr":
        temp_subject = subject
        subject = engr
        print("Here are the available days and their weekly times.")
        print(subject["num_" + temp_subject][temp_subject + "_" + class_number][class_type + "_" + class_number + "_" + temp_subject])
    elif subject == "math":
        temp_subject = subject
        subject = math
        print("Here are the available days and their weekly times.")
        print(subject["num_" + temp_subject][temp_subject + "_" + class_number][class_type + "_" + class_number + "_" + temp_subject])
    elif subject == "me":
        temp_subject = subject
        subject = me
        print("Here are the available days and their weekly times.")
        print(subject["num_" + temp_subject][temp_subject + "_" + class_number][class_type + "_" + class_number + "_" + temp_subject])
    else:
        print("That course during that time or day does not exist in the Spring 2024 catalog.")

    return
   

#calls current_status() to asks the user for their information the first time
current_status()

#verifying if the information inputted is correct and asks to continue looking for available classes
print('Please reference the UC Merced Spring 2023 Catalog while you look at the available dates. i.e. FRIDAY 3 = Third Friday on the listing.')
verify = input('\nAre you finished looking at courses? (Y/N)')
while verify != 'Y':
    print('\nPlease restart this program and fill in correctly and answer Y')
    current_status()
    print('Please reference the UC Merced Spring 2023 Catalog while you look at the available dates. i.e. FRIDAY 3 = Third Friday on the listing.')
    verify = input('\nAre you finished looking at courses? (Y/N)')

