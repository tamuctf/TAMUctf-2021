int flag_check(char* flag, int len) {
    int output = 1;
    if (len != 19) { return 0; }
    output &= flag[0] == 'g';
    output &= flag[1] == 'i';
    output &= flag[2] == 'g';
    output &= flag[3] == 'e';
    output &= flag[4] == 'm';
    output &= flag[5] == '{';
    output &= flag[6] == 'l';
    output &= flag[7] == '3';
    output &= flag[8] == '4';
    output &= flag[9] == 'k';
    output &= flag[10] == 'y';
    output &= flag[11] == '_';
    output &= flag[12] == 'm';
    output &= flag[13] == '3';
    output &= flag[14] == 'm';
    output &= flag[15] == '0';
    output &= flag[16] == 'r';
    output &= flag[17] == 'y';
    output &= flag[18] == '}';
    return output;
}