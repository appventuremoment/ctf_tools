#include "out.h"



int _init(EVP_PKEY_CTX *ctx)

{
  int iVar1;
  
  iVar1 = __gmon_start__();
  return iVar1;
}



void FUN_00101020(void)

{
                    // WARNING: Treating indirect jump as call
  (*(code *)(undefined *)0x0)();
  return;
}



void FUN_00101070(void)

{
  __cxa_finalize();
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int puts(char *__s)

{
  int iVar1;
  
  iVar1 = puts(__s);
  return iVar1;
}



void __stack_chk_fail(void)

{
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int printf(char *__format,...)

{
  int iVar1;
  
  iVar1 = printf(__format);
  return iVar1;
}



void __isoc99_scanf(void)

{
  __isoc99_scanf();
  return;
}



void processEntry _start(undefined8 param_1,undefined8 param_2)

{
  undefined auStack_8 [8];
  
  __libc_start_main(main,param_2,&stack0x00000008,0,0,param_1,auStack_8);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



// WARNING: Removing unreachable block (ram,0x00101103)
// WARNING: Removing unreachable block (ram,0x0010110f)

void deregister_tm_clones(void)

{
  return;
}



// WARNING: Removing unreachable block (ram,0x00101144)
// WARNING: Removing unreachable block (ram,0x00101150)

void register_tm_clones(void)

{
  return;
}



void __do_global_dtors_aux(void)

{
  if (completed_0 != '\0') {
    return;
  }
  FUN_00101070(__dso_handle);
  deregister_tm_clones();
  completed_0 = 1;
  return;
}



void frame_dummy(void)

{
  register_tm_clones();
  return;
}



undefined8 main(void)

{
  long in_FS_OFFSET;
  char local_38;
  char local_37;
  char local_36;
  char local_35;
  char local_34;
  char local_33;
  char local_32;
  char local_31;
  char local_30;
  char local_2f;
  char local_2e;
  char local_2d;
  char local_2c;
  char local_2b;
  char local_2a;
  char local_29;
  char local_28;
  char local_27;
  char local_26;
  char local_25;
  char local_24;
  char local_23;
  char local_22;
  char local_21;
  char local_20;
  char local_1f;
  char local_1e;
  char local_1d;
  char local_1c;
  char local_1b;
  char local_1a;
  char local_19;
  char local_18;
  char local_17;
  char local_16;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter flag: ");
  __isoc99_scanf(&DAT_00102011,&local_38);
  if (local_38 == 'b') {
    if (local_37 == 'l') {
      if (local_36 == 'a') {
        if (local_35 == 'h') {
          if (local_34 == 'a') {
            if (local_33 == 'j') {
              if (local_32 == '{') {
                if (local_31 == 'w') {
                  if (local_30 == 'h') {
                    if (local_2f == '4') {
                      if (local_2e == '7') {
                        if (local_2d == '_') {
                          if (local_2c == 'D') {
                            if (local_2b == '3') {
                              if (local_2a == 'C') {
                                if (local_29 == '0') {
                                  if (local_28 == 'M') {
                                    if (local_27 == 'P') {
                                      if (local_26 == '1') {
                                        if (local_25 == 'L') {
                                          if (local_24 == '3') {
                                            if (local_23 == 'r') {
                                              if (local_22 == '_') {
                                                if (local_21 == 'd') {
                                                  if (local_20 == '0') {
                                                    if (local_1f == '_') {
                                                      if (local_1e == 'y') {
                                                        if (local_1d == '0') {
                                                          if (local_1c == 'U') {
                                                            if (local_1b == '_') {
                                                              if (local_1a == 'U') {
                                                                if (local_19 == 's') {
                                                                  if (local_18 == '3') {
                                                                    if (local_17 == '?') {
                                                                      if (local_16 == '}') {
                                                                        puts("Correct flag!");
                                                                      }
                                                                      else {
                                                                        puts("Wrong flag!");
                                                                      }
                                                                    }
                                                                    else {
                                                                      puts("Wrong flag!");
                                                                    }
                                                                  }
                                                                  else {
                                                                    puts("Wrong flag!");
                                                                  }
                                                                }
                                                                else {
                                                                  puts("Wrong flag!");
                                                                }
                                                              }
                                                              else {
                                                                puts("Wrong flag!");
                                                              }
                                                            }
                                                            else {
                                                              puts("Wrong flag!");
                                                            }
                                                          }
                                                          else {
                                                            puts("Wrong flag!");
                                                          }
                                                        }
                                                        else {
                                                          puts("Wrong flag!");
                                                        }
                                                      }
                                                      else {
                                                        puts("Wrong flag!");
                                                      }
                                                    }
                                                    else {
                                                      puts("Wrong flag!");
                                                    }
                                                  }
                                                  else {
                                                    puts("Wrong flag!");
                                                  }
                                                }
                                                else {
                                                  puts("Wrong flag!");
                                                }
                                              }
                                              else {
                                                puts("Wrong flag!");
                                              }
                                            }
                                            else {
                                              puts("Wrong flag!");
                                            }
                                          }
                                          else {
                                            puts("Wrong flag!");
                                          }
                                        }
                                        else {
                                          puts("Wrong flag!");
                                        }
                                      }
                                      else {
                                        puts("Wrong flag!");
                                      }
                                    }
                                    else {
                                      puts("Wrong flag!");
                                    }
                                  }
                                  else {
                                    puts("Wrong flag!");
                                  }
                                }
                                else {
                                  puts("Wrong flag!");
                                }
                              }
                              else {
                                puts("Wrong flag!");
                              }
                            }
                            else {
                              puts("Wrong flag!");
                            }
                          }
                          else {
                            puts("Wrong flag!");
                          }
                        }
                        else {
                          puts("Wrong flag!");
                        }
                      }
                      else {
                        puts("Wrong flag!");
                      }
                    }
                    else {
                      puts("Wrong flag!");
                    }
                  }
                  else {
                    puts("Wrong flag!");
                  }
                }
                else {
                  puts("Wrong flag!");
                }
              }
              else {
                puts("Wrong flag!");
              }
            }
            else {
              puts("Wrong flag!");
            }
          }
          else {
            puts("Wrong flag!");
          }
        }
        else {
          puts("Wrong flag!");
        }
      }
      else {
        puts("Wrong flag!");
      }
    }
    else {
      puts("Wrong flag!");
    }
  }
  else {
    puts("Wrong flag!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return 0;
}



void _fini(void)

{
  return;
}



