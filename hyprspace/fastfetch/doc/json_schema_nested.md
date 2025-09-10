# JSON config

- [1. [Optional] Property JSON config > $schema](#schema)
- [2. [Optional] Property JSON config > logo](#logo)
  - [2.1. Property `JSON config > logo > oneOf > item 0`](#logo_oneOf_i0)
  - [2.2. Property `JSON config > logo > oneOf > item 1`](#logo_oneOf_i1)
  - [2.3. Property `JSON config > logo > oneOf > item 2`](#logo_oneOf_i2)
    - [2.3.1. [Optional] Property JSON config > logo > oneOf > item 2 > type](#logo_oneOf_i2_type)
    - [2.3.2. [Optional] Property JSON config > logo > oneOf > item 2 > source](#logo_oneOf_i2_source)
    - [2.3.3. [Optional] Property JSON config > logo > oneOf > item 2 > color](#logo_oneOf_i2_color)
      - [2.3.3.1. [Optional] Property JSON config > logo > oneOf > item 2 > color > 1](#logo_oneOf_i2_color_1)
      - [2.3.3.2. [Optional] Property JSON config > logo > oneOf > item 2 > color > 2](#logo_oneOf_i2_color_2)
      - [2.3.3.3. [Optional] Property JSON config > logo > oneOf > item 2 > color > 3](#logo_oneOf_i2_color_3)
      - [2.3.3.4. [Optional] Property JSON config > logo > oneOf > item 2 > color > 4](#logo_oneOf_i2_color_4)
      - [2.3.3.5. [Optional] Property JSON config > logo > oneOf > item 2 > color > 5](#logo_oneOf_i2_color_5)
      - [2.3.3.6. [Optional] Property JSON config > logo > oneOf > item 2 > color > 6](#logo_oneOf_i2_color_6)
      - [2.3.3.7. [Optional] Property JSON config > logo > oneOf > item 2 > color > 7](#logo_oneOf_i2_color_7)
      - [2.3.3.8. [Optional] Property JSON config > logo > oneOf > item 2 > color > 8](#logo_oneOf_i2_color_8)
      - [2.3.3.9. [Optional] Property JSON config > logo > oneOf > item 2 > color > 9](#logo_oneOf_i2_color_9)
    - [2.3.4. [Optional] Property JSON config > logo > oneOf > item 2 > width](#logo_oneOf_i2_width)
    - [2.3.5. [Optional] Property JSON config > logo > oneOf > item 2 > height](#logo_oneOf_i2_height)
    - [2.3.6. [Optional] Property JSON config > logo > oneOf > item 2 > padding](#logo_oneOf_i2_padding)
      - [2.3.6.1. [Optional] Property JSON config > logo > oneOf > item 2 > padding > top](#logo_oneOf_i2_padding_top)
      - [2.3.6.2. [Optional] Property JSON config > logo > oneOf > item 2 > padding > left](#logo_oneOf_i2_padding_left)
      - [2.3.6.3. [Optional] Property JSON config > logo > oneOf > item 2 > padding > right](#logo_oneOf_i2_padding_right)
    - [2.3.7. [Optional] Property JSON config > logo > oneOf > item 2 > printRemaining](#logo_oneOf_i2_printRemaining)
    - [2.3.8. [Optional] Property JSON config > logo > oneOf > item 2 > preserveAspectRatio](#logo_oneOf_i2_preserveAspectRatio)
    - [2.3.9. [Optional] Property JSON config > logo > oneOf > item 2 > recache](#logo_oneOf_i2_recache)
    - [2.3.10. [Optional] Property JSON config > logo > oneOf > item 2 > position](#logo_oneOf_i2_position)
    - [2.3.11. [Optional] Property JSON config > logo > oneOf > item 2 > chafa](#logo_oneOf_i2_chafa)
      - [2.3.11.1. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > fgOnly](#logo_oneOf_i2_chafa_fgOnly)
      - [2.3.11.2. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > symbols](#logo_oneOf_i2_chafa_symbols)
      - [2.3.11.3. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > canvasMode](#logo_oneOf_i2_chafa_canvasMode)
      - [2.3.11.4. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > colorSpace](#logo_oneOf_i2_chafa_colorSpace)
      - [2.3.11.5. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > ditherMode](#logo_oneOf_i2_chafa_ditherMode)
- [3. [Optional] Property JSON config > general](#general)
  - [3.1. [Optional] Property JSON config > general > thread](#general_thread)
  - [3.2. [Optional] Property JSON config > general > escapeBedrock](#general_escapeBedrock)
  - [3.3. [Optional] Property JSON config > general > playerName](#general_playerName)
  - [3.4. [Optional] Property JSON config > general > dsForceDrm](#general_dsForceDrm)
    - [3.4.1. Property `JSON config > general > dsForceDrm > oneOf > item 0`](#general_dsForceDrm_oneOf_i0)
    - [3.4.2. Property `JSON config > general > dsForceDrm > oneOf > item 1`](#general_dsForceDrm_oneOf_i1)
    - [3.4.3. Property `JSON config > general > dsForceDrm > oneOf > item 2`](#general_dsForceDrm_oneOf_i2)
  - [3.5. [Optional] Property JSON config > general > wmiTimeout](#general_wmiTimeout)
  - [3.6. [Optional] Property JSON config > general > processingTimeout](#general_processingTimeout)
  - [3.7. [Optional] Property JSON config > general > preRun](#general_preRun)
  - [3.8. [Optional] Property JSON config > general > detectVersion](#general_detectVersion)
- [4. [Optional] Property JSON config > display](#display)
  - [4.1. [Optional] Property JSON config > display > stat](#display_stat)
    - [4.1.1. Property `JSON config > display > stat > oneOf > item 0`](#display_stat_oneOf_i0)
    - [4.1.2. Property `JSON config > display > stat > oneOf > item 1`](#display_stat_oneOf_i1)
  - [4.2. [Optional] Property JSON config > display > pipe](#display_pipe)
  - [4.3. [Optional] Property JSON config > display > showErrors](#display_showErrors)
  - [4.4. [Optional] Property JSON config > display > disableLinewrap](#display_disableLinewrap)
  - [4.5. [Optional] Property JSON config > display > hideCursor](#display_hideCursor)
  - [4.6. [Optional] Property JSON config > display > separator](#display_separator)
  - [4.7. [Optional] Property JSON config > display > color](#display_color)
    - [4.7.1. Property `JSON config > display > color > oneOf > colors`](#display_color_oneOf_i0)
    - [4.7.2. Property `JSON config > display > color > oneOf > item 1`](#display_color_oneOf_i1)
      - [4.7.2.1. [Optional] Property JSON config > display > color > oneOf > item 1 > keys](#display_color_oneOf_i1_keys)
      - [4.7.2.2. [Optional] Property JSON config > display > color > oneOf > item 1 > title](#display_color_oneOf_i1_title)
      - [4.7.2.3. [Optional] Property JSON config > display > color > oneOf > item 1 > output](#display_color_oneOf_i1_output)
      - [4.7.2.4. [Optional] Property JSON config > display > color > oneOf > item 1 > separator](#display_color_oneOf_i1_separator)
  - [4.8. [Optional] Property JSON config > display > brightColor](#display_brightColor)
  - [4.9. [Optional] Property JSON config > display > key](#display_key)
    - [4.9.1. [Optional] Property JSON config > display > key > width](#display_key_width)
    - [4.9.2. [Optional] Property JSON config > display > key > type](#display_key_type)
    - [4.9.3. [Optional] Property JSON config > display > key > paddingLeft](#display_key_paddingLeft)
  - [4.10. [Optional] Property JSON config > display > size](#display_size)
    - [4.10.1. [Optional] Property JSON config > display > size > binaryPrefix](#display_size_binaryPrefix)
      - [4.10.1.1. Property `JSON config > display > size > binaryPrefix > oneOf > item 0`](#display_size_binaryPrefix_oneOf_i0)
      - [4.10.1.2. Property `JSON config > display > size > binaryPrefix > oneOf > item 1`](#display_size_binaryPrefix_oneOf_i1)
      - [4.10.1.3. Property `JSON config > display > size > binaryPrefix > oneOf > item 2`](#display_size_binaryPrefix_oneOf_i2)
    - [4.10.2. [Optional] Property JSON config > display > size > maxPrefix](#display_size_maxPrefix)
    - [4.10.3. [Optional] Property JSON config > display > size > ndigits](#display_size_ndigits)
  - [4.11. [Optional] Property JSON config > display > temp](#display_temp)
    - [4.11.1. [Optional] Property JSON config > display > temp > unit](#display_temp_unit)
    - [4.11.2. [Optional] Property JSON config > display > temp > ndigits](#display_temp_ndigits)
    - [4.11.3. [Optional] Property JSON config > display > temp > color](#display_temp_color)
      - [4.11.3.1. [Optional] Property JSON config > display > temp > color > green](#display_temp_color_green)
      - [4.11.3.2. [Optional] Property JSON config > display > temp > color > yellow](#display_temp_color_yellow)
      - [4.11.3.3. [Optional] Property JSON config > display > temp > color > red](#display_temp_color_red)
  - [4.12. [Optional] Property JSON config > display > bar](#display_bar)
    - [4.12.1. [Optional] Property JSON config > display > bar > charElapsed](#display_bar_charElapsed)
    - [4.12.2. [Optional] Property JSON config > display > bar > charTotal](#display_bar_charTotal)
    - [4.12.3. [Optional] Property JSON config > display > bar > borderLeft](#display_bar_borderLeft)
    - [4.12.4. [Optional] Property JSON config > display > bar > borderRight](#display_bar_borderRight)
    - [4.12.5. [Optional] Property JSON config > display > bar > width](#display_bar_width)
  - [4.13. [Optional] Property JSON config > display > percent](#display_percent)
    - [4.13.1. [Optional] Property JSON config > display > percent > type](#display_percent_type)
      - [4.13.1.1. Property `JSON config > display > percent > type > oneOf > item 0`](#display_percent_type_oneOf_i0)
      - [4.13.1.2. Property `JSON config > display > percent > type > oneOf > item 1`](#display_percent_type_oneOf_i1)
        - [4.13.1.2.1. JSON config > display > percent > type > oneOf > item 1 > item 1 items](#autogenerated_heading_2)
    - [4.13.2. [Optional] Property JSON config > display > percent > ndigits](#display_percent_ndigits)
    - [4.13.3. [Optional] Property JSON config > display > percent > color](#display_percent_color)
      - [4.13.3.1. [Optional] Property JSON config > display > percent > color > green](#display_percent_color_green)
      - [4.13.3.2. [Optional] Property JSON config > display > percent > color > yellow](#display_percent_color_yellow)
      - [4.13.3.3. [Optional] Property JSON config > display > percent > color > red](#display_percent_color_red)
  - [4.14. [Optional] Property JSON config > display > freq](#display_freq)
    - [4.14.1. [Optional] Property JSON config > display > freq > ndigits](#display_freq_ndigits)
  - [4.15. [Optional] Property JSON config > display > noBuffer](#display_noBuffer)
  - [4.16. [Optional] Property JSON config > display > constants](#display_constants)
    - [4.16.1. JSON config > display > constants > constants items](#autogenerated_heading_3)
- [5. [Optional] Property JSON config > modules](#modules)
  - [5.1. JSON config > modules > modules items](#autogenerated_heading_4)
    - [5.1.1. Property `JSON config > modules > modules items > anyOf > item 0`](#modules_items_anyOf_i0)
    - [5.1.2. Property `JSON config > modules > modules items > anyOf > item 1`](#modules_items_anyOf_i1)
      - [5.1.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Break`](#modules_items_anyOf_i1_oneOf_i0)
        - [5.1.2.1.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Break > type](#modules_items_anyOf_i1_oneOf_i0_type)
      - [5.1.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery`](#modules_items_anyOf_i1_oneOf_i1)
        - [5.1.2.2.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > type](#modules_items_anyOf_i1_oneOf_i1_type)
        - [5.1.2.2.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > useSetupApi](#modules_items_anyOf_i1_oneOf_i1_useSetupApi)
        - [5.1.2.2.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp](#modules_items_anyOf_i1_oneOf_i1_temp)
          - [5.1.2.2.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 0`](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i0)
          - [5.1.2.2.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1`](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1)
            - [5.1.2.2.3.2.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > green](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_green)
            - [5.1.2.2.3.2.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > yellow](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_yellow)
        - [5.1.2.2.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent](#modules_items_anyOf_i1_oneOf_i1_percent)
          - [5.1.2.2.4.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > green](#modules_items_anyOf_i1_oneOf_i1_percent_green)
          - [5.1.2.2.4.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > yellow](#modules_items_anyOf_i1_oneOf_i1_percent_yellow)
          - [5.1.2.2.4.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > type](#modules_items_anyOf_i1_oneOf_i1_percent_type)
        - [5.1.2.2.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > key](#modules_items_anyOf_i1_oneOf_i1_key)
        - [5.1.2.2.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor)
        - [5.1.2.2.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon)
        - [5.1.2.2.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth)
        - [5.1.2.2.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor)
        - [5.1.2.2.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > format](#modules_items_anyOf_i1_oneOf_i1_format)
      - [5.1.2.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS`](#modules_items_anyOf_i1_oneOf_i2)
        - [5.1.2.3.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > type](#modules_items_anyOf_i1_oneOf_i2_type)
        - [5.1.2.3.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > key](#modules_items_anyOf_i1_oneOf_i2_key)
        - [5.1.2.3.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyColor](#modules_items_anyOf_i1_oneOf_i2_keyColor)
        - [5.1.2.3.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyIcon](#modules_items_anyOf_i1_oneOf_i2_keyIcon)
        - [5.1.2.3.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyWidth](#modules_items_anyOf_i1_oneOf_i2_keyWidth)
        - [5.1.2.3.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > outputColor](#modules_items_anyOf_i1_oneOf_i2_outputColor)
        - [5.1.2.3.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > format](#modules_items_anyOf_i1_oneOf_i2_format)
      - [5.1.2.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth`](#modules_items_anyOf_i1_oneOf_i3)
        - [5.1.2.4.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > type](#modules_items_anyOf_i1_oneOf_i3_type)
        - [5.1.2.4.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > showDisconnected](#modules_items_anyOf_i1_oneOf_i3_showDisconnected)
        - [5.1.2.4.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > percent](#modules_items_anyOf_i1_oneOf_i3_percent)
        - [5.1.2.4.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > key](#modules_items_anyOf_i1_oneOf_i3_key)
        - [5.1.2.4.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyColor](#modules_items_anyOf_i1_oneOf_i3_keyColor)
        - [5.1.2.4.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyIcon](#modules_items_anyOf_i1_oneOf_i3_keyIcon)
        - [5.1.2.4.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyWidth](#modules_items_anyOf_i1_oneOf_i3_keyWidth)
        - [5.1.2.4.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > outputColor](#modules_items_anyOf_i1_oneOf_i3_outputColor)
        - [5.1.2.4.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > format](#modules_items_anyOf_i1_oneOf_i3_format)
      - [5.1.2.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio`](#modules_items_anyOf_i1_oneOf_i4)
        - [5.1.2.5.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > type](#modules_items_anyOf_i1_oneOf_i4_type)
        - [5.1.2.5.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > key](#modules_items_anyOf_i1_oneOf_i4_key)
        - [5.1.2.5.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyColor](#modules_items_anyOf_i1_oneOf_i4_keyColor)
        - [5.1.2.5.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyIcon](#modules_items_anyOf_i1_oneOf_i4_keyIcon)
        - [5.1.2.5.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyWidth](#modules_items_anyOf_i1_oneOf_i4_keyWidth)
        - [5.1.2.5.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > outputColor](#modules_items_anyOf_i1_oneOf_i4_outputColor)
        - [5.1.2.5.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > format](#modules_items_anyOf_i1_oneOf_i4_format)
      - [5.1.2.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board`](#modules_items_anyOf_i1_oneOf_i5)
        - [5.1.2.6.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > type](#modules_items_anyOf_i1_oneOf_i5_type)
        - [5.1.2.6.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > key](#modules_items_anyOf_i1_oneOf_i5_key)
        - [5.1.2.6.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyColor](#modules_items_anyOf_i1_oneOf_i5_keyColor)
        - [5.1.2.6.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyIcon](#modules_items_anyOf_i1_oneOf_i5_keyIcon)
        - [5.1.2.6.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyWidth](#modules_items_anyOf_i1_oneOf_i5_keyWidth)
        - [5.1.2.6.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > outputColor](#modules_items_anyOf_i1_oneOf_i5_outputColor)
        - [5.1.2.6.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > format](#modules_items_anyOf_i1_oneOf_i5_format)
      - [5.1.2.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager`](#modules_items_anyOf_i1_oneOf_i6)
        - [5.1.2.7.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > type](#modules_items_anyOf_i1_oneOf_i6_type)
        - [5.1.2.7.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > key](#modules_items_anyOf_i1_oneOf_i6_key)
        - [5.1.2.7.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyColor](#modules_items_anyOf_i1_oneOf_i6_keyColor)
        - [5.1.2.7.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyIcon](#modules_items_anyOf_i1_oneOf_i6_keyIcon)
        - [5.1.2.7.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyWidth](#modules_items_anyOf_i1_oneOf_i6_keyWidth)
        - [5.1.2.7.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > outputColor](#modules_items_anyOf_i1_oneOf_i6_outputColor)
        - [5.1.2.7.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > format](#modules_items_anyOf_i1_oneOf_i6_format)
      - [5.1.2.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness`](#modules_items_anyOf_i1_oneOf_i7)
        - [5.1.2.8.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > type](#modules_items_anyOf_i1_oneOf_i7_type)
        - [5.1.2.8.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > percent](#modules_items_anyOf_i1_oneOf_i7_percent)
        - [5.1.2.8.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > ddcciSleep](#modules_items_anyOf_i1_oneOf_i7_ddcciSleep)
        - [5.1.2.8.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > compact](#modules_items_anyOf_i1_oneOf_i7_compact)
        - [5.1.2.8.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > key](#modules_items_anyOf_i1_oneOf_i7_key)
        - [5.1.2.8.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyColor](#modules_items_anyOf_i1_oneOf_i7_keyColor)
        - [5.1.2.8.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyIcon](#modules_items_anyOf_i1_oneOf_i7_keyIcon)
        - [5.1.2.8.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyWidth](#modules_items_anyOf_i1_oneOf_i7_keyWidth)
        - [5.1.2.8.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > outputColor](#modules_items_anyOf_i1_oneOf_i7_outputColor)
        - [5.1.2.8.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > format](#modules_items_anyOf_i1_oneOf_i7_format)
      - [5.1.2.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS`](#modules_items_anyOf_i1_oneOf_i8)
        - [5.1.2.9.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > type](#modules_items_anyOf_i1_oneOf_i8_type)
        - [5.1.2.9.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > percent](#modules_items_anyOf_i1_oneOf_i8_percent)
        - [5.1.2.9.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > key](#modules_items_anyOf_i1_oneOf_i8_key)
        - [5.1.2.9.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyColor](#modules_items_anyOf_i1_oneOf_i8_keyColor)
        - [5.1.2.9.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyIcon](#modules_items_anyOf_i1_oneOf_i8_keyIcon)
        - [5.1.2.9.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyWidth](#modules_items_anyOf_i1_oneOf_i8_keyWidth)
        - [5.1.2.9.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > outputColor](#modules_items_anyOf_i1_oneOf_i8_outputColor)
        - [5.1.2.9.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > format](#modules_items_anyOf_i1_oneOf_i8_format)
      - [5.1.2.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera`](#modules_items_anyOf_i1_oneOf_i9)
        - [5.1.2.10.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > type](#modules_items_anyOf_i1_oneOf_i9_type)
        - [5.1.2.10.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > key](#modules_items_anyOf_i1_oneOf_i9_key)
        - [5.1.2.10.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyColor](#modules_items_anyOf_i1_oneOf_i9_keyColor)
        - [5.1.2.10.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyIcon](#modules_items_anyOf_i1_oneOf_i9_keyIcon)
        - [5.1.2.10.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyWidth](#modules_items_anyOf_i1_oneOf_i9_keyWidth)
        - [5.1.2.10.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > outputColor](#modules_items_anyOf_i1_oneOf_i9_outputColor)
        - [5.1.2.10.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > format](#modules_items_anyOf_i1_oneOf_i9_format)
      - [5.1.2.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis`](#modules_items_anyOf_i1_oneOf_i10)
        - [5.1.2.11.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > type](#modules_items_anyOf_i1_oneOf_i10_type)
        - [5.1.2.11.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > key](#modules_items_anyOf_i1_oneOf_i10_key)
        - [5.1.2.11.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyColor](#modules_items_anyOf_i1_oneOf_i10_keyColor)
        - [5.1.2.11.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyIcon](#modules_items_anyOf_i1_oneOf_i10_keyIcon)
        - [5.1.2.11.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyWidth](#modules_items_anyOf_i1_oneOf_i10_keyWidth)
        - [5.1.2.11.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > outputColor](#modules_items_anyOf_i1_oneOf_i10_outputColor)
        - [5.1.2.11.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > format](#modules_items_anyOf_i1_oneOf_i10_format)
      - [5.1.2.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU`](#modules_items_anyOf_i1_oneOf_i11)
        - [5.1.2.12.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > type](#modules_items_anyOf_i1_oneOf_i11_type)
        - [5.1.2.12.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > temp](#modules_items_anyOf_i1_oneOf_i11_temp)
        - [5.1.2.12.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > showPeCoreCount](#modules_items_anyOf_i1_oneOf_i11_showPeCoreCount)
        - [5.1.2.12.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > key](#modules_items_anyOf_i1_oneOf_i11_key)
        - [5.1.2.12.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyColor](#modules_items_anyOf_i1_oneOf_i11_keyColor)
        - [5.1.2.12.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyIcon](#modules_items_anyOf_i1_oneOf_i11_keyIcon)
        - [5.1.2.12.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyWidth](#modules_items_anyOf_i1_oneOf_i11_keyWidth)
        - [5.1.2.12.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > outputColor](#modules_items_anyOf_i1_oneOf_i11_outputColor)
        - [5.1.2.12.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > format](#modules_items_anyOf_i1_oneOf_i11_format)
      - [5.1.2.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache`](#modules_items_anyOf_i1_oneOf_i12)
        - [5.1.2.13.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > type](#modules_items_anyOf_i1_oneOf_i12_type)
        - [5.1.2.13.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > percent](#modules_items_anyOf_i1_oneOf_i12_percent)
        - [5.1.2.13.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > key](#modules_items_anyOf_i1_oneOf_i12_key)
        - [5.1.2.13.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyColor](#modules_items_anyOf_i1_oneOf_i12_keyColor)
        - [5.1.2.13.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyIcon](#modules_items_anyOf_i1_oneOf_i12_keyIcon)
        - [5.1.2.13.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyWidth](#modules_items_anyOf_i1_oneOf_i12_keyWidth)
        - [5.1.2.13.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > outputColor](#modules_items_anyOf_i1_oneOf_i12_outputColor)
        - [5.1.2.13.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > format](#modules_items_anyOf_i1_oneOf_i12_format)
      - [5.1.2.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage`](#modules_items_anyOf_i1_oneOf_i13)
        - [5.1.2.14.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > type](#modules_items_anyOf_i1_oneOf_i13_type)
        - [5.1.2.14.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > percent](#modules_items_anyOf_i1_oneOf_i13_percent)
        - [5.1.2.14.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > separate](#modules_items_anyOf_i1_oneOf_i13_separate)
        - [5.1.2.14.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > waitTime](#modules_items_anyOf_i1_oneOf_i13_waitTime)
        - [5.1.2.14.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > key](#modules_items_anyOf_i1_oneOf_i13_key)
        - [5.1.2.14.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyColor](#modules_items_anyOf_i1_oneOf_i13_keyColor)
        - [5.1.2.14.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyIcon](#modules_items_anyOf_i1_oneOf_i13_keyIcon)
        - [5.1.2.14.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyWidth](#modules_items_anyOf_i1_oneOf_i13_keyWidth)
        - [5.1.2.14.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > outputColor](#modules_items_anyOf_i1_oneOf_i13_outputColor)
        - [5.1.2.14.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > format](#modules_items_anyOf_i1_oneOf_i13_format)
      - [5.1.2.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors`](#modules_items_anyOf_i1_oneOf_i14)
        - [5.1.2.15.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > type](#modules_items_anyOf_i1_oneOf_i14_type)
        - [5.1.2.15.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > symbol](#modules_items_anyOf_i1_oneOf_i14_symbol)
        - [5.1.2.15.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > paddingLeft](#modules_items_anyOf_i1_oneOf_i14_paddingLeft)
        - [5.1.2.15.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block](#modules_items_anyOf_i1_oneOf_i14_block)
          - [5.1.2.15.4.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > width](#modules_items_anyOf_i1_oneOf_i14_block_width)
          - [5.1.2.15.4.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range](#modules_items_anyOf_i1_oneOf_i14_block_range)
            - [5.1.2.15.4.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range > range items](#autogenerated_heading_5)
        - [5.1.2.15.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > key](#modules_items_anyOf_i1_oneOf_i14_key)
        - [5.1.2.15.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > keyIcon](#modules_items_anyOf_i1_oneOf_i14_keyIcon)
      - [5.1.2.16. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command`](#modules_items_anyOf_i1_oneOf_i15)
        - [5.1.2.16.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > type](#modules_items_anyOf_i1_oneOf_i15_type)
        - [5.1.2.16.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > shell](#modules_items_anyOf_i1_oneOf_i15_shell)
        - [5.1.2.16.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > param](#modules_items_anyOf_i1_oneOf_i15_param)
        - [5.1.2.16.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > text](#modules_items_anyOf_i1_oneOf_i15_text)
        - [5.1.2.16.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > key](#modules_items_anyOf_i1_oneOf_i15_key)
        - [5.1.2.16.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyColor](#modules_items_anyOf_i1_oneOf_i15_keyColor)
        - [5.1.2.16.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyIcon](#modules_items_anyOf_i1_oneOf_i15_keyIcon)
        - [5.1.2.16.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyWidth](#modules_items_anyOf_i1_oneOf_i15_keyWidth)
        - [5.1.2.16.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > outputColor](#modules_items_anyOf_i1_oneOf_i15_outputColor)
        - [5.1.2.16.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > format](#modules_items_anyOf_i1_oneOf_i15_format)
      - [5.1.2.17. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor`](#modules_items_anyOf_i1_oneOf_i16)
        - [5.1.2.17.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > type](#modules_items_anyOf_i1_oneOf_i16_type)
        - [5.1.2.17.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > percent](#modules_items_anyOf_i1_oneOf_i16_percent)
        - [5.1.2.17.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > key](#modules_items_anyOf_i1_oneOf_i16_key)
        - [5.1.2.17.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyColor](#modules_items_anyOf_i1_oneOf_i16_keyColor)
        - [5.1.2.17.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyIcon](#modules_items_anyOf_i1_oneOf_i16_keyIcon)
        - [5.1.2.17.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyWidth](#modules_items_anyOf_i1_oneOf_i16_keyWidth)
        - [5.1.2.17.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > outputColor](#modules_items_anyOf_i1_oneOf_i16_outputColor)
        - [5.1.2.17.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > format](#modules_items_anyOf_i1_oneOf_i16_format)
      - [5.1.2.18. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom`](#modules_items_anyOf_i1_oneOf_i17)
        - [5.1.2.18.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > type](#modules_items_anyOf_i1_oneOf_i17_type)
        - [5.1.2.18.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > key](#modules_items_anyOf_i1_oneOf_i17_key)
        - [5.1.2.18.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyColor](#modules_items_anyOf_i1_oneOf_i17_keyColor)
        - [5.1.2.18.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyIcon](#modules_items_anyOf_i1_oneOf_i17_keyIcon)
        - [5.1.2.18.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyWidth](#modules_items_anyOf_i1_oneOf_i17_keyWidth)
        - [5.1.2.18.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > outputColor](#modules_items_anyOf_i1_oneOf_i17_outputColor)
        - [5.1.2.18.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > format](#modules_items_anyOf_i1_oneOf_i17_format)
      - [5.1.2.19. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time`](#modules_items_anyOf_i1_oneOf_i18)
        - [5.1.2.19.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > type](#modules_items_anyOf_i1_oneOf_i18_type)
        - [5.1.2.19.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > percent](#modules_items_anyOf_i1_oneOf_i18_percent)
        - [5.1.2.19.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > key](#modules_items_anyOf_i1_oneOf_i18_key)
        - [5.1.2.19.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyColor](#modules_items_anyOf_i1_oneOf_i18_keyColor)
        - [5.1.2.19.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyIcon](#modules_items_anyOf_i1_oneOf_i18_keyIcon)
        - [5.1.2.19.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyWidth](#modules_items_anyOf_i1_oneOf_i18_keyWidth)
        - [5.1.2.19.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > outputColor](#modules_items_anyOf_i1_oneOf_i18_outputColor)
        - [5.1.2.19.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > format](#modules_items_anyOf_i1_oneOf_i18_format)
      - [5.1.2.20. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display`](#modules_items_anyOf_i1_oneOf_i19)
        - [5.1.2.20.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > type](#modules_items_anyOf_i1_oneOf_i19_type)
        - [5.1.2.20.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > compactType](#modules_items_anyOf_i1_oneOf_i19_compactType)
        - [5.1.2.20.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > preciseRefreshRate](#modules_items_anyOf_i1_oneOf_i19_preciseRefreshRate)
        - [5.1.2.20.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > order](#modules_items_anyOf_i1_oneOf_i19_order)
        - [5.1.2.20.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > key](#modules_items_anyOf_i1_oneOf_i19_key)
        - [5.1.2.20.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyColor](#modules_items_anyOf_i1_oneOf_i19_keyColor)
        - [5.1.2.20.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyIcon](#modules_items_anyOf_i1_oneOf_i19_keyIcon)
        - [5.1.2.20.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyWidth](#modules_items_anyOf_i1_oneOf_i19_keyWidth)
        - [5.1.2.20.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > outputColor](#modules_items_anyOf_i1_oneOf_i19_outputColor)
        - [5.1.2.20.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > format](#modules_items_anyOf_i1_oneOf_i19_format)
      - [5.1.2.21. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk`](#modules_items_anyOf_i1_oneOf_i20)
        - [5.1.2.21.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > type](#modules_items_anyOf_i1_oneOf_i20_type)
        - [5.1.2.21.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > folders](#modules_items_anyOf_i1_oneOf_i20_folders)
        - [5.1.2.21.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showExternal](#modules_items_anyOf_i1_oneOf_i20_showExternal)
        - [5.1.2.21.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showHidden](#modules_items_anyOf_i1_oneOf_i20_showHidden)
        - [5.1.2.21.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showSubvolumes](#modules_items_anyOf_i1_oneOf_i20_showSubvolumes)
        - [5.1.2.21.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showReadOnly](#modules_items_anyOf_i1_oneOf_i20_showReadOnly)
        - [5.1.2.21.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showUnknown](#modules_items_anyOf_i1_oneOf_i20_showUnknown)
        - [5.1.2.21.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > useAvailable](#modules_items_anyOf_i1_oneOf_i20_useAvailable)
        - [5.1.2.21.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > percent](#modules_items_anyOf_i1_oneOf_i20_percent)
        - [5.1.2.21.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > key](#modules_items_anyOf_i1_oneOf_i20_key)
        - [5.1.2.21.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyColor](#modules_items_anyOf_i1_oneOf_i20_keyColor)
        - [5.1.2.21.12. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyIcon](#modules_items_anyOf_i1_oneOf_i20_keyIcon)
        - [5.1.2.21.13. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyWidth](#modules_items_anyOf_i1_oneOf_i20_keyWidth)
        - [5.1.2.21.14. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > outputColor](#modules_items_anyOf_i1_oneOf_i20_outputColor)
        - [5.1.2.21.15. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > format](#modules_items_anyOf_i1_oneOf_i20_format)
      - [5.1.2.22. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO`](#modules_items_anyOf_i1_oneOf_i21)
        - [5.1.2.22.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > type](#modules_items_anyOf_i1_oneOf_i21_type)
        - [5.1.2.22.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > namePrefix](#modules_items_anyOf_i1_oneOf_i21_namePrefix)
        - [5.1.2.22.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > detectTotal](#modules_items_anyOf_i1_oneOf_i21_detectTotal)
        - [5.1.2.22.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > waitTime](#modules_items_anyOf_i1_oneOf_i21_waitTime)
        - [5.1.2.22.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > key](#modules_items_anyOf_i1_oneOf_i21_key)
        - [5.1.2.22.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyColor](#modules_items_anyOf_i1_oneOf_i21_keyColor)
        - [5.1.2.22.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyIcon](#modules_items_anyOf_i1_oneOf_i21_keyIcon)
        - [5.1.2.22.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyWidth](#modules_items_anyOf_i1_oneOf_i21_keyWidth)
        - [5.1.2.22.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > outputColor](#modules_items_anyOf_i1_oneOf_i21_outputColor)
        - [5.1.2.22.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > format](#modules_items_anyOf_i1_oneOf_i21_format)
      - [5.1.2.23. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment`](#modules_items_anyOf_i1_oneOf_i22)
        - [5.1.2.23.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > type](#modules_items_anyOf_i1_oneOf_i22_type)
        - [5.1.2.23.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > slowVersionDetection](#modules_items_anyOf_i1_oneOf_i22_slowVersionDetection)
        - [5.1.2.23.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > key](#modules_items_anyOf_i1_oneOf_i22_key)
        - [5.1.2.23.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyColor](#modules_items_anyOf_i1_oneOf_i22_keyColor)
        - [5.1.2.23.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyIcon](#modules_items_anyOf_i1_oneOf_i22_keyIcon)
        - [5.1.2.23.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyWidth](#modules_items_anyOf_i1_oneOf_i22_keyWidth)
        - [5.1.2.23.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > outputColor](#modules_items_anyOf_i1_oneOf_i22_outputColor)
        - [5.1.2.23.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > format](#modules_items_anyOf_i1_oneOf_i22_format)
      - [5.1.2.24. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS`](#modules_items_anyOf_i1_oneOf_i23)
        - [5.1.2.24.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > type](#modules_items_anyOf_i1_oneOf_i23_type)
        - [5.1.2.24.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > showType](#modules_items_anyOf_i1_oneOf_i23_showType)
        - [5.1.2.24.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > key](#modules_items_anyOf_i1_oneOf_i23_key)
        - [5.1.2.24.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyColor](#modules_items_anyOf_i1_oneOf_i23_keyColor)
        - [5.1.2.24.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyIcon](#modules_items_anyOf_i1_oneOf_i23_keyIcon)
        - [5.1.2.24.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyWidth](#modules_items_anyOf_i1_oneOf_i23_keyWidth)
        - [5.1.2.24.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > outputColor](#modules_items_anyOf_i1_oneOf_i23_outputColor)
        - [5.1.2.24.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > format](#modules_items_anyOf_i1_oneOf_i23_format)
      - [5.1.2.25. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor`](#modules_items_anyOf_i1_oneOf_i24)
        - [5.1.2.25.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > type](#modules_items_anyOf_i1_oneOf_i24_type)
        - [5.1.2.25.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > percent](#modules_items_anyOf_i1_oneOf_i24_percent)
        - [5.1.2.25.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > key](#modules_items_anyOf_i1_oneOf_i24_key)
        - [5.1.2.25.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyColor](#modules_items_anyOf_i1_oneOf_i24_keyColor)
        - [5.1.2.25.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyIcon](#modules_items_anyOf_i1_oneOf_i24_keyIcon)
        - [5.1.2.25.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyWidth](#modules_items_anyOf_i1_oneOf_i24_keyWidth)
        - [5.1.2.25.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > outputColor](#modules_items_anyOf_i1_oneOf_i24_outputColor)
        - [5.1.2.25.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > format](#modules_items_anyOf_i1_oneOf_i24_format)
      - [5.1.2.26. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font`](#modules_items_anyOf_i1_oneOf_i25)
        - [5.1.2.26.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > type](#modules_items_anyOf_i1_oneOf_i25_type)
        - [5.1.2.26.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > percent](#modules_items_anyOf_i1_oneOf_i25_percent)
        - [5.1.2.26.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > key](#modules_items_anyOf_i1_oneOf_i25_key)
        - [5.1.2.26.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyColor](#modules_items_anyOf_i1_oneOf_i25_keyColor)
        - [5.1.2.26.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyIcon](#modules_items_anyOf_i1_oneOf_i25_keyIcon)
        - [5.1.2.26.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyWidth](#modules_items_anyOf_i1_oneOf_i25_keyWidth)
        - [5.1.2.26.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > outputColor](#modules_items_anyOf_i1_oneOf_i25_outputColor)
        - [5.1.2.26.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > format](#modules_items_anyOf_i1_oneOf_i25_format)
      - [5.1.2.27. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad`](#modules_items_anyOf_i1_oneOf_i26)
        - [5.1.2.27.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > type](#modules_items_anyOf_i1_oneOf_i26_type)
        - [5.1.2.27.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > percent](#modules_items_anyOf_i1_oneOf_i26_percent)
        - [5.1.2.27.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > key](#modules_items_anyOf_i1_oneOf_i26_key)
        - [5.1.2.27.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyColor](#modules_items_anyOf_i1_oneOf_i26_keyColor)
        - [5.1.2.27.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyIcon](#modules_items_anyOf_i1_oneOf_i26_keyIcon)
        - [5.1.2.27.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyWidth](#modules_items_anyOf_i1_oneOf_i26_keyWidth)
        - [5.1.2.27.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > outputColor](#modules_items_anyOf_i1_oneOf_i26_outputColor)
        - [5.1.2.27.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > format](#modules_items_anyOf_i1_oneOf_i26_format)
      - [5.1.2.28. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU`](#modules_items_anyOf_i1_oneOf_i27)
        - [5.1.2.28.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > type](#modules_items_anyOf_i1_oneOf_i27_type)
        - [5.1.2.28.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > temp](#modules_items_anyOf_i1_oneOf_i27_temp)
        - [5.1.2.28.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > driverSpecific](#modules_items_anyOf_i1_oneOf_i27_driverSpecific)
        - [5.1.2.28.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > detectionMethod](#modules_items_anyOf_i1_oneOf_i27_detectionMethod)
        - [5.1.2.28.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > hideType](#modules_items_anyOf_i1_oneOf_i27_hideType)
        - [5.1.2.28.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > key](#modules_items_anyOf_i1_oneOf_i27_key)
        - [5.1.2.28.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyColor](#modules_items_anyOf_i1_oneOf_i27_keyColor)
        - [5.1.2.28.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyIcon](#modules_items_anyOf_i1_oneOf_i27_keyIcon)
        - [5.1.2.28.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyWidth](#modules_items_anyOf_i1_oneOf_i27_keyWidth)
        - [5.1.2.28.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > outputColor](#modules_items_anyOf_i1_oneOf_i27_outputColor)
        - [5.1.2.28.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > format](#modules_items_anyOf_i1_oneOf_i27_format)
      - [5.1.2.29. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host`](#modules_items_anyOf_i1_oneOf_i28)
        - [5.1.2.29.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > type](#modules_items_anyOf_i1_oneOf_i28_type)
        - [5.1.2.29.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > key](#modules_items_anyOf_i1_oneOf_i28_key)
        - [5.1.2.29.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyColor](#modules_items_anyOf_i1_oneOf_i28_keyColor)
        - [5.1.2.29.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyIcon](#modules_items_anyOf_i1_oneOf_i28_keyIcon)
        - [5.1.2.29.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyWidth](#modules_items_anyOf_i1_oneOf_i28_keyWidth)
        - [5.1.2.29.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > outputColor](#modules_items_anyOf_i1_oneOf_i28_outputColor)
        - [5.1.2.29.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > format](#modules_items_anyOf_i1_oneOf_i28_format)
      - [5.1.2.30. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons`](#modules_items_anyOf_i1_oneOf_i29)
        - [5.1.2.30.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > type](#modules_items_anyOf_i1_oneOf_i29_type)
        - [5.1.2.30.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > key](#modules_items_anyOf_i1_oneOf_i29_key)
        - [5.1.2.30.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyColor](#modules_items_anyOf_i1_oneOf_i29_keyColor)
        - [5.1.2.30.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyIcon](#modules_items_anyOf_i1_oneOf_i29_keyIcon)
        - [5.1.2.30.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyWidth](#modules_items_anyOf_i1_oneOf_i29_keyWidth)
        - [5.1.2.30.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > outputColor](#modules_items_anyOf_i1_oneOf_i29_outputColor)
        - [5.1.2.30.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > format](#modules_items_anyOf_i1_oneOf_i29_format)
      - [5.1.2.31. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System`](#modules_items_anyOf_i1_oneOf_i30)
        - [5.1.2.31.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > type](#modules_items_anyOf_i1_oneOf_i30_type)
        - [5.1.2.31.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > key](#modules_items_anyOf_i1_oneOf_i30_key)
        - [5.1.2.31.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyColor](#modules_items_anyOf_i1_oneOf_i30_keyColor)
        - [5.1.2.31.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyIcon](#modules_items_anyOf_i1_oneOf_i30_keyIcon)
        - [5.1.2.31.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyWidth](#modules_items_anyOf_i1_oneOf_i30_keyWidth)
        - [5.1.2.31.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > outputColor](#modules_items_anyOf_i1_oneOf_i30_outputColor)
        - [5.1.2.31.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > format](#modules_items_anyOf_i1_oneOf_i30_format)
      - [5.1.2.32. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel`](#modules_items_anyOf_i1_oneOf_i31)
        - [5.1.2.32.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > type](#modules_items_anyOf_i1_oneOf_i31_type)
        - [5.1.2.32.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > key](#modules_items_anyOf_i1_oneOf_i31_key)
        - [5.1.2.32.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyColor](#modules_items_anyOf_i1_oneOf_i31_keyColor)
        - [5.1.2.32.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyIcon](#modules_items_anyOf_i1_oneOf_i31_keyIcon)
        - [5.1.2.32.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyWidth](#modules_items_anyOf_i1_oneOf_i31_keyWidth)
        - [5.1.2.32.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > outputColor](#modules_items_anyOf_i1_oneOf_i31_outputColor)
        - [5.1.2.32.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > format](#modules_items_anyOf_i1_oneOf_i31_format)
      - [5.1.2.33. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager`](#modules_items_anyOf_i1_oneOf_i32)
        - [5.1.2.33.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > type](#modules_items_anyOf_i1_oneOf_i32_type)
        - [5.1.2.33.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > key](#modules_items_anyOf_i1_oneOf_i32_key)
        - [5.1.2.33.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyColor](#modules_items_anyOf_i1_oneOf_i32_keyColor)
        - [5.1.2.33.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyIcon](#modules_items_anyOf_i1_oneOf_i32_keyIcon)
        - [5.1.2.33.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyWidth](#modules_items_anyOf_i1_oneOf_i32_keyWidth)
        - [5.1.2.33.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > outputColor](#modules_items_anyOf_i1_oneOf_i32_outputColor)
        - [5.1.2.33.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > format](#modules_items_anyOf_i1_oneOf_i32_format)
      - [5.1.2.34. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP`](#modules_items_anyOf_i1_oneOf_i33)
        - [5.1.2.34.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > type](#modules_items_anyOf_i1_oneOf_i33_type)
        - [5.1.2.34.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv4](#modules_items_anyOf_i1_oneOf_i33_showIpv4)
        - [5.1.2.34.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv6](#modules_items_anyOf_i1_oneOf_i33_showIpv6)
        - [5.1.2.34.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showSpeed](#modules_items_anyOf_i1_oneOf_i33_showSpeed)
        - [5.1.2.34.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMtu](#modules_items_anyOf_i1_oneOf_i33_showMtu)
        - [5.1.2.34.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMac](#modules_items_anyOf_i1_oneOf_i33_showMac)
        - [5.1.2.34.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showLoop](#modules_items_anyOf_i1_oneOf_i33_showLoop)
        - [5.1.2.34.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showPrefixLen](#modules_items_anyOf_i1_oneOf_i33_showPrefixLen)
        - [5.1.2.34.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showAllIps](#modules_items_anyOf_i1_oneOf_i33_showAllIps)
        - [5.1.2.34.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showFlags](#modules_items_anyOf_i1_oneOf_i33_showFlags)
        - [5.1.2.34.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > compact](#modules_items_anyOf_i1_oneOf_i33_compact)
        - [5.1.2.34.12. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > namePrefix](#modules_items_anyOf_i1_oneOf_i33_namePrefix)
        - [5.1.2.34.13. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > defaultRouteOnly](#modules_items_anyOf_i1_oneOf_i33_defaultRouteOnly)
        - [5.1.2.34.14. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > key](#modules_items_anyOf_i1_oneOf_i33_key)
        - [5.1.2.34.15. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyColor](#modules_items_anyOf_i1_oneOf_i33_keyColor)
        - [5.1.2.34.16. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyIcon](#modules_items_anyOf_i1_oneOf_i33_keyIcon)
        - [5.1.2.34.17. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyWidth](#modules_items_anyOf_i1_oneOf_i33_keyWidth)
        - [5.1.2.34.18. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > outputColor](#modules_items_anyOf_i1_oneOf_i33_outputColor)
        - [5.1.2.34.19. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > format](#modules_items_anyOf_i1_oneOf_i33_format)
      - [5.1.2.35. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg`](#modules_items_anyOf_i1_oneOf_i34)
        - [5.1.2.35.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > type](#modules_items_anyOf_i1_oneOf_i34_type)
        - [5.1.2.35.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > ndigits](#modules_items_anyOf_i1_oneOf_i34_ndigits)
        - [5.1.2.35.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > compact](#modules_items_anyOf_i1_oneOf_i34_compact)
        - [5.1.2.35.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > percent](#modules_items_anyOf_i1_oneOf_i34_percent)
        - [5.1.2.35.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > key](#modules_items_anyOf_i1_oneOf_i34_key)
        - [5.1.2.35.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyColor](#modules_items_anyOf_i1_oneOf_i34_keyColor)
        - [5.1.2.35.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyIcon](#modules_items_anyOf_i1_oneOf_i34_keyIcon)
        - [5.1.2.35.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyWidth](#modules_items_anyOf_i1_oneOf_i34_keyWidth)
        - [5.1.2.35.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > outputColor](#modules_items_anyOf_i1_oneOf_i34_outputColor)
        - [5.1.2.35.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > format](#modules_items_anyOf_i1_oneOf_i34_format)
      - [5.1.2.36. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale`](#modules_items_anyOf_i1_oneOf_i35)
        - [5.1.2.36.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > type](#modules_items_anyOf_i1_oneOf_i35_type)
        - [5.1.2.36.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > key](#modules_items_anyOf_i1_oneOf_i35_key)
        - [5.1.2.36.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyColor](#modules_items_anyOf_i1_oneOf_i35_keyColor)
        - [5.1.2.36.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyIcon](#modules_items_anyOf_i1_oneOf_i35_keyIcon)
        - [5.1.2.36.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyWidth](#modules_items_anyOf_i1_oneOf_i35_keyWidth)
        - [5.1.2.36.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > outputColor](#modules_items_anyOf_i1_oneOf_i35_outputColor)
        - [5.1.2.36.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > format](#modules_items_anyOf_i1_oneOf_i35_format)
      - [5.1.2.37. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media`](#modules_items_anyOf_i1_oneOf_i36)
        - [5.1.2.37.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > type](#modules_items_anyOf_i1_oneOf_i36_type)
        - [5.1.2.37.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > key](#modules_items_anyOf_i1_oneOf_i36_key)
        - [5.1.2.37.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyColor](#modules_items_anyOf_i1_oneOf_i36_keyColor)
        - [5.1.2.37.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyIcon](#modules_items_anyOf_i1_oneOf_i36_keyIcon)
        - [5.1.2.37.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyWidth](#modules_items_anyOf_i1_oneOf_i36_keyWidth)
        - [5.1.2.37.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > outputColor](#modules_items_anyOf_i1_oneOf_i36_outputColor)
        - [5.1.2.37.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > format](#modules_items_anyOf_i1_oneOf_i36_format)
      - [5.1.2.38. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory`](#modules_items_anyOf_i1_oneOf_i37)
        - [5.1.2.38.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > type](#modules_items_anyOf_i1_oneOf_i37_type)
        - [5.1.2.38.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > percent](#modules_items_anyOf_i1_oneOf_i37_percent)
        - [5.1.2.38.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > key](#modules_items_anyOf_i1_oneOf_i37_key)
        - [5.1.2.38.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyColor](#modules_items_anyOf_i1_oneOf_i37_keyColor)
        - [5.1.2.38.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyIcon](#modules_items_anyOf_i1_oneOf_i37_keyIcon)
        - [5.1.2.38.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyWidth](#modules_items_anyOf_i1_oneOf_i37_keyWidth)
        - [5.1.2.38.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > outputColor](#modules_items_anyOf_i1_oneOf_i37_outputColor)
        - [5.1.2.38.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > format](#modules_items_anyOf_i1_oneOf_i37_format)
      - [5.1.2.39. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor`](#modules_items_anyOf_i1_oneOf_i38)
        - [5.1.2.39.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > type](#modules_items_anyOf_i1_oneOf_i38_type)
        - [5.1.2.39.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > key](#modules_items_anyOf_i1_oneOf_i38_key)
        - [5.1.2.39.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyColor](#modules_items_anyOf_i1_oneOf_i38_keyColor)
        - [5.1.2.39.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyIcon](#modules_items_anyOf_i1_oneOf_i38_keyIcon)
        - [5.1.2.39.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyWidth](#modules_items_anyOf_i1_oneOf_i38_keyWidth)
        - [5.1.2.39.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > outputColor](#modules_items_anyOf_i1_oneOf_i38_outputColor)
        - [5.1.2.39.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > format](#modules_items_anyOf_i1_oneOf_i38_format)
      - [5.1.2.40. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO`](#modules_items_anyOf_i1_oneOf_i39)
        - [5.1.2.40.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > type](#modules_items_anyOf_i1_oneOf_i39_type)
        - [5.1.2.40.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > namePrefix](#modules_items_anyOf_i1_oneOf_i39_namePrefix)
        - [5.1.2.40.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > defaultRouteOnly](#modules_items_anyOf_i1_oneOf_i39_defaultRouteOnly)
        - [5.1.2.40.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > detectTotal](#modules_items_anyOf_i1_oneOf_i39_detectTotal)
        - [5.1.2.40.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > waitTime](#modules_items_anyOf_i1_oneOf_i39_waitTime)
        - [5.1.2.40.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > key](#modules_items_anyOf_i1_oneOf_i39_key)
        - [5.1.2.40.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyColor](#modules_items_anyOf_i1_oneOf_i39_keyColor)
        - [5.1.2.40.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyIcon](#modules_items_anyOf_i1_oneOf_i39_keyIcon)
        - [5.1.2.40.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyWidth](#modules_items_anyOf_i1_oneOf_i39_keyWidth)
        - [5.1.2.40.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > outputColor](#modules_items_anyOf_i1_oneOf_i39_outputColor)
        - [5.1.2.40.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > format](#modules_items_anyOf_i1_oneOf_i39_format)
      - [5.1.2.41. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL`](#modules_items_anyOf_i1_oneOf_i40)
        - [5.1.2.41.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > type](#modules_items_anyOf_i1_oneOf_i40_type)
        - [5.1.2.41.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > key](#modules_items_anyOf_i1_oneOf_i40_key)
        - [5.1.2.41.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyColor](#modules_items_anyOf_i1_oneOf_i40_keyColor)
        - [5.1.2.41.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyIcon](#modules_items_anyOf_i1_oneOf_i40_keyIcon)
        - [5.1.2.41.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyWidth](#modules_items_anyOf_i1_oneOf_i40_keyWidth)
        - [5.1.2.41.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > outputColor](#modules_items_anyOf_i1_oneOf_i40_outputColor)
        - [5.1.2.41.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > format](#modules_items_anyOf_i1_oneOf_i40_format)
      - [5.1.2.42. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL`](#modules_items_anyOf_i1_oneOf_i41)
        - [5.1.2.42.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > type](#modules_items_anyOf_i1_oneOf_i41_type)
        - [5.1.2.42.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > library](#modules_items_anyOf_i1_oneOf_i41_library)
        - [5.1.2.42.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > key](#modules_items_anyOf_i1_oneOf_i41_key)
        - [5.1.2.42.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyColor](#modules_items_anyOf_i1_oneOf_i41_keyColor)
        - [5.1.2.42.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyIcon](#modules_items_anyOf_i1_oneOf_i41_keyIcon)
        - [5.1.2.42.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyWidth](#modules_items_anyOf_i1_oneOf_i41_keyWidth)
        - [5.1.2.42.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > outputColor](#modules_items_anyOf_i1_oneOf_i41_outputColor)
        - [5.1.2.42.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > format](#modules_items_anyOf_i1_oneOf_i41_format)
      - [5.1.2.43. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System`](#modules_items_anyOf_i1_oneOf_i42)
        - [5.1.2.43.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > type](#modules_items_anyOf_i1_oneOf_i42_type)
        - [5.1.2.43.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > key](#modules_items_anyOf_i1_oneOf_i42_key)
        - [5.1.2.43.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyColor](#modules_items_anyOf_i1_oneOf_i42_keyColor)
        - [5.1.2.43.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyIcon](#modules_items_anyOf_i1_oneOf_i42_keyIcon)
        - [5.1.2.43.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyWidth](#modules_items_anyOf_i1_oneOf_i42_keyWidth)
        - [5.1.2.43.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > outputColor](#modules_items_anyOf_i1_oneOf_i42_outputColor)
        - [5.1.2.43.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > format](#modules_items_anyOf_i1_oneOf_i42_format)
      - [5.1.2.44. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages`](#modules_items_anyOf_i1_oneOf_i43)
        - [5.1.2.44.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > type](#modules_items_anyOf_i1_oneOf_i43_type)
        - [5.1.2.44.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled](#modules_items_anyOf_i1_oneOf_i43_disabled)
          - [5.1.2.44.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled > disabled items](#autogenerated_heading_6)
        - [5.1.2.44.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > key](#modules_items_anyOf_i1_oneOf_i43_key)
        - [5.1.2.44.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyColor](#modules_items_anyOf_i1_oneOf_i43_keyColor)
        - [5.1.2.44.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyIcon](#modules_items_anyOf_i1_oneOf_i43_keyIcon)
        - [5.1.2.44.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyWidth](#modules_items_anyOf_i1_oneOf_i43_keyWidth)
        - [5.1.2.44.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > outputColor](#modules_items_anyOf_i1_oneOf_i43_outputColor)
        - [5.1.2.44.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > format](#modules_items_anyOf_i1_oneOf_i43_format)
      - [5.1.2.45. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk`](#modules_items_anyOf_i1_oneOf_i44)
        - [5.1.2.45.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > type](#modules_items_anyOf_i1_oneOf_i44_type)
        - [5.1.2.45.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > namePrefix](#modules_items_anyOf_i1_oneOf_i44_namePrefix)
        - [5.1.2.45.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > temp](#modules_items_anyOf_i1_oneOf_i44_temp)
        - [5.1.2.45.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > key](#modules_items_anyOf_i1_oneOf_i44_key)
        - [5.1.2.45.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyColor](#modules_items_anyOf_i1_oneOf_i44_keyColor)
        - [5.1.2.45.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyIcon](#modules_items_anyOf_i1_oneOf_i44_keyIcon)
        - [5.1.2.45.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyWidth](#modules_items_anyOf_i1_oneOf_i44_keyWidth)
        - [5.1.2.45.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > outputColor](#modules_items_anyOf_i1_oneOf_i44_outputColor)
        - [5.1.2.45.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > format](#modules_items_anyOf_i1_oneOf_i44_format)
      - [5.1.2.46. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory`](#modules_items_anyOf_i1_oneOf_i45)
        - [5.1.2.46.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > type](#modules_items_anyOf_i1_oneOf_i45_type)
        - [5.1.2.46.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > key](#modules_items_anyOf_i1_oneOf_i45_key)
        - [5.1.2.46.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyColor](#modules_items_anyOf_i1_oneOf_i45_keyColor)
        - [5.1.2.46.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyIcon](#modules_items_anyOf_i1_oneOf_i45_keyIcon)
        - [5.1.2.46.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyWidth](#modules_items_anyOf_i1_oneOf_i45_keyWidth)
        - [5.1.2.46.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > outputColor](#modules_items_anyOf_i1_oneOf_i45_outputColor)
        - [5.1.2.46.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > format](#modules_items_anyOf_i1_oneOf_i45_format)
      - [5.1.2.47. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player`](#modules_items_anyOf_i1_oneOf_i46)
        - [5.1.2.47.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > type](#modules_items_anyOf_i1_oneOf_i46_type)
        - [5.1.2.47.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > key](#modules_items_anyOf_i1_oneOf_i46_key)
        - [5.1.2.47.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyColor](#modules_items_anyOf_i1_oneOf_i46_keyColor)
        - [5.1.2.47.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyIcon](#modules_items_anyOf_i1_oneOf_i46_keyIcon)
        - [5.1.2.47.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyWidth](#modules_items_anyOf_i1_oneOf_i46_keyWidth)
        - [5.1.2.47.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > outputColor](#modules_items_anyOf_i1_oneOf_i46_outputColor)
        - [5.1.2.47.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > format](#modules_items_anyOf_i1_oneOf_i46_format)
      - [5.1.2.48. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter`](#modules_items_anyOf_i1_oneOf_i47)
        - [5.1.2.48.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > type](#modules_items_anyOf_i1_oneOf_i47_type)
        - [5.1.2.48.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > key](#modules_items_anyOf_i1_oneOf_i47_key)
        - [5.1.2.48.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyColor](#modules_items_anyOf_i1_oneOf_i47_keyColor)
        - [5.1.2.48.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyIcon](#modules_items_anyOf_i1_oneOf_i47_keyIcon)
        - [5.1.2.48.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyWidth](#modules_items_anyOf_i1_oneOf_i47_keyWidth)
        - [5.1.2.48.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > outputColor](#modules_items_anyOf_i1_oneOf_i47_outputColor)
        - [5.1.2.48.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > format](#modules_items_anyOf_i1_oneOf_i47_format)
      - [5.1.2.49. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes`](#modules_items_anyOf_i1_oneOf_i48)
        - [5.1.2.49.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > type](#modules_items_anyOf_i1_oneOf_i48_type)
        - [5.1.2.49.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > key](#modules_items_anyOf_i1_oneOf_i48_key)
        - [5.1.2.49.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyColor](#modules_items_anyOf_i1_oneOf_i48_keyColor)
        - [5.1.2.49.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyIcon](#modules_items_anyOf_i1_oneOf_i48_keyIcon)
        - [5.1.2.49.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyWidth](#modules_items_anyOf_i1_oneOf_i48_keyWidth)
        - [5.1.2.49.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > outputColor](#modules_items_anyOf_i1_oneOf_i48_outputColor)
        - [5.1.2.49.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > format](#modules_items_anyOf_i1_oneOf_i48_format)
      - [5.1.2.50. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP`](#modules_items_anyOf_i1_oneOf_i49)
        - [5.1.2.50.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > type](#modules_items_anyOf_i1_oneOf_i49_type)
        - [5.1.2.50.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > url](#modules_items_anyOf_i1_oneOf_i49_url)
        - [5.1.2.50.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > timeout](#modules_items_anyOf_i1_oneOf_i49_timeout)
        - [5.1.2.50.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > ipv6](#modules_items_anyOf_i1_oneOf_i49_ipv6)
        - [5.1.2.50.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > key](#modules_items_anyOf_i1_oneOf_i49_key)
        - [5.1.2.50.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyColor](#modules_items_anyOf_i1_oneOf_i49_keyColor)
        - [5.1.2.50.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyIcon](#modules_items_anyOf_i1_oneOf_i49_keyIcon)
        - [5.1.2.50.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyWidth](#modules_items_anyOf_i1_oneOf_i49_keyWidth)
        - [5.1.2.50.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > outputColor](#modules_items_anyOf_i1_oneOf_i49_outputColor)
        - [5.1.2.50.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > format](#modules_items_anyOf_i1_oneOf_i49_format)
      - [5.1.2.51. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator`](#modules_items_anyOf_i1_oneOf_i50)
        - [5.1.2.51.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > type](#modules_items_anyOf_i1_oneOf_i50_type)
        - [5.1.2.51.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > string](#modules_items_anyOf_i1_oneOf_i50_string)
        - [5.1.2.51.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > outputColor](#modules_items_anyOf_i1_oneOf_i50_outputColor)
        - [5.1.2.51.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > length](#modules_items_anyOf_i1_oneOf_i50_length)
      - [5.1.2.52. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell`](#modules_items_anyOf_i1_oneOf_i51)
        - [5.1.2.52.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > type](#modules_items_anyOf_i1_oneOf_i51_type)
        - [5.1.2.52.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > key](#modules_items_anyOf_i1_oneOf_i51_key)
        - [5.1.2.52.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyColor](#modules_items_anyOf_i1_oneOf_i51_keyColor)
        - [5.1.2.52.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyIcon](#modules_items_anyOf_i1_oneOf_i51_keyIcon)
        - [5.1.2.52.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyWidth](#modules_items_anyOf_i1_oneOf_i51_keyWidth)
        - [5.1.2.52.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > outputColor](#modules_items_anyOf_i1_oneOf_i51_outputColor)
        - [5.1.2.52.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > format](#modules_items_anyOf_i1_oneOf_i51_format)
      - [5.1.2.53. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound`](#modules_items_anyOf_i1_oneOf_i52)
        - [5.1.2.53.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > type](#modules_items_anyOf_i1_oneOf_i52_type)
        - [5.1.2.53.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > soundType](#modules_items_anyOf_i1_oneOf_i52_soundType)
        - [5.1.2.53.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > percent](#modules_items_anyOf_i1_oneOf_i52_percent)
        - [5.1.2.53.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > key](#modules_items_anyOf_i1_oneOf_i52_key)
        - [5.1.2.53.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyColor](#modules_items_anyOf_i1_oneOf_i52_keyColor)
        - [5.1.2.53.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyIcon](#modules_items_anyOf_i1_oneOf_i52_keyIcon)
        - [5.1.2.53.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyWidth](#modules_items_anyOf_i1_oneOf_i52_keyWidth)
        - [5.1.2.53.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > outputColor](#modules_items_anyOf_i1_oneOf_i52_outputColor)
        - [5.1.2.53.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > format](#modules_items_anyOf_i1_oneOf_i52_format)
      - [5.1.2.54. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap`](#modules_items_anyOf_i1_oneOf_i53)
        - [5.1.2.54.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > type](#modules_items_anyOf_i1_oneOf_i53_type)
        - [5.1.2.54.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > percent](#modules_items_anyOf_i1_oneOf_i53_percent)
        - [5.1.2.54.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > key](#modules_items_anyOf_i1_oneOf_i53_key)
        - [5.1.2.54.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyColor](#modules_items_anyOf_i1_oneOf_i53_keyColor)
        - [5.1.2.54.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyIcon](#modules_items_anyOf_i1_oneOf_i53_keyIcon)
        - [5.1.2.54.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyWidth](#modules_items_anyOf_i1_oneOf_i53_keyWidth)
        - [5.1.2.54.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > outputColor](#modules_items_anyOf_i1_oneOf_i53_outputColor)
        - [5.1.2.54.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > format](#modules_items_anyOf_i1_oneOf_i53_format)
      - [5.1.2.55. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal`](#modules_items_anyOf_i1_oneOf_i54)
        - [5.1.2.55.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > type](#modules_items_anyOf_i1_oneOf_i54_type)
        - [5.1.2.55.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > key](#modules_items_anyOf_i1_oneOf_i54_key)
        - [5.1.2.55.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyColor](#modules_items_anyOf_i1_oneOf_i54_keyColor)
        - [5.1.2.55.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyIcon](#modules_items_anyOf_i1_oneOf_i54_keyIcon)
        - [5.1.2.55.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyWidth](#modules_items_anyOf_i1_oneOf_i54_keyWidth)
        - [5.1.2.55.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > outputColor](#modules_items_anyOf_i1_oneOf_i54_outputColor)
        - [5.1.2.55.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > format](#modules_items_anyOf_i1_oneOf_i54_format)
      - [5.1.2.56. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font`](#modules_items_anyOf_i1_oneOf_i55)
        - [5.1.2.56.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > type](#modules_items_anyOf_i1_oneOf_i55_type)
        - [5.1.2.56.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > key](#modules_items_anyOf_i1_oneOf_i55_key)
        - [5.1.2.56.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyColor](#modules_items_anyOf_i1_oneOf_i55_keyColor)
        - [5.1.2.56.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyIcon](#modules_items_anyOf_i1_oneOf_i55_keyIcon)
        - [5.1.2.56.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyWidth](#modules_items_anyOf_i1_oneOf_i55_keyWidth)
        - [5.1.2.56.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > outputColor](#modules_items_anyOf_i1_oneOf_i55_outputColor)
        - [5.1.2.56.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > format](#modules_items_anyOf_i1_oneOf_i55_format)
      - [5.1.2.57. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size`](#modules_items_anyOf_i1_oneOf_i56)
        - [5.1.2.57.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > type](#modules_items_anyOf_i1_oneOf_i56_type)
        - [5.1.2.57.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > key](#modules_items_anyOf_i1_oneOf_i56_key)
        - [5.1.2.57.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyColor](#modules_items_anyOf_i1_oneOf_i56_keyColor)
        - [5.1.2.57.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyIcon](#modules_items_anyOf_i1_oneOf_i56_keyIcon)
        - [5.1.2.57.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyWidth](#modules_items_anyOf_i1_oneOf_i56_keyWidth)
        - [5.1.2.57.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > outputColor](#modules_items_anyOf_i1_oneOf_i56_outputColor)
        - [5.1.2.57.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > format](#modules_items_anyOf_i1_oneOf_i56_format)
      - [5.1.2.58. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme`](#modules_items_anyOf_i1_oneOf_i57)
        - [5.1.2.58.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > type](#modules_items_anyOf_i1_oneOf_i57_type)
        - [5.1.2.58.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > key](#modules_items_anyOf_i1_oneOf_i57_key)
        - [5.1.2.58.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyColor](#modules_items_anyOf_i1_oneOf_i57_keyColor)
        - [5.1.2.58.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyIcon](#modules_items_anyOf_i1_oneOf_i57_keyIcon)
        - [5.1.2.58.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyWidth](#modules_items_anyOf_i1_oneOf_i57_keyWidth)
        - [5.1.2.58.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > outputColor](#modules_items_anyOf_i1_oneOf_i57_outputColor)
        - [5.1.2.58.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > format](#modules_items_anyOf_i1_oneOf_i57_format)
      - [5.1.2.59. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme`](#modules_items_anyOf_i1_oneOf_i58)
        - [5.1.2.59.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > type](#modules_items_anyOf_i1_oneOf_i58_type)
        - [5.1.2.59.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > key](#modules_items_anyOf_i1_oneOf_i58_key)
        - [5.1.2.59.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyColor](#modules_items_anyOf_i1_oneOf_i58_keyColor)
        - [5.1.2.59.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyIcon](#modules_items_anyOf_i1_oneOf_i58_keyIcon)
        - [5.1.2.59.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyWidth](#modules_items_anyOf_i1_oneOf_i58_keyWidth)
        - [5.1.2.59.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > outputColor](#modules_items_anyOf_i1_oneOf_i58_outputColor)
        - [5.1.2.59.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > format](#modules_items_anyOf_i1_oneOf_i58_format)
      - [5.1.2.60. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title`](#modules_items_anyOf_i1_oneOf_i59)
        - [5.1.2.60.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > type](#modules_items_anyOf_i1_oneOf_i59_type)
        - [5.1.2.60.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > fqdn](#modules_items_anyOf_i1_oneOf_i59_fqdn)
        - [5.1.2.60.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color](#modules_items_anyOf_i1_oneOf_i59_color)
          - [5.1.2.60.3.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > user](#modules_items_anyOf_i1_oneOf_i59_color_user)
          - [5.1.2.60.3.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > at](#modules_items_anyOf_i1_oneOf_i59_color_at)
          - [5.1.2.60.3.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > host](#modules_items_anyOf_i1_oneOf_i59_color_host)
        - [5.1.2.60.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > key](#modules_items_anyOf_i1_oneOf_i59_key)
        - [5.1.2.60.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyColor](#modules_items_anyOf_i1_oneOf_i59_keyColor)
        - [5.1.2.60.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyIcon](#modules_items_anyOf_i1_oneOf_i59_keyIcon)
        - [5.1.2.60.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyWidth](#modules_items_anyOf_i1_oneOf_i59_keyWidth)
        - [5.1.2.60.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > outputColor](#modules_items_anyOf_i1_oneOf_i59_outputColor)
        - [5.1.2.60.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > format](#modules_items_anyOf_i1_oneOf_i59_format)
      - [5.1.2.61. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM`](#modules_items_anyOf_i1_oneOf_i60)
        - [5.1.2.61.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > type](#modules_items_anyOf_i1_oneOf_i60_type)
        - [5.1.2.61.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > key](#modules_items_anyOf_i1_oneOf_i60_key)
        - [5.1.2.61.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyColor](#modules_items_anyOf_i1_oneOf_i60_keyColor)
        - [5.1.2.61.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyIcon](#modules_items_anyOf_i1_oneOf_i60_keyIcon)
        - [5.1.2.61.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyWidth](#modules_items_anyOf_i1_oneOf_i60_keyWidth)
        - [5.1.2.61.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > outputColor](#modules_items_anyOf_i1_oneOf_i60_outputColor)
        - [5.1.2.61.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > format](#modules_items_anyOf_i1_oneOf_i60_format)
      - [5.1.2.62. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users`](#modules_items_anyOf_i1_oneOf_i61)
        - [5.1.2.62.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > type](#modules_items_anyOf_i1_oneOf_i61_type)
        - [5.1.2.62.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > compact](#modules_items_anyOf_i1_oneOf_i61_compact)
        - [5.1.2.62.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > myselfOnly](#modules_items_anyOf_i1_oneOf_i61_myselfOnly)
        - [5.1.2.62.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > key](#modules_items_anyOf_i1_oneOf_i61_key)
        - [5.1.2.62.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyColor](#modules_items_anyOf_i1_oneOf_i61_keyColor)
        - [5.1.2.62.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyIcon](#modules_items_anyOf_i1_oneOf_i61_keyIcon)
        - [5.1.2.62.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyWidth](#modules_items_anyOf_i1_oneOf_i61_keyWidth)
        - [5.1.2.62.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > outputColor](#modules_items_anyOf_i1_oneOf_i61_outputColor)
        - [5.1.2.62.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > format](#modules_items_anyOf_i1_oneOf_i61_format)
      - [5.1.2.63. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime`](#modules_items_anyOf_i1_oneOf_i62)
        - [5.1.2.63.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > type](#modules_items_anyOf_i1_oneOf_i62_type)
        - [5.1.2.63.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > key](#modules_items_anyOf_i1_oneOf_i62_key)
        - [5.1.2.63.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyColor](#modules_items_anyOf_i1_oneOf_i62_keyColor)
        - [5.1.2.63.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyIcon](#modules_items_anyOf_i1_oneOf_i62_keyIcon)
        - [5.1.2.63.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyWidth](#modules_items_anyOf_i1_oneOf_i62_keyWidth)
        - [5.1.2.63.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > outputColor](#modules_items_anyOf_i1_oneOf_i62_outputColor)
        - [5.1.2.63.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > format](#modules_items_anyOf_i1_oneOf_i62_format)
      - [5.1.2.64. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version`](#modules_items_anyOf_i1_oneOf_i63)
        - [5.1.2.64.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > type](#modules_items_anyOf_i1_oneOf_i63_type)
        - [5.1.2.64.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > key](#modules_items_anyOf_i1_oneOf_i63_key)
        - [5.1.2.64.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyColor](#modules_items_anyOf_i1_oneOf_i63_keyColor)
        - [5.1.2.64.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyIcon](#modules_items_anyOf_i1_oneOf_i63_keyIcon)
        - [5.1.2.64.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyWidth](#modules_items_anyOf_i1_oneOf_i63_keyWidth)
        - [5.1.2.64.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > outputColor](#modules_items_anyOf_i1_oneOf_i63_outputColor)
        - [5.1.2.64.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > format](#modules_items_anyOf_i1_oneOf_i63_format)
      - [5.1.2.65. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan`](#modules_items_anyOf_i1_oneOf_i64)
        - [5.1.2.65.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > type](#modules_items_anyOf_i1_oneOf_i64_type)
        - [5.1.2.65.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > key](#modules_items_anyOf_i1_oneOf_i64_key)
        - [5.1.2.65.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyColor](#modules_items_anyOf_i1_oneOf_i64_keyColor)
        - [5.1.2.65.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyIcon](#modules_items_anyOf_i1_oneOf_i64_keyIcon)
        - [5.1.2.65.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyWidth](#modules_items_anyOf_i1_oneOf_i64_keyWidth)
        - [5.1.2.65.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > outputColor](#modules_items_anyOf_i1_oneOf_i64_outputColor)
        - [5.1.2.65.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > format](#modules_items_anyOf_i1_oneOf_i64_format)
      - [5.1.2.66. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper`](#modules_items_anyOf_i1_oneOf_i65)
        - [5.1.2.66.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > type](#modules_items_anyOf_i1_oneOf_i65_type)
        - [5.1.2.66.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > key](#modules_items_anyOf_i1_oneOf_i65_key)
        - [5.1.2.66.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyColor](#modules_items_anyOf_i1_oneOf_i65_keyColor)
        - [5.1.2.66.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyIcon](#modules_items_anyOf_i1_oneOf_i65_keyIcon)
        - [5.1.2.66.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyWidth](#modules_items_anyOf_i1_oneOf_i65_keyWidth)
        - [5.1.2.66.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > outputColor](#modules_items_anyOf_i1_oneOf_i65_outputColor)
        - [5.1.2.66.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > format](#modules_items_anyOf_i1_oneOf_i65_format)
      - [5.1.2.67. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather`](#modules_items_anyOf_i1_oneOf_i66)
        - [5.1.2.67.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > type](#modules_items_anyOf_i1_oneOf_i66_type)
        - [5.1.2.67.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > location](#modules_items_anyOf_i1_oneOf_i66_location)
        - [5.1.2.67.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > timeout](#modules_items_anyOf_i1_oneOf_i66_timeout)
        - [5.1.2.67.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputFormat](#modules_items_anyOf_i1_oneOf_i66_outputFormat)
        - [5.1.2.67.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > key](#modules_items_anyOf_i1_oneOf_i66_key)
        - [5.1.2.67.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyColor](#modules_items_anyOf_i1_oneOf_i66_keyColor)
        - [5.1.2.67.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyIcon](#modules_items_anyOf_i1_oneOf_i66_keyIcon)
        - [5.1.2.67.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyWidth](#modules_items_anyOf_i1_oneOf_i66_keyWidth)
        - [5.1.2.67.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputColor](#modules_items_anyOf_i1_oneOf_i66_outputColor)
        - [5.1.2.67.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > format](#modules_items_anyOf_i1_oneOf_i66_format)
      - [5.1.2.68. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi`](#modules_items_anyOf_i1_oneOf_i67)
        - [5.1.2.68.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > type](#modules_items_anyOf_i1_oneOf_i67_type)
        - [5.1.2.68.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > key](#modules_items_anyOf_i1_oneOf_i67_key)
        - [5.1.2.68.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyColor](#modules_items_anyOf_i1_oneOf_i67_keyColor)
        - [5.1.2.68.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyIcon](#modules_items_anyOf_i1_oneOf_i67_keyIcon)
        - [5.1.2.68.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyWidth](#modules_items_anyOf_i1_oneOf_i67_keyWidth)
        - [5.1.2.68.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > outputColor](#modules_items_anyOf_i1_oneOf_i67_outputColor)
        - [5.1.2.68.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > format](#modules_items_anyOf_i1_oneOf_i67_format)
      - [5.1.2.69. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager`](#modules_items_anyOf_i1_oneOf_i68)
        - [5.1.2.69.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > type](#modules_items_anyOf_i1_oneOf_i68_type)
        - [5.1.2.69.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > detectPlugin](#modules_items_anyOf_i1_oneOf_i68_detectPlugin)
        - [5.1.2.69.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > key](#modules_items_anyOf_i1_oneOf_i68_key)
        - [5.1.2.69.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyColor](#modules_items_anyOf_i1_oneOf_i68_keyColor)
        - [5.1.2.69.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyIcon](#modules_items_anyOf_i1_oneOf_i68_keyIcon)
        - [5.1.2.69.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyWidth](#modules_items_anyOf_i1_oneOf_i68_keyWidth)
        - [5.1.2.69.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > outputColor](#modules_items_anyOf_i1_oneOf_i68_outputColor)
        - [5.1.2.69.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > format](#modules_items_anyOf_i1_oneOf_i68_format)
      - [5.1.2.70. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme`](#modules_items_anyOf_i1_oneOf_i69)
        - [5.1.2.70.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > type](#modules_items_anyOf_i1_oneOf_i69_type)
        - [5.1.2.70.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > key](#modules_items_anyOf_i1_oneOf_i69_key)
        - [5.1.2.70.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyColor](#modules_items_anyOf_i1_oneOf_i69_keyColor)
        - [5.1.2.70.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyIcon](#modules_items_anyOf_i1_oneOf_i69_keyIcon)
        - [5.1.2.70.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyWidth](#modules_items_anyOf_i1_oneOf_i69_keyWidth)
        - [5.1.2.70.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > outputColor](#modules_items_anyOf_i1_oneOf_i69_outputColor)
        - [5.1.2.70.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > format](#modules_items_anyOf_i1_oneOf_i69_format)
      - [5.1.2.71. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool`](#modules_items_anyOf_i1_oneOf_i70)
        - [5.1.2.71.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > type](#modules_items_anyOf_i1_oneOf_i70_type)
        - [5.1.2.71.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > percent](#modules_items_anyOf_i1_oneOf_i70_percent)
        - [5.1.2.71.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > key](#modules_items_anyOf_i1_oneOf_i70_key)
        - [5.1.2.71.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyColor](#modules_items_anyOf_i1_oneOf_i70_keyColor)
        - [5.1.2.71.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyIcon](#modules_items_anyOf_i1_oneOf_i70_keyIcon)
        - [5.1.2.71.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyWidth](#modules_items_anyOf_i1_oneOf_i70_keyWidth)
        - [5.1.2.71.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > outputColor](#modules_items_anyOf_i1_oneOf_i70_outputColor)
        - [5.1.2.71.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > format](#modules_items_anyOf_i1_oneOf_i70_format)
      - [5.1.2.72. [Required] Property JSON config > modules > modules items > anyOf > item 1 > type](#modules_items_anyOf_i1_type)

**Title:** JSON config

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** JSON config file for fastfetch. Usually located at `~/.config/fastfetch/config.jsonc`

<details>
<summary>
<strong> <a name="schema"></a>1. [Optional] Property JSON config > $schema</strong>  

</summary>
<blockquote>

|              |                                                                             |
| ------------ | --------------------------------------------------------------------------- |
| **Type**     | `string`                                                                    |
| **Required** | No                                                                          |
| **Format**   | `uri`                                                                       |
| **Default**  | `"https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json"` |

**Description:** JSON schema URL, for JSON validation and IDE intelligence

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo"></a>2. [Optional] Property JSON config > logo</strong>  

</summary>
<blockquote>

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Fastfetch logo configurations
See also https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options

<blockquote>

| One of(Option)           |
| ------------------------ |
| [item 0](#logo_oneOf_i0) |
| [item 1](#logo_oneOf_i1) |
| [item 2](#logo_oneOf_i2) |

<blockquote>

### <a name="logo_oneOf_i0"></a>2.1. Property `JSON config > logo > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Disable logo

Specific value: `null`

</blockquote>
<blockquote>

### <a name="logo_oneOf_i1"></a>2.2. Property `JSON config > logo > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the source file of the logo

</blockquote>
<blockquote>

### <a name="logo_oneOf_i2"></a>2.3. Property `JSON config > logo > oneOf > item 2`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Fastfetch logo configurations

<details>
<summary>
<strong> <a name="logo_oneOf_i2_type"></a>2.3.1. [Optional] Property JSON config > logo > oneOf > item 2 > type</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"auto"`           |

**Description:** Set the type of the logo

Must be one of:
* "auto"
* "builtin"
* "small"
* "file"
* "file-raw"
* "data"
* "data-raw"
* "sixel"
* "kitty"
* "kitty-direct"
* "kitty-icat"
* "iterm"
* "chafa"
* "raw"
* "none"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_source"></a>2.3.2. [Optional] Property JSON config > logo > oneOf > item 2 > source</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the source file of the logo

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color"></a>2.3.3. [Optional] Property JSON config > logo > oneOf > item 2 > color</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Override colors in the logo

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_1"></a>2.3.3.1. [Optional] Property JSON config > logo > oneOf > item 2 > color > 1</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Defined in** | #/$defs/colors     |

**Description:** Color 1

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_2"></a>2.3.3.2. [Optional] Property JSON config > logo > oneOf > item 2 > color > 2</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 2

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_3"></a>2.3.3.3. [Optional] Property JSON config > logo > oneOf > item 2 > color > 3</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 3

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_4"></a>2.3.3.4. [Optional] Property JSON config > logo > oneOf > item 2 > color > 4</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 4

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_5"></a>2.3.3.5. [Optional] Property JSON config > logo > oneOf > item 2 > color > 5</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 5

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_6"></a>2.3.3.6. [Optional] Property JSON config > logo > oneOf > item 2 > color > 6</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 6

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_7"></a>2.3.3.7. [Optional] Property JSON config > logo > oneOf > item 2 > color > 7</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 7

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_8"></a>2.3.3.8. [Optional] Property JSON config > logo > oneOf > item 2 > color > 8</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 8

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_color_9"></a>2.3.3.9. [Optional] Property JSON config > logo > oneOf > item 2 > color > 9</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 9

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_width"></a>2.3.4. [Optional] Property JSON config > logo > oneOf > item 2 > width</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the width of the logo (in characters). Required for iTerm image protocol

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_height"></a>2.3.5. [Optional] Property JSON config > logo > oneOf > item 2 > height</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the height of the logo (in characters). Required for iTerm image protocol

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_padding"></a>2.3.6. [Optional] Property JSON config > logo > oneOf > item 2 > padding</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set the padding of the logo

<details>
<summary>
<strong> <a name="logo_oneOf_i2_padding_top"></a>2.3.6.1. [Optional] Property JSON config > logo > oneOf > item 2 > padding > top</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the top padding of the logo

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_padding_left"></a>2.3.6.2. [Optional] Property JSON config > logo > oneOf > item 2 > padding > left</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the left padding of the logo

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_padding_right"></a>2.3.6.3. [Optional] Property JSON config > logo > oneOf > item 2 > padding > right</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the right padding of the logo

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_printRemaining"></a>2.3.7. [Optional] Property JSON config > logo > oneOf > item 2 > printRemaining</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to print the remaining logo if it has more lines than modules to display

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_preserveAspectRatio"></a>2.3.8. [Optional] Property JSON config > logo > oneOf > item 2 > preserveAspectRatio</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to preserve the aspect ratio of the logo. Supported by iTerm image protocol only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_recache"></a>2.3.9. [Optional] Property JSON config > logo > oneOf > item 2 > recache</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** If true, regenerate image logo cache

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_position"></a>2.3.10. [Optional] Property JSON config > logo > oneOf > item 2 > position</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"left"`           |

**Description:** Set the position where the logo should be displayed

Must be one of:
* "left"
* "top"
* "right"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_chafa"></a>2.3.11. [Optional] Property JSON config > logo > oneOf > item 2 > chafa</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Chafa configuration. See chafa documentation for details

<details>
<summary>
<strong> <a name="logo_oneOf_i2_chafa_fgOnly"></a>2.3.11.1. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > fgOnly</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Produce character-cell output using foreground colors only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_chafa_symbols"></a>2.3.11.2. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > symbols</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Specify character symbols to employ in final output

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_chafa_canvasMode"></a>2.3.11.3. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > canvasMode</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Determine how colors are used in the output. This value maps to enum ChafaCanvasMode.

Must be one of:
* "TRUECOLOR"
* "INDEXED_256"
* "INDEXED_240"
* "INDEXED_16"
* "FGBG_BGFG"
* "FGBG"
* "INDEXED_8"
* "INDEXED_16_8"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_chafa_colorSpace"></a>2.3.11.4. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > colorSpace</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Set color space used for quantization. This value maps to enum ChafaColorSpace.

Must be one of:
* "RGB"
* "DIN99D"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="logo_oneOf_i2_chafa_ditherMode"></a>2.3.11.5. [Optional] Property JSON config > logo > oneOf > item 2 > chafa > ditherMode</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Set output dither mode (No effect with 24-bit color). This value maps to enum ChafaDitherMode.

Must be one of:
* "NONE"
* "ORDERED"
* "DIFFUSION"

</blockquote>
</details>

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general"></a>3. [Optional] Property JSON config > general</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Fastfetch general configurations

<details>
<summary>
<strong> <a name="general_thread"></a>3.1. [Optional] Property JSON config > general > thread</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Use separate threads for HTTP requests

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general_escapeBedrock"></a>3.2. [Optional] Property JSON config > general > escapeBedrock</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** On Bedrock Linux, whether to escape the bedrock jail

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general_playerName"></a>3.3. [Optional] Property JSON config > general > playerName</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the player to use for Media and Player modules. Linux only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general_dsForceDrm"></a>3.4. [Optional] Property JSON config > general > dsForceDrm</strong>  

</summary>
<blockquote>

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `false`          |

**Description:** Force display detection to use DRM. Linux only

<blockquote>

| One of(Option)                         |
| -------------------------------------- |
| [item 0](#general_dsForceDrm_oneOf_i0) |
| [item 1](#general_dsForceDrm_oneOf_i1) |
| [item 2](#general_dsForceDrm_oneOf_i2) |

<blockquote>

#### <a name="general_dsForceDrm_oneOf_i0"></a>3.4.1. Property `JSON config > general > dsForceDrm > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Try `wayland`, then `x11`, then `drm`

Specific value: `false`

</blockquote>
<blockquote>

#### <a name="general_dsForceDrm_oneOf_i1"></a>3.4.2. Property `JSON config > general > dsForceDrm > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Use `/sys/class/drm` only

Specific value: `"sysfs-only"`

</blockquote>
<blockquote>

#### <a name="general_dsForceDrm_oneOf_i2"></a>3.4.3. Property `JSON config > general > dsForceDrm > oneOf > item 2`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Try `libdrm` first, then `sysfs` if libdrm fails

Specific value: `true`

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general_wmiTimeout"></a>3.5. [Optional] Property JSON config > general > wmiTimeout</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `5000`    |

**Description:** Set the timeout (ms) for WMI queries, `-1` for no timeout. Windows only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general_processingTimeout"></a>3.6. [Optional] Property JSON config > general > processingTimeout</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `5000`    |

**Description:** Set the timeout (ms) when waiting for child processes, `-1` for no timeout

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general_preRun"></a>3.7. [Optional] Property JSON config > general > preRun</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** Set the command to be executed before printing logos

</blockquote>
</details>

<details>
<summary>
<strong> <a name="general_detectVersion"></a>3.8. [Optional] Property JSON config > general > detectVersion</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to detect and display component versions. Mainly for benchmarking

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display"></a>4. [Optional] Property JSON config > display</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Configure how things should be displayed

<details>
<summary>
<strong> <a name="display_stat"></a>4.1. [Optional] Property JSON config > display > stat</strong>  

</summary>
<blockquote>

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Show time usage (in ms) for individual modules with optional threshold

<blockquote>

| One of(Option)                   |
| -------------------------------- |
| [item 0](#display_stat_oneOf_i0) |
| [item 1](#display_stat_oneOf_i1) |

<blockquote>

#### <a name="display_stat_oneOf_i0"></a>4.1.1. Property `JSON config > display > stat > oneOf > item 0`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

</blockquote>
<blockquote>

#### <a name="display_stat_oneOf_i1"></a>4.1.2. Property `JSON config > display > stat > oneOf > item 1`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_pipe"></a>4.2. [Optional] Property JSON config > display > pipe</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to disable colors (auto-detected based on isatty(1) by default)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_showErrors"></a>4.3. [Optional] Property JSON config > display > showErrors</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Print occurring errors to the console. False to ignore errored modules

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_disableLinewrap"></a>4.4. [Optional] Property JSON config > display > disableLinewrap</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to disable line wrap during execution

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_hideCursor"></a>4.5. [Optional] Property JSON config > display > hideCursor</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to hide the cursor during execution

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_separator"></a>4.6. [Optional] Property JSON config > display > separator</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `": "`   |

**Description:** Set the separator between key and value

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_color"></a>4.7. [Optional] Property JSON config > display > color</strong>  

</summary>
<blockquote>

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Set the color of the keys and title

<blockquote>

| One of(Option)                    |
| --------------------------------- |
| [colors](#display_color_oneOf_i0) |
| [item 1](#display_color_oneOf_i1) |

<blockquote>

#### <a name="display_color_oneOf_i0"></a>4.7.1. Property `JSON config > display > color > oneOf > colors`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set both the colors of keys and title

</blockquote>
<blockquote>

#### <a name="display_color_oneOf_i1"></a>4.7.2. Property `JSON config > display > color > oneOf > item 1`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="display_color_oneOf_i1_keys"></a>4.7.2.1. [Optional] Property JSON config > display > color > oneOf > item 1 > keys</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the keys

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_color_oneOf_i1_title"></a>4.7.2.2. [Optional] Property JSON config > display > color > oneOf > item 1 > title</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the title

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_color_oneOf_i1_output"></a>4.7.2.3. [Optional] Property JSON config > display > color > oneOf > item 1 > output</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the module output

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_color_oneOf_i1_separator"></a>4.7.2.4. [Optional] Property JSON config > display > color > oneOf > item 1 > separator</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the key-value separator

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_brightColor"></a>4.8. [Optional] Property JSON config > display > brightColor</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Set if the keys, title and ASCII logo should be printed in bright color

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_key"></a>4.9. [Optional] Property JSON config > display > key</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how module keys should be displayed

<details>
<summary>
<strong> <a name="display_key_width"></a>4.9.1. [Optional] Property JSON config > display > key > width</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Align the width of keys to number of characters, 0 to disable

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_key_type"></a>4.9.2. [Optional] Property JSON config > display > key > type</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"string"`         |

**Description:** Set whether to show icon before string keys

Must be one of:
* "none"
* "string"
* "icon"
* "both"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_key_paddingLeft"></a>4.9.3. [Optional] Property JSON config > display > key > paddingLeft</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Set the left padding of keys

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_size"></a>4.10. [Optional] Property JSON config > display > size</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how size values should be displayed

<details>
<summary>
<strong> <a name="display_size_binaryPrefix"></a>4.10.1. [Optional] Property JSON config > display > size > binaryPrefix</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |
| **Default**  | `"iec"`     |

**Description:** Set the binary prefix to use when formatting sizes

<blockquote>

| One of(Option)                                |
| --------------------------------------------- |
| [item 0](#display_size_binaryPrefix_oneOf_i0) |
| [item 1](#display_size_binaryPrefix_oneOf_i1) |
| [item 2](#display_size_binaryPrefix_oneOf_i2) |

<blockquote>

##### <a name="display_size_binaryPrefix_oneOf_i0"></a>4.10.1.1. Property `JSON config > display > size > binaryPrefix > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** 1024 Bytes = 1 KiB, 1024 KiB = 1 MiB, ... (standard)

Specific value: `"iec"`

</blockquote>
<blockquote>

##### <a name="display_size_binaryPrefix_oneOf_i1"></a>4.10.1.2. Property `JSON config > display > size > binaryPrefix > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** 1000 Bytes = 1 kB, 1000 kB = 1 MB, ...

Specific value: `"si"`

</blockquote>
<blockquote>

##### <a name="display_size_binaryPrefix_oneOf_i2"></a>4.10.1.3. Property `JSON config > display > size > binaryPrefix > oneOf > item 2`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** 1024 Bytes = 1 KB, 1024 KB = 1 MB, ...

Specific value: `"jedec"`

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_size_maxPrefix"></a>4.10.2. [Optional] Property JSON config > display > size > maxPrefix</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"YB"`             |

**Description:** Set the largest binary prefix to use when formatting sizes

Must be one of:
* "B"
* "kB"
* "MB"
* "GB"
* "TB"
* "PB"
* "EB"
* "ZB"
* "YB"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_size_ndigits"></a>4.10.3. [Optional] Property JSON config > display > size > ndigits</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `2`       |

**Description:** Set the number of digits to keep after the decimal point when formatting sizes

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_temp"></a>4.11. [Optional] Property JSON config > display > temp</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how temperature values should be displayed

<details>
<summary>
<strong> <a name="display_temp_unit"></a>4.11.1. [Optional] Property JSON config > display > temp > unit</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"D"`              |

**Description:** Set the unit of temperature

Must be one of:
* "D"
* "Default"
* "Celsius"
* "C"
* "Fahrenheit"
* "F"
* "Kelvin"
* "K"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_temp_ndigits"></a>4.11.2. [Optional] Property JSON config > display > temp > ndigits</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `1`       |

**Description:** Set the number of digits to keep after the decimal point when formatting temperature values

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_temp_color"></a>4.11.3. [Optional] Property JSON config > display > temp > color</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set colors used in different states of temperature values

<details>
<summary>
<strong> <a name="display_temp_color_green"></a>4.11.3.1. [Optional] Property JSON config > display > temp > color > green</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"green"`          |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in green state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_temp_color_yellow"></a>4.11.3.2. [Optional] Property JSON config > display > temp > color > yellow</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_yellow"`   |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in yellow state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_temp_color_red"></a>4.11.3.3. [Optional] Property JSON config > display > temp > color > red</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_red"`      |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in red state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_bar"></a>4.12. [Optional] Property JSON config > display > bar</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set the bar configuration

<details>
<summary>
<strong> <a name="display_bar_charElapsed"></a>4.12.1. [Optional] Property JSON config > display > bar > charElapsed</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"■"`    |

**Description:** Set the character to use in elapsed part

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_bar_charTotal"></a>4.12.2. [Optional] Property JSON config > display > bar > charTotal</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"-"`    |

**Description:** Set the character to use in total part

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_bar_borderLeft"></a>4.12.3. [Optional] Property JSON config > display > bar > borderLeft</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"[ "`   |

**Description:** Set the string to use at left border

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_bar_borderRight"></a>4.12.4. [Optional] Property JSON config > display > bar > borderRight</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `" ]"`   |

**Description:** Set the string to use at right border

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_bar_width"></a>4.12.5. [Optional] Property JSON config > display > bar > width</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `10`      |

**Description:** Set the width of the bar, in number of characters

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_percent"></a>4.13. [Optional] Property JSON config > display > percent</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how percentage values should be displayed

<details>
<summary>
<strong> <a name="display_percent_type"></a>4.13.1. [Optional] Property JSON config > display > percent > type</strong>  

</summary>
<blockquote>

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `combining`         |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/percentType |

**Description:** Set the percentage output type

<blockquote>

| One of(Option)                           |
| ---------------------------------------- |
| [item 0](#display_percent_type_oneOf_i0) |
| [item 1](#display_percent_type_oneOf_i1) |

<blockquote>

##### <a name="display_percent_type_oneOf_i0"></a>4.13.1.1. Property `JSON config > display > percent > type > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `9`      |

**Description:** 0 to use global setting, 1 for percentage number, 2 for multi-color bar, 3 for both, 6 for bar only, 9 for colored number, 10 for monochrome bar

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 255 |

</blockquote>
<blockquote>

##### <a name="display_percent_type_oneOf_i1"></a>4.13.1.2. Property `JSON config > display > percent > type > oneOf > item 1`

|              |                             |
| ------------ | --------------------------- |
| **Type**     | `array of enum (of string)` |
| **Required** | No                          |
| **Default**  | `["num", "num-color"]`      |

**Description:** Array of string flags

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [item 1 items](#display_percent_type_oneOf_i1_items) | -           |

###### <a name="autogenerated_heading_2"></a>4.13.1.2.1. JSON config > display > percent > type > oneOf > item 1 > item 1 items

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "num"
* "bar"
* "hide-others"
* "num-color"
* "bar-monochrome"

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_percent_ndigits"></a>4.13.2. [Optional] Property JSON config > display > percent > ndigits</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `0`      |

**Description:** Set the number of digits to keep after the decimal point when formatting percentage numbers

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_percent_color"></a>4.13.3. [Optional] Property JSON config > display > percent > color</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set colors used in different states of percentage bars and numbers

<details>
<summary>
<strong> <a name="display_percent_color_green"></a>4.13.3.1. [Optional] Property JSON config > display > percent > color > green</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"green"`          |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in green state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_percent_color_yellow"></a>4.13.3.2. [Optional] Property JSON config > display > percent > color > yellow</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_yellow"`   |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in yellow state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_percent_color_red"></a>4.13.3.3. [Optional] Property JSON config > display > percent > color > red</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_red"`      |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in red state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_freq"></a>4.14. [Optional] Property JSON config > display > freq</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how frequency values should be displayed

<details>
<summary>
<strong> <a name="display_freq_ndigits"></a>4.14.1. [Optional] Property JSON config > display > freq > ndigits</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `2`       |

**Description:** Set the number of digits to keep after the decimal point when formatting frequency values
A positive value will show the frequency in GHz with decimal
-1 will show the frequency in MHz

| Restrictions |         |
| ------------ | ------- |
| **Minimum**  | &ge; -1 |
| **Maximum**  | &le; 9  |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_noBuffer"></a>4.15. [Optional] Property JSON config > display > noBuffer</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to disable the stdout application buffer

</blockquote>
</details>

<details>
<summary>
<strong> <a name="display_constants"></a>4.16. [Optional] Property JSON config > display > constants</strong>  

</summary>
<blockquote>

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** List of strings to be used in custom format of modules

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [constants items](#display_constants_items) | -           |

#### <a name="autogenerated_heading_3"></a>4.16.1. JSON config > display > constants > constants items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules"></a>5. [Optional] Property JSON config > modules</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Fastfetch modules to run

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [modules items](#modules_items) | -           |

### <a name="autogenerated_heading_4"></a>5.1. JSON config > modules > modules items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

<blockquote>

| Any of(Option)                    |
| --------------------------------- |
| [item 0](#modules_items_anyOf_i0) |
| [item 1](#modules_items_anyOf_i1) |

<blockquote>

#### <a name="modules_items_anyOf_i0"></a>5.1.1. Property `JSON config > modules > modules items > anyOf > item 0`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Run module with default configurations

Must be one of:
* "battery"
* "bios"
* "bluetooth"
* "bluetoothradio"
* "board"
* "bootmgr"
* "break"
* "brightness"
* "btrfs"
* "camera"
* "chassis"
* "cpu"
* "cpucache"
* "cpuusage"
* "command"
* "colors"
* "cursor"
* "datetime"
* "display"
* "disk"
* "diskio"
* "de"
* "dns"
* "editor"
* "font"
* "gamepad"
* "gpu"
* "host"
* "icons"
* "initsystem"
* "kernel"
* "lm"
* "loadavg"
* "locale"
* "localip"
* "media"
* "memory"
* "monitor"
* "netio"
* "opencl"
* "opengl"
* "os"
* "packages"
* "physicaldisk"
* "physicalmemory"
* "player"
* "poweradapter"
* "processes"
* "publicip"
* "separator"
* "shell"
* "sound"
* "swap"
* "terminal"
* "terminalfont"
* "terminalsize"
* "terminaltheme"
* "title"
* "theme"
* "tpm"
* "uptime"
* "users"
* "version"
* "vulkan"
* "wallpaper"
* "weather"
* "wm"
* "wifi"
* "wmtheme"
* "zpool"

</blockquote>
<blockquote>

#### <a name="modules_items_anyOf_i1"></a>5.1.2. Property `JSON config > modules > modules items > anyOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Run module with custom configurations

<blockquote>

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Break](#modules_items_anyOf_i1_oneOf_i0)                |
| [Battery](#modules_items_anyOf_i1_oneOf_i1)              |
| [BIOS](#modules_items_anyOf_i1_oneOf_i2)                 |
| [Bluetooth](#modules_items_anyOf_i1_oneOf_i3)            |
| [Bluetooth Radio](#modules_items_anyOf_i1_oneOf_i4)      |
| [Board](#modules_items_anyOf_i1_oneOf_i5)                |
| [Boot Manager](#modules_items_anyOf_i1_oneOf_i6)         |
| [Brightness](#modules_items_anyOf_i1_oneOf_i7)           |
| [BTRFS](#modules_items_anyOf_i1_oneOf_i8)                |
| [Camera](#modules_items_anyOf_i1_oneOf_i9)               |
| [Chassis](#modules_items_anyOf_i1_oneOf_i10)             |
| [CPU](#modules_items_anyOf_i1_oneOf_i11)                 |
| [CPU Cache](#modules_items_anyOf_i1_oneOf_i12)           |
| [CPU Usage](#modules_items_anyOf_i1_oneOf_i13)           |
| [Colors](#modules_items_anyOf_i1_oneOf_i14)              |
| [Command](#modules_items_anyOf_i1_oneOf_i15)             |
| [Cursor](#modules_items_anyOf_i1_oneOf_i16)              |
| [Custom](#modules_items_anyOf_i1_oneOf_i17)              |
| [Date Time](#modules_items_anyOf_i1_oneOf_i18)           |
| [Display](#modules_items_anyOf_i1_oneOf_i19)             |
| [Disk](#modules_items_anyOf_i1_oneOf_i20)                |
| [DiskIO](#modules_items_anyOf_i1_oneOf_i21)              |
| [Desktop Environment](#modules_items_anyOf_i1_oneOf_i22) |
| [DNS](#modules_items_anyOf_i1_oneOf_i23)                 |
| [Editor](#modules_items_anyOf_i1_oneOf_i24)              |
| [Font](#modules_items_anyOf_i1_oneOf_i25)                |
| [Gamepad](#modules_items_anyOf_i1_oneOf_i26)             |
| [GPU](#modules_items_anyOf_i1_oneOf_i27)                 |
| [Host](#modules_items_anyOf_i1_oneOf_i28)                |
| [Icons](#modules_items_anyOf_i1_oneOf_i29)               |
| [Init System](#modules_items_anyOf_i1_oneOf_i30)         |
| [Kernel](#modules_items_anyOf_i1_oneOf_i31)              |
| [Login Manager](#modules_items_anyOf_i1_oneOf_i32)       |
| [Local IP](#modules_items_anyOf_i1_oneOf_i33)            |
| [Loadavg](#modules_items_anyOf_i1_oneOf_i34)             |
| [Locale](#modules_items_anyOf_i1_oneOf_i35)              |
| [Media](#modules_items_anyOf_i1_oneOf_i36)               |
| [Memory](#modules_items_anyOf_i1_oneOf_i37)              |
| [Monitor](#modules_items_anyOf_i1_oneOf_i38)             |
| [NetIO](#modules_items_anyOf_i1_oneOf_i39)               |
| [OpenCL](#modules_items_anyOf_i1_oneOf_i40)              |
| [OpenGL](#modules_items_anyOf_i1_oneOf_i41)              |
| [Operating System](#modules_items_anyOf_i1_oneOf_i42)    |
| [Packages](#modules_items_anyOf_i1_oneOf_i43)            |
| [Physical Disk](#modules_items_anyOf_i1_oneOf_i44)       |
| [Physical Memory](#modules_items_anyOf_i1_oneOf_i45)     |
| [Player](#modules_items_anyOf_i1_oneOf_i46)              |
| [Power Adapter](#modules_items_anyOf_i1_oneOf_i47)       |
| [Processes](#modules_items_anyOf_i1_oneOf_i48)           |
| [Public IP](#modules_items_anyOf_i1_oneOf_i49)           |
| [Separator](#modules_items_anyOf_i1_oneOf_i50)           |
| [Shell](#modules_items_anyOf_i1_oneOf_i51)               |
| [Sound](#modules_items_anyOf_i1_oneOf_i52)               |
| [Swap](#modules_items_anyOf_i1_oneOf_i53)                |
| [Terminal](#modules_items_anyOf_i1_oneOf_i54)            |
| [Terminal Font](#modules_items_anyOf_i1_oneOf_i55)       |
| [Terminal Size](#modules_items_anyOf_i1_oneOf_i56)       |
| [Terminal Theme](#modules_items_anyOf_i1_oneOf_i57)      |
| [Theme](#modules_items_anyOf_i1_oneOf_i58)               |
| [Title](#modules_items_anyOf_i1_oneOf_i59)               |
| [TPM](#modules_items_anyOf_i1_oneOf_i60)                 |
| [Users](#modules_items_anyOf_i1_oneOf_i61)               |
| [Uptime](#modules_items_anyOf_i1_oneOf_i62)              |
| [Version](#modules_items_anyOf_i1_oneOf_i63)             |
| [Vulkan](#modules_items_anyOf_i1_oneOf_i64)              |
| [Wallpaper](#modules_items_anyOf_i1_oneOf_i65)           |
| [Weather](#modules_items_anyOf_i1_oneOf_i66)             |
| [Wi-Fi](#modules_items_anyOf_i1_oneOf_i67)               |
| [Window Manager](#modules_items_anyOf_i1_oneOf_i68)      |
| [WM Theme](#modules_items_anyOf_i1_oneOf_i69)            |
| [Zpool](#modules_items_anyOf_i1_oneOf_i70)               |

<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i0"></a>5.1.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Break`

**Title:** Break

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i0_type"></a>5.1.2.1.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Break > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print a empty line

Specific value: `"break"`

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i1"></a>5.1.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery`

**Title:** Battery

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_type"></a>5.1.2.2.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print battery capacity, status, etc

Specific value: `"battery"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_useSetupApi"></a>5.1.2.2.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > useSetupApi</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if `SetupAPI` should be used on Windows to detect battery info, which supports multi batteries, but slower. Windows only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_temp"></a>5.1.2.2.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp</strong>  

</summary>
<blockquote>

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `combining`         |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/temperature |

**Description:** Detect and display temperature if supported

<blockquote>

| One of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i0) |
| [item 1](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1) |

<blockquote>

###### <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i0"></a>5.1.2.2.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 0`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

</blockquote>
<blockquote>

###### <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1"></a>5.1.2.2.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_green"></a>5.1.2.2.3.2.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > green</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values (in celsius) less than green will be shown in green

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_yellow"></a>5.1.2.2.3.2.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > yellow</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values (in celsius) greater than green and less than yellow will be shown in yellow.
Values greater than yellow will be shown in red

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_percent"></a>5.1.2.2.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent</strong>  

</summary>
<blockquote>

|                           |                 |
| ------------------------- | --------------- |
| **Type**                  | `object`        |
| **Required**              | No              |
| **Additional properties** | Not allowed     |
| **Defined in**            | #/$defs/percent |

**Description:** Thresholds for percentage colors

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_percent_green"></a>5.1.2.2.4.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > green</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values less than green will be shown in green

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_percent_yellow"></a>5.1.2.2.4.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > yellow</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values greater than green and less than yellow will be shown in yellow.
Values greater than yellow will be shown in red

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_percent_type"></a>5.1.2.2.4.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > type</strong>  

</summary>
<blockquote>

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Same definition as**    | [type](#display_percent_type) |

**Description:** Set the percentage output type

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_key"></a>5.1.2.2.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > key</strong>  

</summary>
<blockquote>

|                |             |
| -------------- | ----------- |
| **Type**       | `string`    |
| **Required**   | No          |
| **Defined in** | #/$defs/key |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_keyColor"></a>5.1.2.2.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyColor</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Defined in** | #/$defs/keyColor   |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_keyIcon"></a>5.1.2.2.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyIcon</strong>  

</summary>
<blockquote>

|                |                 |
| -------------- | --------------- |
| **Type**       | `string`        |
| **Required**   | No              |
| **Defined in** | #/$defs/keyIcon |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_keyWidth"></a>5.1.2.2.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyWidth</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `integer`        |
| **Required**   | No               |
| **Default**    | `0`              |
| **Defined in** | #/$defs/keyWidth |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_outputColor"></a>5.1.2.2.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > outputColor</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `enum (of string)`  |
| **Required**   | No                  |
| **Defined in** | #/$defs/outputColor |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i1_format"></a>5.1.2.2.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/batteryFormat |

**Description:** Output format of the module `Battery`. See Wiki for formatting syntax
    1. {manufacturer}: Battery manufacturer
    2. {model-name}: Battery model name
    3. {technology}: Battery technology
    4. {capacity}: Battery capacity (percentage num)
    5. {status}: Battery status
    6. {temperature}: Battery temperature (formatted)
    7. {cycle-count}: Battery cycle count
    8. {serial}: Battery serial number
    9. {manufacture-date}: Battery manufactor date
    10. {capacity-bar}: Battery capacity (percentage bar)
    11. {time-days}: Battery time remaining days
    12. {time-hours}: Battery time remaining hours
    13. {time-minutes}: Battery time remaining minutes
    14. {time-seconds}: Battery time remaining seconds

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i2"></a>5.1.2.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS`

**Title:** BIOS

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i2_type"></a>5.1.2.3.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print information of 1st-stage bootloader (name, version, release date, etc)

Specific value: `"bios"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i2_key"></a>5.1.2.3.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i2_keyColor"></a>5.1.2.3.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i2_keyIcon"></a>5.1.2.3.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i2_keyWidth"></a>5.1.2.3.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i2_outputColor"></a>5.1.2.3.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i2_format"></a>5.1.2.3.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > format</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/biosFormat |

**Description:** Output format of the module `Bios`. See Wiki for formatting syntax
    1. {date}: Bios date
    2. {release}: Bios release
    3. {vendor}: Bios vendor
    4. {version}: Bios version
    5. {type}: Firmware type

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i3"></a>5.1.2.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth`

**Title:** Bluetooth

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_type"></a>5.1.2.4.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List (connected) bluetooth devices

Specific value: `"bluetooth"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_showDisconnected"></a>5.1.2.4.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > showDisconnected</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if disconnected bluetooth devices should be printed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_percent"></a>5.1.2.4.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_key"></a>5.1.2.4.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_keyColor"></a>5.1.2.4.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_keyIcon"></a>5.1.2.4.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_keyWidth"></a>5.1.2.4.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_outputColor"></a>5.1.2.4.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i3_format"></a>5.1.2.4.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > format</strong>  

</summary>
<blockquote>

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | No                      |
| **Defined in** | #/$defs/bluetoothFormat |

**Description:** Output format of the module `Bluetooth`. See Wiki for formatting syntax
    1. {name}: Name
    2. {address}: Address
    3. {type}: Type
    4. {battery-percentage}: Battery percentage number
    5. {connected}: Is connected
    6. {battery-percentage-bar}: Battery percentage bar

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i4"></a>5.1.2.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio`

**Title:** Bluetooth Radio

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i4_type"></a>5.1.2.5.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List bluetooth radios width supported version and vendor

Specific value: `"bluetoothradio"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i4_key"></a>5.1.2.5.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i4_keyColor"></a>5.1.2.5.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i4_keyIcon"></a>5.1.2.5.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i4_keyWidth"></a>5.1.2.5.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i4_outputColor"></a>5.1.2.5.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i4_format"></a>5.1.2.5.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > format</strong>  

</summary>
<blockquote>

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `string`                     |
| **Required**   | No                           |
| **Defined in** | #/$defs/bluetoothradioFormat |

**Description:** Output format of the module `BluetoothRadio`. See Wiki for formatting syntax
    1. {name}: Radio name for discovering
    2. {address}: Address
    3. {lmp-version}: LMP version
    4. {lmp-subversion}: LMP subversion
    5. {version}: Bluetooth version
    6. {vendor}: Vendor
    7. {discoverable}: Discoverable
    8. {connectable}: Connectable / Pairable

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i5"></a>5.1.2.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board`

**Title:** Board

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i5_type"></a>5.1.2.6.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print motherboard name and other info

Specific value: `"board"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i5_key"></a>5.1.2.6.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i5_keyColor"></a>5.1.2.6.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i5_keyIcon"></a>5.1.2.6.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i5_keyWidth"></a>5.1.2.6.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i5_outputColor"></a>5.1.2.6.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i5_format"></a>5.1.2.6.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/boardFormat |

**Description:** Output format of the module `Board`. See Wiki for formatting syntax
    1. {name}: Board name
    2. {vendor}: Board vendor
    3. {version}: Board version
    4. {serial}: Board serial number

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i6"></a>5.1.2.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager`

**Title:** Boot Manager

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i6_type"></a>5.1.2.7.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print information of 2nd-stage bootloader (name, firmware, etc)

Specific value: `"bootmgr"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i6_key"></a>5.1.2.7.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i6_keyColor"></a>5.1.2.7.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i6_keyIcon"></a>5.1.2.7.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i6_keyWidth"></a>5.1.2.7.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i6_outputColor"></a>5.1.2.7.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i6_format"></a>5.1.2.7.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/bootmgrFormat |

**Description:** Output format of the module `Bootmgr`. See Wiki for formatting syntax
    1. {name}: Name / description
    2. {firmware-path}: Firmware file path
    3. {firmware-name}: Firmware file name
    4. {secure-boot}: Is secure boot enabled
    5. {order}: Boot order

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i7"></a>5.1.2.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness`

**Title:** Brightness

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_type"></a>5.1.2.8.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current brightness level of your monitors

Specific value: `"brightness"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_percent"></a>5.1.2.8.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_ddcciSleep"></a>5.1.2.8.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > ddcciSleep</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `10`      |

**Description:** Set the sleep times (in ms) when sending DDC/CI requests.
See <https://www.ddcutil.com/performance_options/#option-sleep-multiplier> for detail

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 400 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_compact"></a>5.1.2.8.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > compact</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if multiple results should be printed in one line

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_key"></a>5.1.2.8.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_keyColor"></a>5.1.2.8.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_keyIcon"></a>5.1.2.8.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_keyWidth"></a>5.1.2.8.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_outputColor"></a>5.1.2.8.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i7_format"></a>5.1.2.8.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > format</strong>  

</summary>
<blockquote>

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `string`                 |
| **Required**   | No                       |
| **Defined in** | #/$defs/brightnessFormat |

**Description:** Output format of the module `Brightness`. See Wiki for formatting syntax
    1. {percentage}: Screen brightness (percentage num)
    2. {name}: Screen name
    3. {max}: Maximum brightness value
    4. {min}: Minimum brightness value
    5. {current}: Current brightness value
    6. {percentage-bar}: Screen brightness (percentage bar)
    7. {is-builtin}: Is built-in screen

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i8"></a>5.1.2.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS`

**Title:** BTRFS

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_type"></a>5.1.2.9.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print Linux BTRFS volumes

Specific value: `"btrfs"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_percent"></a>5.1.2.9.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_key"></a>5.1.2.9.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_keyColor"></a>5.1.2.9.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_keyIcon"></a>5.1.2.9.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_keyWidth"></a>5.1.2.9.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_outputColor"></a>5.1.2.9.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i8_format"></a>5.1.2.9.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/btrfsFormat |

**Description:** Output format of the module `Btrfs`. See Wiki for formatting syntax
    1. {name}: Name / Label
    2. {uuid}: UUID
    3. {devices}: Associated devices
    4. {features}: Enabled features
    5. {used}: Size used
    6. {allocated}: Size allocated
    7. {total}: Size total
    8. {used-percentage}: Used percentage num
    9. {allocated-percentage}: Allocated percentage num
    10. {used-percentage-bar}: Used percentage bar
    11. {allocated-percentage-bar}: Allocated percentage bar
    12. {node-size}: Node size
    13. {sector-size}: Sector size

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i9"></a>5.1.2.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera`

**Title:** Camera

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i9_type"></a>5.1.2.10.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print available cameras

Specific value: `"camera"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i9_key"></a>5.1.2.10.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i9_keyColor"></a>5.1.2.10.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i9_keyIcon"></a>5.1.2.10.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i9_keyWidth"></a>5.1.2.10.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i9_outputColor"></a>5.1.2.10.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i9_format"></a>5.1.2.10.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/cameraFormat |

**Description:** Output format of the module `Camera`. See Wiki for formatting syntax
    1. {name}: Device name
    2. {vendor}: Vendor
    3. {colorspace}: Color space
    4. {id}: Identifier
    5. {width}: Width (in px)
    6. {height}: Height (in px)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i10"></a>5.1.2.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis`

**Title:** Chassis

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i10_type"></a>5.1.2.11.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print chassis type (desktop, laptop, etc)

Specific value: `"chassis"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i10_key"></a>5.1.2.11.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i10_keyColor"></a>5.1.2.11.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i10_keyIcon"></a>5.1.2.11.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i10_keyWidth"></a>5.1.2.11.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i10_outputColor"></a>5.1.2.11.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i10_format"></a>5.1.2.11.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/chassisFormat |

**Description:** Output format of the module `Chassis`. See Wiki for formatting syntax
    1. {type}: Chassis type
    2. {vendor}: Chassis vendor
    3. {version}: Chassis version
    4. {serial}: Chassis serial number

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i11"></a>5.1.2.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU`

**Title:** CPU

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_type"></a>5.1.2.12.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print CPU name, frequency, etc

Specific value: `"cpu"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_temp"></a>5.1.2.12.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > temp</strong>  

</summary>
<blockquote>

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `combining`                                   |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [temp](#modules_items_anyOf_i1_oneOf_i1_temp) |

**Description:** Detect and display temperature if supported

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_showPeCoreCount"></a>5.1.2.12.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > showPeCoreCount</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Detect and display CPU frequency of different core types (eg. Pcore and Ecore) if supported

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_key"></a>5.1.2.12.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_keyColor"></a>5.1.2.12.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_keyIcon"></a>5.1.2.12.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_keyWidth"></a>5.1.2.12.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_outputColor"></a>5.1.2.12.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i11_format"></a>5.1.2.12.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > format</strong>  

</summary>
<blockquote>

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/cpuFormat |

**Description:** Output format of the module `CPU`. See Wiki for formatting syntax
    1. {name}: Name
    2. {vendor}: Vendor
    3. {cores-physical}: Physical core count
    4. {cores-logical}: Logical core count
    5. {cores-online}: Online core count
    6. {freq-base}: Base frequency (formatted)
    7. {freq-max}: Max frequency (formatted)
    8. {temperature}: Temperature (formatted)
    9. {core-types}: Logical core count grouped by frequency
    10. {packages}: Processor package count

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i12"></a>5.1.2.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache`

**Title:** CPU Cache

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_type"></a>5.1.2.13.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print CPU cache sizes

Specific value: `"cpucache"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_percent"></a>5.1.2.13.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_key"></a>5.1.2.13.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_keyColor"></a>5.1.2.13.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_keyIcon"></a>5.1.2.13.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_keyWidth"></a>5.1.2.13.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_outputColor"></a>5.1.2.13.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i12_format"></a>5.1.2.13.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > format</strong>  

</summary>
<blockquote>

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/cpucacheFormat |

**Description:** Output format of the module `CPUCache`. See Wiki for formatting syntax
    1. {result}: Separate result
    2. {sum}: Sum result

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i13"></a>5.1.2.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage`

**Title:** CPU Usage

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_type"></a>5.1.2.14.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print CPU usage. Costs some time to collect data

Specific value: `"cpuusage"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_percent"></a>5.1.2.14.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_separate"></a>5.1.2.14.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > separate</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Display CPU usage per CPU logical core, instead of an average result

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_waitTime"></a>5.1.2.14.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > waitTime</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `200`     |

**Description:** Wait time (in ms). CPU usage = (inUseEnd - inUseStart) / waitTime

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_key"></a>5.1.2.14.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_keyColor"></a>5.1.2.14.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_keyIcon"></a>5.1.2.14.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_keyWidth"></a>5.1.2.14.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_outputColor"></a>5.1.2.14.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i13_format"></a>5.1.2.14.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > format</strong>  

</summary>
<blockquote>

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/cpuusageFormat |

**Description:** Output format of the module `CPUUsage`. See Wiki for formatting syntax
    1. {avg}: CPU usage (percentage num, average)
    2. {max}: CPU usage (percentage num, maximum)
    3. {max-index}: CPU core index of maximum usage
    4. {min}: CPU usage (percentage num, minimum)
    5. {min-index}: CPU core index of minimum usage
    6. {avg-bar}: CPU usage (percentage bar, average)
    7. {max-bar}: CPU usage (percentage bar, maximum)
    8. {min-bar}: CPU usage (percentage bar, minimum)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i14"></a>5.1.2.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors`

**Title:** Colors

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_type"></a>5.1.2.15.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print some colored blocks

Specific value: `"colors"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_symbol"></a>5.1.2.15.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > symbol</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"background"`     |

**Description:** Set the symbol to use

Must be one of:
* "block"
* "background"
* "circle"
* "diamond"
* "triangle"
* "square"
* "star"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_paddingLeft"></a>5.1.2.15.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > paddingLeft</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Set the number of white spaces to print before the symbol

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_block"></a>5.1.2.15.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set behavior of block printing

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_block_width"></a>5.1.2.15.4.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > width</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `3`       |

**Description:** Set the block width in spaces

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_block_range"></a>5.1.2.15.4.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `array of integer` |
| **Required** | No                 |

**Description:** Set the range of colors in the blocks to print

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | 2                  |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [range items](#modules_items_anyOf_i1_oneOf_i14_block_range_items) | -           |

###### <a name="autogenerated_heading_5"></a>5.1.2.15.4.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range > range items

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

| Restrictions |         |
| ------------ | ------- |
| **Minimum**  | &ge; 0  |
| **Maximum**  | &le; 15 |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_key"></a>5.1.2.15.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i14_keyIcon"></a>5.1.2.15.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i15"></a>5.1.2.16. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command`

**Title:** Command

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_type"></a>5.1.2.16.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Running custom shell scripts

Specific value: `"command"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_shell"></a>5.1.2.16.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > shell</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the shell program to execute the command text
Default: cmd for Windows, /bin/sh for *nix

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_param"></a>5.1.2.16.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > param</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the parameter used when starting the shell
Default: /c for Windows, -c for *nix

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_text"></a>5.1.2.16.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > text</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the command text to be executed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_key"></a>5.1.2.16.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_keyColor"></a>5.1.2.16.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_keyIcon"></a>5.1.2.16.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_keyWidth"></a>5.1.2.16.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_outputColor"></a>5.1.2.16.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i15_format"></a>5.1.2.16.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/commandFormat |

**Description:** Output format of the module `Command`. See Wiki for formatting syntax
    1. {result}: Command result

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i16"></a>5.1.2.17. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor`

**Title:** Cursor

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_type"></a>5.1.2.17.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print cursor style name

Specific value: `"cursor"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_percent"></a>5.1.2.17.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_key"></a>5.1.2.17.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_keyColor"></a>5.1.2.17.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_keyIcon"></a>5.1.2.17.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_keyWidth"></a>5.1.2.17.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_outputColor"></a>5.1.2.17.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i16_format"></a>5.1.2.17.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/cursorFormat |

**Description:** Output format of the module `Cursor`. See Wiki for formatting syntax
    1. {theme}: Cursor theme
    2. {size}: Cursor size

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i17"></a>5.1.2.18. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom`

**Title:** Custom

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i17_type"></a>5.1.2.18.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print a custom string, with or without key

Specific value: `"custom"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i17_key"></a>5.1.2.18.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > key</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Leave empty not to print the key

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i17_keyColor"></a>5.1.2.18.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i17_keyIcon"></a>5.1.2.18.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i17_keyWidth"></a>5.1.2.18.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i17_outputColor"></a>5.1.2.18.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i17_format"></a>5.1.2.18.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > format</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Text to print

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i18"></a>5.1.2.19. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time`

**Title:** Date Time

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_type"></a>5.1.2.19.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current date and time

Specific value: `"datetime"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_percent"></a>5.1.2.19.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_key"></a>5.1.2.19.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_keyColor"></a>5.1.2.19.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_keyIcon"></a>5.1.2.19.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_keyWidth"></a>5.1.2.19.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_outputColor"></a>5.1.2.19.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i18_format"></a>5.1.2.19.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > format</strong>  

</summary>
<blockquote>

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/datetimeFormat |

**Description:** Output format of the module `DateTime`. See Wiki for formatting syntax
    1. {year}: Year
    2. {year-short}: Last two digits of year
    3. {month}: Month
    4. {month-pretty}: Month with leading zero
    5. {month-name}: Month name
    6. {month-name-short}: Month name short
    7. {week}: Week number on year
    8. {weekday}: Weekday
    9. {weekday-short}: Weekday short
    10. {day-in-year}: Day in year
    11. {day-in-month}: Day in month
    12. {day-in-week}: Day in week
    13. {hour}: Hour
    14. {hour-pretty}: Hour with leading zero
    15. {hour-12}: Hour 12h format
    16. {hour-12-pretty}: Hour 12h format with leading zero
    17. {minute}: Minute
    18. {minute-pretty}: Minute with leading zero
    19. {second}: Second
    20. {second-pretty}: Second with leading zero
    21. {offset-from-utc}: Offset from UTC in the ISO 8601 format
    22. {timezone-name}: Locale-dependent timezone name or abbreviation
    23. {day-pretty}: Day in month with leading zero

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i19"></a>5.1.2.20. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display`

**Title:** Display

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_type"></a>5.1.2.20.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print resolutions, refresh rates, etc

Specific value: `"display"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_compactType"></a>5.1.2.20.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > compactType</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"none"`           |

**Description:** Set if all displays should be printed in one line

Must be one of:
* "none"
* "original"
* "scaled"
* "original-with-refresh-rate"
* "scaled-with-refresh-rate"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_preciseRefreshRate"></a>5.1.2.20.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > preciseRefreshRate</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if decimal refresh rates should not be rounded into integers when printing

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_order"></a>5.1.2.20.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > order</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"none"`           |

**Description:** Set the order should be used when printing

Must be one of:
* "none"
* "asc"
* "desc"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_key"></a>5.1.2.20.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_keyColor"></a>5.1.2.20.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_keyIcon"></a>5.1.2.20.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_keyWidth"></a>5.1.2.20.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_outputColor"></a>5.1.2.20.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i19_format"></a>5.1.2.20.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/displayFormat |

**Description:** Output format of the module `Display`. See Wiki for formatting syntax
    1. {width}: Screen configured width (in pixels)
    2. {height}: Screen configured height (in pixels)
    3. {refresh-rate}: Screen configured refresh rate (in Hz)
    4. {scaled-width}: Screen scaled width (in pixels)
    5. {scaled-height}: Screen scaled height (in pixels)
    6. {name}: Screen name
    7. {type}: Screen type (Built-in or External)
    8. {rotation}: Screen rotation (in degrees)
    9. {is-primary}: True if being the primary screen
    10. {physical-width}: Screen physical width (in millimeters)
    11. {physical-height}: Screen physical height (in millimeters)
    12. {inch}: Physical diagonal length in inches
    13. {ppi}: Pixels per inch (PPI)
    14. {bit-depth}: Bits per color channel
    15. {hdr-enabled}: True if high dynamic range (HDR) mode is enabled
    16. {manufacture-year}: Year of manufacturing
    17. {manufacture-week}: Nth week of manufacturing in the year
    18. {serial}: Serial number
    19. {platform-api}: The platform API used when detecting the display
    20. {hdr-compatible}: True if the display is HDR compatible
    21. {scale-factor}: HiDPI scale factor
    22. {preferred-width}: Screen preferred width (in pixels)
    23. {preferred-height}: Screen preferred height (in pixels)
    24. {preferred-refresh-rate}: Screen preferred refresh rate (in Hz)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i20"></a>5.1.2.21. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk`

**Title:** Disk

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_type"></a>5.1.2.21.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print partitions, space usage, disk type, etc

Specific value: `"disk"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_folders"></a>5.1.2.21.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > folders</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A colon (semicolon on Windows) separated list of folder paths for the disk output
Default: auto detection using mount-points
This option overrides other `show*` options

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_showExternal"></a>5.1.2.21.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showExternal</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Set if external volume should be printed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_showHidden"></a>5.1.2.21.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showHidden</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if hidden volumes should be printed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_showSubvolumes"></a>5.1.2.21.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showSubvolumes</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if subvolumes should be printed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_showReadOnly"></a>5.1.2.21.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showReadOnly</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if read only volumes should be printed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_showUnknown"></a>5.1.2.21.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showUnknown</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if unknown (unable to detect sizes) volumes should be printed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_useAvailable"></a>5.1.2.21.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > useAvailable</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Use f_bavail (lpFreeBytesAvailableToCaller for Windows) instead of f_bfree to calculate used bytes

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_percent"></a>5.1.2.21.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_key"></a>5.1.2.21.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_keyColor"></a>5.1.2.21.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_keyIcon"></a>5.1.2.21.12. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_keyWidth"></a>5.1.2.21.13. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_outputColor"></a>5.1.2.21.14. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i20_format"></a>5.1.2.21.15. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > format</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/diskFormat |

**Description:** Output format of the module `Disk`. See Wiki for formatting syntax
    1. {size-used}: Size used
    2. {size-total}: Size total
    3. {size-percentage}: Size percentage num
    4. {files-used}: Files used
    5. {files-total}: Files total
    6. {files-percentage}: Files percentage num
    7. {is-external}: True if external volume
    8. {is-hidden}: True if hidden volume
    9. {filesystem}: Filesystem
    10. {name}: Label / name
    11. {is-readonly}: True if read-only
    12. {create-time}: Create time in local timezone
    13. {size-percentage-bar}: Size percentage bar
    14. {files-percentage-bar}: Files percentage bar
    15. {days}: Days after creation
    16. {hours}: Hours after creation
    17. {minutes}: Minutes after creation
    18. {seconds}: Seconds after creation
    19. {milliseconds}: Milliseconds after creation
    20. {mountpoint}: Mount point / drive letter
    21. {mount-from}: Mount from (device path)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i21"></a>5.1.2.22. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO`

**Title:** DiskIO

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_type"></a>5.1.2.22.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print physical disk I/O throughput

Specific value: `"diskio"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_namePrefix"></a>5.1.2.22.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > namePrefix</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show disks with given name prefix only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_detectTotal"></a>5.1.2.22.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > detectTotal</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Detect total bytes instead of current rate

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_waitTime"></a>5.1.2.22.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > waitTime</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `200`     |

**Description:** Wait time (in ms). Disk I/O = (totalBytesEnd - totalBytesStart) / waitTime

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_key"></a>5.1.2.22.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_keyColor"></a>5.1.2.22.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_keyIcon"></a>5.1.2.22.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_keyWidth"></a>5.1.2.22.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_outputColor"></a>5.1.2.22.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i21_format"></a>5.1.2.22.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/diskioFormat |

**Description:** Output format of the module `DiskIO`. See Wiki for formatting syntax
    1. {size-read}: Size of data read [per second] (formatted)
    2. {size-written}: Size of data written [per second] (formatted)
    3. {name}: Device name
    4. {dev-path}: Device raw file path
    5. {bytes-read}: Size of data read [per second] (in bytes)
    6. {bytes-written}: Size of data written [per second] (in bytes)
    7. {read-count}: Number of reads
    8. {write-count}: Number of writes

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i22"></a>5.1.2.23. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment`

**Title:** Desktop Environment

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_type"></a>5.1.2.23.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print desktop environment name

Specific value: `"de"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_slowVersionDetection"></a>5.1.2.23.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > slowVersionDetection</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

**Description:** Set if DE version should be detected with slow operations.
Should be unnecessary for most cases.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_key"></a>5.1.2.23.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_keyColor"></a>5.1.2.23.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_keyIcon"></a>5.1.2.23.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_keyWidth"></a>5.1.2.23.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_outputColor"></a>5.1.2.23.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i22_format"></a>5.1.2.23.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > format</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/deFormat |

**Description:** Output format of the module `DE`. See Wiki for formatting syntax
    1. {process-name}: DE process name
    2. {pretty-name}: DE pretty name
    3. {version}: DE version

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i23"></a>5.1.2.24. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS`

**Title:** DNS

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_type"></a>5.1.2.24.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print DNS servers

Specific value: `"dns"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_showType"></a>5.1.2.24.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > showType</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"both"`           |

**Description:** Specify the type of DNS servers should be detected

Must be one of:
* "ipv4"
* "ipv6"
* "both"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_key"></a>5.1.2.24.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_keyColor"></a>5.1.2.24.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_keyIcon"></a>5.1.2.24.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_keyWidth"></a>5.1.2.24.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_outputColor"></a>5.1.2.24.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i23_format"></a>5.1.2.24.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > format</strong>  

</summary>
<blockquote>

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/dnsFormat |

**Description:** Output format of the module `DNS`. See Wiki for formatting syntax
    1. {result}: DNS result

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i24"></a>5.1.2.25. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor`

**Title:** Editor

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_type"></a>5.1.2.25.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print information of the default editor ($VISUAL or $EDITOR)

Specific value: `"editor"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_percent"></a>5.1.2.25.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_key"></a>5.1.2.25.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_keyColor"></a>5.1.2.25.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_keyIcon"></a>5.1.2.25.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_keyWidth"></a>5.1.2.25.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_outputColor"></a>5.1.2.25.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i24_format"></a>5.1.2.25.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/editorFormat |

**Description:** Output format of the module `Editor`. See Wiki for formatting syntax
    1. {type}: Type (Visual / Editor)
    2. {name}: Name
    3. {exe-name}: Exe name of real path
    4. {full-path}: Full path of real path
    5. {version}: Version

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i25"></a>5.1.2.26. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font`

**Title:** Font

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_type"></a>5.1.2.26.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system font names

Specific value: `"font"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_percent"></a>5.1.2.26.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_key"></a>5.1.2.26.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_keyColor"></a>5.1.2.26.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_keyIcon"></a>5.1.2.26.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_keyWidth"></a>5.1.2.26.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_outputColor"></a>5.1.2.26.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i25_format"></a>5.1.2.26.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > format</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/fontFormat |

**Description:** Output format of the module `Font`. See Wiki for formatting syntax
    1. {font1}: Font 1
    2. {font2}: Font 2
    3. {font3}: Font 3
    4. {font4}: Font 4
    5. {combined}: Combined fonts for display

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i26"></a>5.1.2.27. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad`

**Title:** Gamepad

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_type"></a>5.1.2.27.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List connected gamepads

Specific value: `"gamepad"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_percent"></a>5.1.2.27.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_key"></a>5.1.2.27.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_keyColor"></a>5.1.2.27.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_keyIcon"></a>5.1.2.27.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_keyWidth"></a>5.1.2.27.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_outputColor"></a>5.1.2.27.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i26_format"></a>5.1.2.27.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/gamepadFormat |

**Description:** Output format of the module `Gamepad`. See Wiki for formatting syntax
    1. {name}: Name
    2. {serial}: Serial number
    3. {battery-percentage}: Battery percentage num
    4. {battery-percentage-bar}: Battery percentage bar

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i27"></a>5.1.2.28. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU`

**Title:** GPU

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_type"></a>5.1.2.28.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print GPU names, graphic memory size, type, etc

Specific value: `"gpu"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_temp"></a>5.1.2.28.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > temp</strong>  

</summary>
<blockquote>

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `combining`                                   |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [temp](#modules_items_anyOf_i1_oneOf_i1_temp) |

**Description:** Detect and display temperature if supported

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_driverSpecific"></a>5.1.2.28.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > driverSpecific</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Use driver specific method to detect more detailed GPU information (memory usage, core count, etc)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_detectionMethod"></a>5.1.2.28.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > detectionMethod</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"auto"`           |

**Description:** Force using a specified method to detect GPUs

Must be one of:
* "auto"
* "pci"
* "vulkan"
* "opencl"
* "opengl"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_hideType"></a>5.1.2.28.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > hideType</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"none"`           |

**Description:** Specify the type of GPUs should not be printed

Must be one of:
* "integrated"
* "discrete"
* "unknown"
* "none"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_key"></a>5.1.2.28.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_keyColor"></a>5.1.2.28.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_keyIcon"></a>5.1.2.28.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_keyWidth"></a>5.1.2.28.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_outputColor"></a>5.1.2.28.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i27_format"></a>5.1.2.28.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > format</strong>  

</summary>
<blockquote>

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/gpuFormat |

**Description:** Output format of the module `GPU`. See Wiki for formatting syntax
    1. {vendor}: GPU vendor
    2. {name}: GPU name
    3. {driver}: GPU driver
    4. {temperature}: GPU temperature
    5. {core-count}: GPU core count
    6. {type}: GPU type
    7. {dedicated-total}: GPU total dedicated memory
    8. {dedicated-used}: GPU used dedicated memory
    9. {shared-total}: GPU total shared memory
    10. {shared-used}: GPU used shared memory
    11. {platform-api}: The platform API used when detecting the GPU
    12. {frequency}: Current frequency in GHz
    13. {index}: GPU vendor specific index
    14. {dedicated-percentage-num}: Dedicated memory usage percentage num
    15. {dedicated-percentage-bar}: Dedicated memory usage percentage bar
    16. {shared-percentage-num}: Shared memory usage percentage num
    17. {shared-percentage-bar}: Shared memory usage percentage bar
    18. {core-usage-num}: Core usage percentage num
    19. {core-usage-bar}: Core usage percentage bar
    20. {memory-type}: Memory type (Windows only)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i28"></a>5.1.2.29. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host`

**Title:** Host

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i28_type"></a>5.1.2.29.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print product name of your computer

Specific value: `"host"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i28_key"></a>5.1.2.29.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i28_keyColor"></a>5.1.2.29.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i28_keyIcon"></a>5.1.2.29.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i28_keyWidth"></a>5.1.2.29.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i28_outputColor"></a>5.1.2.29.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i28_format"></a>5.1.2.29.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > format</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/hostFormat |

**Description:** Output format of the module `Host`. See Wiki for formatting syntax
    1. {family}: Product family
    2. {name}: Product name
    3. {version}: Product version
    4. {sku}: Product sku
    5. {vendor}: Product vendor
    6. {serial}: Product serial number
    7. {uuid}: Product uuid

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i29"></a>5.1.2.30. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons`

**Title:** Icons

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i29_type"></a>5.1.2.30.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print icon style name

Specific value: `"icons"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i29_key"></a>5.1.2.30.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i29_keyColor"></a>5.1.2.30.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i29_keyIcon"></a>5.1.2.30.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i29_keyWidth"></a>5.1.2.30.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i29_outputColor"></a>5.1.2.30.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i29_format"></a>5.1.2.30.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/iconsFormat |

**Description:** Output format of the module `Icons`. See Wiki for formatting syntax
    1. {icons1}: Icons part 1
    2. {icons2}: Icons part 2

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i30"></a>5.1.2.31. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System`

**Title:** Init System

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i30_type"></a>5.1.2.31.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print init system (pid 1) name and version

Specific value: `"initsystem"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i30_key"></a>5.1.2.31.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i30_keyColor"></a>5.1.2.31.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i30_keyIcon"></a>5.1.2.31.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i30_keyWidth"></a>5.1.2.31.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i30_outputColor"></a>5.1.2.31.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i30_format"></a>5.1.2.31.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > format</strong>  

</summary>
<blockquote>

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `string`                 |
| **Required**   | No                       |
| **Defined in** | #/$defs/initsystemFormat |

**Description:** Output format of the module `InitSystem`. See Wiki for formatting syntax
    1. {name}: Init system name
    2. {exe}: Init system exe path
    3. {version}: Init system version path
    4. {pid}: Init system pid

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i31"></a>5.1.2.32. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel`

**Title:** Kernel

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i31_type"></a>5.1.2.32.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system kernel version

Specific value: `"kernel"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i31_key"></a>5.1.2.32.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i31_keyColor"></a>5.1.2.32.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i31_keyIcon"></a>5.1.2.32.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i31_keyWidth"></a>5.1.2.32.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i31_outputColor"></a>5.1.2.32.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i31_format"></a>5.1.2.32.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/kernelFormat |

**Description:** Output format of the module `Kernel`. See Wiki for formatting syntax
    1. {sysname}: Sysname
    2. {release}: Release
    3. {version}: Version
    4. {arch}: Architecture
    5. {display-version}: Display version
    6. {page-size}: Page size

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i32"></a>5.1.2.33. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager`

**Title:** Login Manager

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i32_type"></a>5.1.2.33.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print login manager (desktop manager) name and version

Specific value: `"lm"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i32_key"></a>5.1.2.33.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i32_keyColor"></a>5.1.2.33.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i32_keyIcon"></a>5.1.2.33.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i32_keyWidth"></a>5.1.2.33.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i32_outputColor"></a>5.1.2.33.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i32_format"></a>5.1.2.33.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > format</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/lmFormat |

**Description:** Output format of the module `LM`. See Wiki for formatting syntax
    1. {service}: LM service
    2. {type}: LM type
    3. {version}: LM version

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i33"></a>5.1.2.34. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP`

**Title:** Local IP

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_type"></a>5.1.2.34.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List local IP addresses (v4 or v6), MAC addresses, etc

Specific value: `"localip"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showIpv4"></a>5.1.2.34.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv4</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show IPv4 addresses

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showIpv6"></a>5.1.2.34.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv6</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show IPv6 addresses

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showSpeed"></a>5.1.2.34.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showSpeed</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show ethernet rx speed

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showMtu"></a>5.1.2.34.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMtu</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show MTU

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showMac"></a>5.1.2.34.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMac</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show MAC addresses

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showLoop"></a>5.1.2.34.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showLoop</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show loop back addresses (127.0.0.1)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showPrefixLen"></a>5.1.2.34.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showPrefixLen</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show network prefix length (/N)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showAllIps"></a>5.1.2.34.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showAllIps</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show all IPs bound to the same interface.
By default only the first IP is shown

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_showFlags"></a>5.1.2.34.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showFlags</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show the interface's flags

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_compact"></a>5.1.2.34.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > compact</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show all IPs in one line

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_namePrefix"></a>5.1.2.34.12. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > namePrefix</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show IPs with given name prefix only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_defaultRouteOnly"></a>5.1.2.34.13. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > defaultRouteOnly</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show ips that are used for default routing only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_key"></a>5.1.2.34.14. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_keyColor"></a>5.1.2.34.15. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_keyIcon"></a>5.1.2.34.16. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_keyWidth"></a>5.1.2.34.17. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_outputColor"></a>5.1.2.34.18. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i33_format"></a>5.1.2.34.19. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/localipFormat |

**Description:** Output format of the module `LocalIp`. See Wiki for formatting syntax
    1. {ipv4}: IPv4 address
    2. {ipv6}: IPv6 address
    3. {mac}: MAC address
    4. {ifname}: Interface name
    5. {is-default-route}: Is default route
    6. {mtu}: MTU size in bytes
    7. {speed}: Link speed (formatted)
    8. {flags}: Interface flags

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i34"></a>5.1.2.35. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg`

**Title:** Loadavg

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_type"></a>5.1.2.35.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system load averages

Specific value: `"loadavg"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_ndigits"></a>5.1.2.35.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > ndigits</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `2`       |

**Description:** Set the number of digits to keep after the decimal point

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_compact"></a>5.1.2.35.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > compact</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show values in one line

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_percent"></a>5.1.2.35.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_key"></a>5.1.2.35.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_keyColor"></a>5.1.2.35.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_keyIcon"></a>5.1.2.35.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_keyWidth"></a>5.1.2.35.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_outputColor"></a>5.1.2.35.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i34_format"></a>5.1.2.35.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/loadavgFormat |

**Description:** Output format of the module `Loadavg`. See Wiki for formatting syntax
    1. {loadavg1}: Load average over 1min
    2. {loadavg2}: Load average over 5min
    3. {loadavg3}: Load average over 15min

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i35"></a>5.1.2.36. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale`

**Title:** Locale

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i35_type"></a>5.1.2.36.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system locale name

Specific value: `"locale"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i35_key"></a>5.1.2.36.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i35_keyColor"></a>5.1.2.36.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i35_keyIcon"></a>5.1.2.36.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i35_keyWidth"></a>5.1.2.36.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i35_outputColor"></a>5.1.2.36.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i35_format"></a>5.1.2.36.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/localeFormat |

**Description:** Output format of the module `Locale`. See Wiki for formatting syntax
    1. {result}: Locale code

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i36"></a>5.1.2.37. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media`

**Title:** Media

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i36_type"></a>5.1.2.37.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print song name of currently playing

Specific value: `"media"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i36_key"></a>5.1.2.37.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i36_keyColor"></a>5.1.2.37.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i36_keyIcon"></a>5.1.2.37.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i36_keyWidth"></a>5.1.2.37.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i36_outputColor"></a>5.1.2.37.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i36_format"></a>5.1.2.37.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/mediaFormat |

**Description:** Output format of the module `Media`. See Wiki for formatting syntax
    1. {combined}: Pretty media name
    2. {title}: Media name
    3. {artist}: Artist name
    4. {album}: Album name
    5. {status}: Status

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i37"></a>5.1.2.38. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory`

**Title:** Memory

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_type"></a>5.1.2.38.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system memory usage info

Specific value: `"memory"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_percent"></a>5.1.2.38.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_key"></a>5.1.2.38.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_keyColor"></a>5.1.2.38.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_keyIcon"></a>5.1.2.38.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_keyWidth"></a>5.1.2.38.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_outputColor"></a>5.1.2.38.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i37_format"></a>5.1.2.38.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/memoryFormat |

**Description:** Output format of the module `Memory`. See Wiki for formatting syntax
    1. {used}: Used size
    2. {total}: Total size
    3. {percentage}: Percentage used (num)
    4. {percentage-bar}: Percentage used (bar)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i38"></a>5.1.2.39. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor`

**Title:** Monitor

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i38_type"></a>5.1.2.39.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Alias of Display module (for backwards compatibility, deprecated)

Specific value: `"monitor"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i38_key"></a>5.1.2.39.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i38_keyColor"></a>5.1.2.39.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i38_keyIcon"></a>5.1.2.39.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i38_keyWidth"></a>5.1.2.39.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i38_outputColor"></a>5.1.2.39.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i38_format"></a>5.1.2.39.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/monitorFormat |

**Description:** Output format of the module `Monitor`. See Wiki for formatting syntax
    1. {name}: Display name
    2. {width}: Native resolution width in pixels
    3. {height}: Native resolution height in pixels
    4. {physical-width}: Physical width in millimeters
    5. {physical-height}: Physical height in millimeters
    6. {inch}: Physical diagonal length in inches
    7. {ppi}: Pixels per inch (PPI)
    8. {manufacture-year}: Year of manufacturing
    9. {manufacture-week}: Nth week of manufacturing in the year
    10. {serial}: Serial number
    11. {refresh-rate}: Maximum refresh rate in Hz
    12. {hdr-compatible}: True if the display is HDR compatible

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i39"></a>5.1.2.40. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO`

**Title:** NetIO

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_type"></a>5.1.2.40.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print network I/O throughput

Specific value: `"netio"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_namePrefix"></a>5.1.2.40.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > namePrefix</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show IPs with given name prefix only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_defaultRouteOnly"></a>5.1.2.40.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > defaultRouteOnly</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show ips that are used for default routing only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_detectTotal"></a>5.1.2.40.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > detectTotal</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Detect total bytes instead of current rate

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_waitTime"></a>5.1.2.40.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > waitTime</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `200`     |

**Description:** Wait time (in ms). Disk I/O = (totalBytesEnd - totalBytesStart) / waitTime

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_key"></a>5.1.2.40.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_keyColor"></a>5.1.2.40.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_keyIcon"></a>5.1.2.40.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_keyWidth"></a>5.1.2.40.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_outputColor"></a>5.1.2.40.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i39_format"></a>5.1.2.40.11. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/netioFormat |

**Description:** Output format of the module `NetIO`. See Wiki for formatting syntax
    1. {rx-size}: Size of data received [per second] (formatted)
    2. {tx-size}: Size of data sent [per second] (formatted)
    3. {ifname}: Interface name
    4. {is-default-route}: Is default route
    5. {rx-bytes}: Size of data received [per second] (in bytes)
    6. {tx-bytes}: Size of data sent [per second] (in bytes)
    7. {rx-packets}: Number of packets received [per second]
    8. {tx-packets}: Number of packets sent [per second]
    9. {rx-errors}: Number of errors received [per second]
    10. {tx-errors}: Number of errors sent [per second]
    11. {rx-drops}: Number of packets dropped when receiving [per second]
    12. {tx-drops}: Number of packets dropped when sending [per second]

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i40"></a>5.1.2.41. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL`

**Title:** OpenCL

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i40_type"></a>5.1.2.41.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print highest OpenCL version supported by the GPU

Specific value: `"opencl"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i40_key"></a>5.1.2.41.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i40_keyColor"></a>5.1.2.41.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i40_keyIcon"></a>5.1.2.41.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i40_keyWidth"></a>5.1.2.41.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i40_outputColor"></a>5.1.2.41.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i40_format"></a>5.1.2.41.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/openclFormat |

**Description:** Output format of the module `OpenCL`. See Wiki for formatting syntax
    1. {version}: Platform version
    2. {name}: Platform name
    3. {vendor}: Platform vendor

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i41"></a>5.1.2.42. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL`

**Title:** OpenGL

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_type"></a>5.1.2.42.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print highest OpenGL version supported by the GPU

Specific value: `"opengl"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_library"></a>5.1.2.42.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > library</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"auto"`           |

**Description:** Set the OpenGL context creation library to use

Must be one of:
* "auto"
* "egl"
* "glx"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_key"></a>5.1.2.42.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_keyColor"></a>5.1.2.42.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_keyIcon"></a>5.1.2.42.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_keyWidth"></a>5.1.2.42.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_outputColor"></a>5.1.2.42.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i41_format"></a>5.1.2.42.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/openglFormat |

**Description:** Output format of the module `OpenGL`. See Wiki for formatting syntax
    1. {version}: OpenGL version
    2. {renderer}: OpenGL renderer
    3. {vendor}: OpenGL vendor
    4. {slv}: OpenGL shading language version
    5. {library}: OpenGL library used

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i42"></a>5.1.2.43. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System`

**Title:** Operating System

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i42_type"></a>5.1.2.43.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print OS / or Linux distro name and version

Specific value: `"os"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i42_key"></a>5.1.2.43.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i42_keyColor"></a>5.1.2.43.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i42_keyIcon"></a>5.1.2.43.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i42_keyWidth"></a>5.1.2.43.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i42_outputColor"></a>5.1.2.43.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i42_format"></a>5.1.2.43.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > format</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/osFormat |

**Description:** Output format of the module `OS`. See Wiki for formatting syntax
    1. {sysname}: Name of the kernel
    2. {name}: Name of the OS
    3. {pretty-name}: Pretty name of the OS, if available
    4. {id}: ID of the OS
    5. {id-like}: ID like of the OS
    6. {variant}: Variant of the OS
    7. {variant-id}: Variant ID of the OS
    8. {version}: Version of the OS
    9. {version-id}: Version ID of the OS
    10. {codename}: Version codename of the OS
    11. {build-id}: Build ID of the OS
    12. {arch}: Architecture of the OS

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i43"></a>5.1.2.44. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages`

**Title:** Packages

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_type"></a>5.1.2.44.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List installed package managers and count of installed packages

Specific value: `"packages"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_disabled"></a>5.1.2.44.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled</strong>  

</summary>
<blockquote>

|              |                             |
| ------------ | --------------------------- |
| **Type**     | `array of enum (of string)` |
| **Required** | No                          |
| **Default**  | `["winget"]`                |

**Description:** List of package managers to be disabled when detecting

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [disabled items](#modules_items_anyOf_i1_oneOf_i43_disabled_items) | -           |

###### <a name="autogenerated_heading_6"></a>5.1.2.44.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled > disabled items

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "am"
* "apk"
* "brew"
* "choco"
* "dpkg"
* "emerge"
* "eopkg"
* "flatpak"
* "guix"
* "hpkg"
* "linglong"
* "lpkg"
* "lpkgbuild"
* "macports"
* "mport"
* "nix"
* "opkg"
* "pacman"
* "pacstall"
* "paludis"
* "pisi"
* "pkg"
* "pkgtool"
* "qi"
* "rpm"
* "scoop"
* "snap"
* "sorcery"
* "winget"
* "xbps"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_key"></a>5.1.2.44.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_keyColor"></a>5.1.2.44.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_keyIcon"></a>5.1.2.44.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_keyWidth"></a>5.1.2.44.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_outputColor"></a>5.1.2.44.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i43_format"></a>5.1.2.44.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > format</strong>  

</summary>
<blockquote>

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/packagesFormat |

**Description:** Output format of the module `Packages`. See Wiki for formatting syntax
    1. {all}: Number of all packages
    2. {pacman}: Number of pacman packages
    3. {pacman-branch}: Pacman branch on manjaro
    4. {dpkg}: Number of dpkg packages
    5. {rpm}: Number of rpm packages
    6. {emerge}: Number of emerge packages
    7. {eopkg}: Number of eopkg packages
    8. {xbps}: Number of xbps packages
    9. {nix-system}: Number of nix-system packages
    10. {nix-user}: Number of nix-user packages
    11. {nix-default}: Number of nix-default packages
    12. {apk}: Number of apk packages
    13. {pkg}: Number of pkg packages
    14. {flatpak-system}: Number of flatpak-system app packages
    15. {flatpak-user}: Number of flatpak-user app packages
    16. {snap}: Number of snap packages
    17. {brew}: Number of brew packages
    18. {brew-cask}: Number of brew-cask packages
    19. {macports}: Number of macports packages
    20. {scoop}: Number of scoop packages
    21. {choco}: Number of choco packages
    22. {pkgtool}: Number of pkgtool packages
    23. {paludis}: Number of paludis packages
    24. {winget}: Number of winget packages
    25. {opkg}: Number of opkg packages
    26. {am-system}: Number of am-system packages
    27. {sorcery}: Number of sorcery packages
    28. {lpkg}: Number of lpkg packages
    29. {lpkgbuild}: Number of lpkgbuild packages
    30. {guix-system}: Number of guix-system packages
    31. {guix-user}: Number of guix-user packages
    32. {guix-home}: Number of guix-home packages
    33. {linglong}: Number of linglong packages
    34. {pacstall}: Number of pacstall packages
    35. {mport}: Number of mport packages
    36. {qi}: Number of qi packages
    37. {am-user}: Number of am-user (aka appman) packages
    38. {pkgsrc}: Number of pkgsrc packages
    39. {hpkg-system}: Number of hpkg-system packages
    40. {hpkg-user}: Number of hpkg-user packages
    41. {pisi}: Number of pisi packages
    42. {soar}: Number of soar packages
    43. {nix-all}: Total number of all nix packages
    44. {flatpak-all}: Total number of all flatpak app packages
    45. {brew-all}: Total number of all brew packages
    46. {guix-all}: Total number of all guix packages
    47. {hpkg-all}: Total number of all hpkg packages

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i44"></a>5.1.2.45. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk`

**Title:** Physical Disk

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_type"></a>5.1.2.45.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print physical disk information

Specific value: `"physicaldisk"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_namePrefix"></a>5.1.2.45.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > namePrefix</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show disks with given name prefix only

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_temp"></a>5.1.2.45.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > temp</strong>  

</summary>
<blockquote>

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `combining`                                   |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [temp](#modules_items_anyOf_i1_oneOf_i1_temp) |

**Description:** Detect and display temperature if supported

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_key"></a>5.1.2.45.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_keyColor"></a>5.1.2.45.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_keyIcon"></a>5.1.2.45.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_keyWidth"></a>5.1.2.45.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_outputColor"></a>5.1.2.45.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i44_format"></a>5.1.2.45.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > format</strong>  

</summary>
<blockquote>

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/physicaldiskFormat |

**Description:** Output format of the module `PhysicalDisk`. See Wiki for formatting syntax
    1. {size}: Device size (formatted)
    2. {name}: Device name
    3. {interconnect}: Device interconnect type
    4. {dev-path}: Device raw file path
    5. {serial}: Serial number
    6. {physical-type}: Device kind (SSD or HDD)
    7. {removable-type}: Device kind (Removable or Fixed)
    8. {readonly-type}: Device kind (Read-only or Read-write)
    9. {revision}: Product revision
    10. {temperature}: Device temperature (formatted)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i45"></a>5.1.2.46. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory`

**Title:** Physical Memory

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i45_type"></a>5.1.2.46.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system physical memory devices

Specific value: `"physicalmemory"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i45_key"></a>5.1.2.46.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i45_keyColor"></a>5.1.2.46.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i45_keyIcon"></a>5.1.2.46.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i45_keyWidth"></a>5.1.2.46.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i45_outputColor"></a>5.1.2.46.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i45_format"></a>5.1.2.46.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > format</strong>  

</summary>
<blockquote>

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `string`                     |
| **Required**   | No                           |
| **Defined in** | #/$defs/physicalmemoryFormat |

**Description:** Output format of the module `PhysicalMemory`. See Wiki for formatting syntax
    1. {bytes}: Size (in bytes)
    2. {size}: Size formatted
    3. {max-speed}: Max speed (in MT/s)
    4. {running-speed}: Running speed (in MT/s)
    5. {type}: Type (DDR4, DDR5, etc.)
    6. {form-factor}: Form factor (SODIMM, DIMM, etc.)
    7. {locator}: Bank/Device Locator (BANK0/SIMM0, BANK0/SIMM1, etc.)
    8. {vendor}: Vendor
    9. {serial}: Serial number
    10. {part-number}: Part number
    11. {is-ecc-enabled}: True if ECC enabled

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i46"></a>5.1.2.47. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player`

**Title:** Player

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i46_type"></a>5.1.2.47.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print music player name

Specific value: `"player"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i46_key"></a>5.1.2.47.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i46_keyColor"></a>5.1.2.47.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i46_keyIcon"></a>5.1.2.47.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i46_keyWidth"></a>5.1.2.47.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i46_outputColor"></a>5.1.2.47.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i46_format"></a>5.1.2.47.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/playerFormat |

**Description:** Output format of the module `Player`. See Wiki for formatting syntax
    1. {player}: Pretty player name
    2. {name}: Player name
    3. {id}: Player Identifier
    4. {url}: URL name

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i47"></a>5.1.2.48. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter`

**Title:** Power Adapter

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i47_type"></a>5.1.2.48.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print power adapter name and charging watts

Specific value: `"poweradapter"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i47_key"></a>5.1.2.48.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i47_keyColor"></a>5.1.2.48.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i47_keyIcon"></a>5.1.2.48.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i47_keyWidth"></a>5.1.2.48.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i47_outputColor"></a>5.1.2.48.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i47_format"></a>5.1.2.48.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > format</strong>  

</summary>
<blockquote>

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/poweradapterFormat |

**Description:** Output format of the module `PowerAdapter`. See Wiki for formatting syntax
    1. {watts}: Power adapter watts
    2. {name}: Power adapter name
    3. {manufacturer}: Power adapter manufacturer
    4. {model}: Power adapter model
    5. {description}: Power adapter description
    6. {serial}: Power adapter serial number

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i48"></a>5.1.2.49. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes`

**Title:** Processes

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i48_type"></a>5.1.2.49.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Count running processes

Specific value: `"processes"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i48_key"></a>5.1.2.49.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i48_keyColor"></a>5.1.2.49.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i48_keyIcon"></a>5.1.2.49.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i48_keyWidth"></a>5.1.2.49.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i48_outputColor"></a>5.1.2.49.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i48_format"></a>5.1.2.49.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > format</strong>  

</summary>
<blockquote>

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | No                      |
| **Defined in** | #/$defs/processesFormat |

**Description:** Output format of the module `Processes`. See Wiki for formatting syntax
    1. {result}: Process count

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i49"></a>5.1.2.50. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP`

**Title:** Public IP

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_type"></a>5.1.2.50.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print your public IP address, etc

Specific value: `"publicip"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_url"></a>5.1.2.50.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > url</strong>  

</summary>
<blockquote>

|              |                         |
| ------------ | ----------------------- |
| **Type**     | `string`                |
| **Required** | No                      |
| **Format**   | `url`                   |
| **Default**  | `"http://ipinfo.io/ip"` |

**Description:** The URL of public IP detection server to be used. Only HTTP protocol is supported

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_timeout"></a>5.1.2.50.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > timeout</strong>  

</summary>
<blockquote>

|              |                  |
| ------------ | ---------------- |
| **Type**     | `integer`        |
| **Required** | No               |
| **Default**  | `"disabled (0)"` |

**Description:** Time in milliseconds to wait for the public ip server to respond

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_ipv6"></a>5.1.2.50.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > ipv6</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to use IPv6 for public IP detection server

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_key"></a>5.1.2.50.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_keyColor"></a>5.1.2.50.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_keyIcon"></a>5.1.2.50.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_keyWidth"></a>5.1.2.50.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_outputColor"></a>5.1.2.50.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i49_format"></a>5.1.2.50.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > format</strong>  

</summary>
<blockquote>

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/publicipFormat |

**Description:** Output format of the module `PublicIp`. See Wiki for formatting syntax
    1. {ip}: Public IP address
    2. {location}: Location

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i50"></a>5.1.2.51. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator`

**Title:** Separator

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i50_type"></a>5.1.2.51.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print a separator line

Specific value: `"separator"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i50_string"></a>5.1.2.51.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > string</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"-"`    |

**Description:** Set the string to be printed by the separator line

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i50_outputColor"></a>5.1.2.51.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Set the color of the separator line

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i50_length"></a>5.1.2.51.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > length</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Set the length of the separator line, or 0 to auto-detect

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i51"></a>5.1.2.52. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell`

**Title:** Shell

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i51_type"></a>5.1.2.52.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current shell name and version

Specific value: `"shell"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i51_key"></a>5.1.2.52.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i51_keyColor"></a>5.1.2.52.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i51_keyIcon"></a>5.1.2.52.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i51_keyWidth"></a>5.1.2.52.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i51_outputColor"></a>5.1.2.52.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i51_format"></a>5.1.2.52.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/shellFormat |

**Description:** Output format of the module `Shell`. See Wiki for formatting syntax
    1. {process-name}: Shell process name
    2. {exe}: The first argument of the command line when running the shell
    3. {exe-name}: Shell base name of arg0
    4. {version}: Shell version
    5. {pid}: Shell pid
    6. {pretty-name}: Shell pretty name
    7. {exe-path}: Shell full exe path
    8. {tty}: Shell tty used

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i52"></a>5.1.2.53. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound`

**Title:** Sound

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_type"></a>5.1.2.53.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print sound devices, volume, etc

Specific value: `"sound"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_soundType"></a>5.1.2.53.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > soundType</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"main"`           |

**Description:** Set what type of sound devices should be printed

Must be one of:
* "main"
* "active"
* "all"

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_percent"></a>5.1.2.53.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_key"></a>5.1.2.53.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_keyColor"></a>5.1.2.53.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_keyIcon"></a>5.1.2.53.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_keyWidth"></a>5.1.2.53.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_outputColor"></a>5.1.2.53.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i52_format"></a>5.1.2.53.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/soundFormat |

**Description:** Output format of the module `Sound`. See Wiki for formatting syntax
    1. {is-main}: Is main sound device
    2. {name}: Device name
    3. {volume-percentage}: Volume (in percentage num)
    4. {identifier}: Identifier
    5. {volume-percentage-bar}: Volume (in percentage bar)
    6. {platform-api}: Platform API used

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i53"></a>5.1.2.54. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap`

**Title:** Swap

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_type"></a>5.1.2.54.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print swap (paging file) space usage

Specific value: `"swap"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_percent"></a>5.1.2.54.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_key"></a>5.1.2.54.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_keyColor"></a>5.1.2.54.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_keyIcon"></a>5.1.2.54.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_keyWidth"></a>5.1.2.54.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_outputColor"></a>5.1.2.54.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i53_format"></a>5.1.2.54.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > format</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/swapFormat |

**Description:** Output format of the module `Swap`. See Wiki for formatting syntax
    1. {used}: Used size
    2. {total}: Total size
    3. {percentage}: Percentage used (num)
    4. {percentage-bar}: Percentage used (bar)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i54"></a>5.1.2.55. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal`

**Title:** Terminal

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i54_type"></a>5.1.2.55.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current terminal name and version

Specific value: `"terminal"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i54_key"></a>5.1.2.55.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i54_keyColor"></a>5.1.2.55.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i54_keyIcon"></a>5.1.2.55.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i54_keyWidth"></a>5.1.2.55.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i54_outputColor"></a>5.1.2.55.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i54_format"></a>5.1.2.55.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > format</strong>  

</summary>
<blockquote>

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/terminalFormat |

**Description:** Output format of the module `Terminal`. See Wiki for formatting syntax
    1. {process-name}: Terminal process name
    2. {exe}: The first argument of the command line when running the terminal
    3. {exe-name}: Terminal base name of arg0
    4. {pid}: Terminal pid
    5. {pretty-name}: Terminal pretty name
    6. {version}: Terminal version
    7. {exe-path}: Terminal full exe path
    8. {tty}: Terminal tty / pts used

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i55"></a>5.1.2.56. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font`

**Title:** Terminal Font

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i55_type"></a>5.1.2.56.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print font name and size used by current terminal

Specific value: `"terminalfont"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i55_key"></a>5.1.2.56.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i55_keyColor"></a>5.1.2.56.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i55_keyIcon"></a>5.1.2.56.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i55_keyWidth"></a>5.1.2.56.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i55_outputColor"></a>5.1.2.56.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i55_format"></a>5.1.2.56.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > format</strong>  

</summary>
<blockquote>

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/terminalfontFormat |

**Description:** Output format of the module `TerminalFont`. See Wiki for formatting syntax
    1. {combined}: Terminal font combined
    2. {name}: Terminal font name
    3. {size}: Terminal font size
    4. {styles}: Terminal font styles

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i56"></a>5.1.2.57. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size`

**Title:** Terminal Size

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i56_type"></a>5.1.2.57.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current terminal size

Specific value: `"terminalsize"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i56_key"></a>5.1.2.57.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i56_keyColor"></a>5.1.2.57.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i56_keyIcon"></a>5.1.2.57.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i56_keyWidth"></a>5.1.2.57.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i56_outputColor"></a>5.1.2.57.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i56_format"></a>5.1.2.57.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > format</strong>  

</summary>
<blockquote>

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/terminalsizeFormat |

**Description:** Output format of the module `TerminalSize`. See Wiki for formatting syntax
    1. {rows}: Terminal rows
    2. {columns}: Terminal columns
    3. {width}: Terminal width (in pixels)
    4. {height}: Terminal height (in pixels)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i57"></a>5.1.2.58. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme`

**Title:** Terminal Theme

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i57_type"></a>5.1.2.58.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current terminal theme (foreground and background colors)

Specific value: `"terminaltheme"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i57_key"></a>5.1.2.58.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i57_keyColor"></a>5.1.2.58.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i57_keyIcon"></a>5.1.2.58.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i57_keyWidth"></a>5.1.2.58.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i57_outputColor"></a>5.1.2.58.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i57_format"></a>5.1.2.58.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > format</strong>  

</summary>
<blockquote>

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Required**   | No                          |
| **Defined in** | #/$defs/terminalthemeFormat |

**Description:** Output format of the module `TerminalTheme`. See Wiki for formatting syntax
    1. {fg-color}: Terminal foreground color
    2. {fg-type}: Terminal foreground type (Dark / Light)
    3. {bg-color}: Terminal background color
    4. {bg-type}: Terminal background type (Dark / Light)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i58"></a>5.1.2.59. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme`

**Title:** Theme

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i58_type"></a>5.1.2.59.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current theme of desktop environment

Specific value: `"theme"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i58_key"></a>5.1.2.59.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i58_keyColor"></a>5.1.2.59.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i58_keyIcon"></a>5.1.2.59.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i58_keyWidth"></a>5.1.2.59.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i58_outputColor"></a>5.1.2.59.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i58_format"></a>5.1.2.59.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/themeFormat |

**Description:** Output format of the module `Theme`. See Wiki for formatting syntax
    1. {theme1}: Theme part 1
    2. {theme2}: Theme part 2

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i59"></a>5.1.2.60. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title`

**Title:** Title

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_type"></a>5.1.2.60.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print title, which contains your user name, hostname

Specific value: `"title"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_fqdn"></a>5.1.2.60.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > fqdn</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if the title should use fully qualified domain name

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_color"></a>5.1.2.60.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color</strong>  

</summary>
<blockquote>

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set colors of the different part of title

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_color_user"></a>5.1.2.60.3.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > user</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set color of the user name (left part)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_color_at"></a>5.1.2.60.3.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > at</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set color of the @ symbol (middle part)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_color_host"></a>5.1.2.60.3.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > host</strong>  

</summary>
<blockquote>

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set color of the host name (right part)

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_key"></a>5.1.2.60.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_keyColor"></a>5.1.2.60.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_keyIcon"></a>5.1.2.60.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_keyWidth"></a>5.1.2.60.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_outputColor"></a>5.1.2.60.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i59_format"></a>5.1.2.60.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/titleFormat |

**Description:** Output format of the module `Title`. See Wiki for formatting syntax
    1. {user-name}: User name
    2. {host-name}: Host name
    3. {home-dir}: Home directory
    4. {exe-path}: Executable path of current process
    5. {user-shell}: User's default shell
    6. {user-name-colored}: User name (colored)
    7. {at-symbol-colored}: @ symbol (colored)
    8. {host-name-colored}: Host name (colored)

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i60"></a>5.1.2.61. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM`

**Title:** TPM

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i60_type"></a>5.1.2.61.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print info of Trusted Platform Module (TPM) Security Device

Specific value: `"tpm"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i60_key"></a>5.1.2.61.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i60_keyColor"></a>5.1.2.61.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i60_keyIcon"></a>5.1.2.61.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i60_keyWidth"></a>5.1.2.61.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i60_outputColor"></a>5.1.2.61.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i60_format"></a>5.1.2.61.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > format</strong>  

</summary>
<blockquote>

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/tpmFormat |

**Description:** Output format of the module `TPM`. See Wiki for formatting syntax
    1. {version}: TPM device version
    2. {description}: TPM general description

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i61"></a>5.1.2.62. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users`

**Title:** Users

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_type"></a>5.1.2.62.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print users currently logged in

Specific value: `"users"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_compact"></a>5.1.2.62.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > compact</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show all active users in one line

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_myselfOnly"></a>5.1.2.62.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > myselfOnly</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show only the current user

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_key"></a>5.1.2.62.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_keyColor"></a>5.1.2.62.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_keyIcon"></a>5.1.2.62.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_keyWidth"></a>5.1.2.62.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_outputColor"></a>5.1.2.62.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i61_format"></a>5.1.2.62.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/usersFormat |

**Description:** Output format of the module `Users`. See Wiki for formatting syntax
    1. {name}: User name
    2. {host-name}: Host name
    3. {session}: Session name
    4. {client-ip}: Client IP
    5. {login-time}: Login Time in local timezone
    6. {days}: Days after login
    7. {hours}: Hours after login
    8. {minutes}: Minutes after login
    9. {seconds}: Seconds after login
    10. {milliseconds}: Milliseconds after login

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i62"></a>5.1.2.63. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime`

**Title:** Uptime

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i62_type"></a>5.1.2.63.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print how long system has been running

Specific value: `"uptime"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i62_key"></a>5.1.2.63.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i62_keyColor"></a>5.1.2.63.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i62_keyIcon"></a>5.1.2.63.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i62_keyWidth"></a>5.1.2.63.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i62_outputColor"></a>5.1.2.63.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i62_format"></a>5.1.2.63.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/uptimeFormat |

**Description:** Output format of the module `Uptime`. See Wiki for formatting syntax
    1. {days}: Days
    2. {hours}: Hours
    3. {minutes}: Minutes
    4. {seconds}: Seconds
    5. {milliseconds}: Milliseconds
    6. {boot-time}: Boot time in local timezone

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i63"></a>5.1.2.64. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version`

**Title:** Version

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i63_type"></a>5.1.2.64.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print Fastfetch version

Specific value: `"version"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i63_key"></a>5.1.2.64.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i63_keyColor"></a>5.1.2.64.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i63_keyIcon"></a>5.1.2.64.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i63_keyWidth"></a>5.1.2.64.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i63_outputColor"></a>5.1.2.64.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i63_format"></a>5.1.2.64.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/versionFormat |

**Description:** Output format of the module `Version`. See Wiki for formatting syntax
    1. {name}: Project name
    2. {version}: Version
    3. {version-tweak}: Version tweak
    4. {build-type}: Build type (debug or release)
    5. {sysname}: System name
    6. {arch}: Architecture
    7. {cmake-built-type}: CMake build type when compiling (Debug, Release, RelWithDebInfo, MinSizeRel)
    8. {compile-time}: Date time when compiling
    9. {compiler}: Compiler used when compiling
    10. {libc}: Libc used when compiling

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i64"></a>5.1.2.65. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan`

**Title:** Vulkan

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i64_type"></a>5.1.2.65.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print highest Vulkan version supported by the GPU

Specific value: `"vulkan"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i64_key"></a>5.1.2.65.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i64_keyColor"></a>5.1.2.65.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i64_keyIcon"></a>5.1.2.65.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i64_keyWidth"></a>5.1.2.65.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i64_outputColor"></a>5.1.2.65.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i64_format"></a>5.1.2.65.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > format</strong>  

</summary>
<blockquote>

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/vulkanFormat |

**Description:** Output format of the module `Vulkan`. See Wiki for formatting syntax
    1. {driver}: Driver name
    2. {api-version}: API version
    3. {conformance-version}: Conformance version
    4. {instance-version}: Instance version

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i65"></a>5.1.2.66. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper`

**Title:** Wallpaper

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i65_type"></a>5.1.2.66.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print image file path of current wallpaper

Specific value: `"wallpaper"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i65_key"></a>5.1.2.66.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i65_keyColor"></a>5.1.2.66.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i65_keyIcon"></a>5.1.2.66.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i65_keyWidth"></a>5.1.2.66.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i65_outputColor"></a>5.1.2.66.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i65_format"></a>5.1.2.66.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > format</strong>  

</summary>
<blockquote>

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | No                      |
| **Defined in** | #/$defs/wallpaperFormat |

**Description:** Output format of the module `Wallpaper`. See Wiki for formatting syntax
    1. {file-name}: File name
    2. {full-path}: Full path

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i66"></a>5.1.2.67. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather`

**Title:** Weather

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_type"></a>5.1.2.67.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print weather information

Specific value: `"weather"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_location"></a>5.1.2.67.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > location</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The location to display

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_timeout"></a>5.1.2.67.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > timeout</strong>  

</summary>
<blockquote>

|              |                  |
| ------------ | ---------------- |
| **Type**     | `integer`        |
| **Required** | No               |
| **Default**  | `"disabled (0)"` |

**Description:** Time in milliseconds to wait for the weather server to respond

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_outputFormat"></a>5.1.2.67.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputFormat</strong>  

</summary>
<blockquote>

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"%t+-+%C+(%l)"` |

**Description:** The output weather format to be used (must be URI encoded)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_key"></a>5.1.2.67.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_keyColor"></a>5.1.2.67.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_keyIcon"></a>5.1.2.67.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_keyWidth"></a>5.1.2.67.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_outputColor"></a>5.1.2.67.9. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i66_format"></a>5.1.2.67.10. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/weatherFormat |

**Description:** Output format of the module `Weather`. See Wiki for formatting syntax
    1. {result}: Weather result

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i67"></a>5.1.2.68. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi`

**Title:** Wi-Fi

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i67_type"></a>5.1.2.68.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print connected Wi-Fi info (SSID, connection and security protocol)

Specific value: `"wifi"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i67_key"></a>5.1.2.68.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i67_keyColor"></a>5.1.2.68.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i67_keyIcon"></a>5.1.2.68.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i67_keyWidth"></a>5.1.2.68.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i67_outputColor"></a>5.1.2.68.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i67_format"></a>5.1.2.68.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > format</strong>  

</summary>
<blockquote>

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/wifiFormat |

**Description:** Output format of the module `Wifi`. See Wiki for formatting syntax
    1. {inf-desc}: Interface description
    2. {inf-status}: Interface status
    3. {status}: Connection status
    4. {ssid}: Connection SSID
    5. {bssid}: Connection BSSID
    6. {protocol}: Connection protocol
    7. {signal-quality}: Connection signal quality (percentage num)
    8. {rx-rate}: Connection RX rate
    9. {tx-rate}: Connection TX rate
    10. {security}: Connection Security algorithm
    11. {signal-quality-bar}: Connection signal quality (percentage bar)
    12. {channel}: Connection channel number
    13. {band}: Connection channel band in GHz

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i68"></a>5.1.2.69. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager`

**Title:** Window Manager

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_type"></a>5.1.2.69.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print window manager name and version

Specific value: `"wm"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_detectPlugin"></a>5.1.2.69.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > detectPlugin</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if window manager plugin should be detected on supported platforms

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_key"></a>5.1.2.69.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_keyColor"></a>5.1.2.69.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_keyIcon"></a>5.1.2.69.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_keyWidth"></a>5.1.2.69.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_outputColor"></a>5.1.2.69.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i68_format"></a>5.1.2.69.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > format</strong>  

</summary>
<blockquote>

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/wmFormat |

**Description:** Output format of the module `WM`. See Wiki for formatting syntax
    1. {process-name}: WM process name
    2. {pretty-name}: WM pretty name
    3. {protocol-name}: WM protocol name
    4. {plugin-name}: WM plugin name
    5. {version}: WM version

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i69"></a>5.1.2.70. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme`

**Title:** WM Theme

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i69_type"></a>5.1.2.70.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current theme of window manager

Specific value: `"wmtheme"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i69_key"></a>5.1.2.70.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i69_keyColor"></a>5.1.2.70.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i69_keyIcon"></a>5.1.2.70.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i69_keyWidth"></a>5.1.2.70.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i69_outputColor"></a>5.1.2.70.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i69_format"></a>5.1.2.70.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > format</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/wmthemeFormat |

**Description:** Output format of the module `WMTheme`. See Wiki for formatting syntax
    1. {result}: WM theme

</blockquote>
</details>

</blockquote>
<blockquote>

##### <a name="modules_items_anyOf_i1_oneOf_i70"></a>5.1.2.71. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool`

**Title:** Zpool

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_type"></a>5.1.2.71.1. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print ZFS storage pools

Specific value: `"zpool"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_percent"></a>5.1.2.71.2. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > percent</strong>  

</summary>
<blockquote>

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_key"></a>5.1.2.71.3. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > key</strong>  

</summary>
<blockquote>

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_keyColor"></a>5.1.2.71.4. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyColor</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_keyIcon"></a>5.1.2.71.5. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyIcon</strong>  

</summary>
<blockquote>

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_keyWidth"></a>5.1.2.71.6. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyWidth</strong>  

</summary>
<blockquote>

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_outputColor"></a>5.1.2.71.7. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > outputColor</strong>  

</summary>
<blockquote>

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_oneOf_i70_format"></a>5.1.2.71.8. [Optional] Property JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > format</strong>  

</summary>
<blockquote>

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/zpoolFormat |

**Description:** Output format of the module `Zpool`. See Wiki for formatting syntax
    1. {name}: Zpool name
    2. {state}: Zpool state
    3. {used}: Size used
    4. {total}: Size total
    5. {used-percentage}: Size percentage num
    6. {fragmentation-percentage}: Fragmentation percentage num
    7. {used-percentage-bar}: Size percentage bar
    8. {fragmentation-percentage-bar}: Fragmentation percentage bar

</blockquote>
</details>

</blockquote>

</blockquote>

<details>
<summary>
<strong> <a name="modules_items_anyOf_i1_type"></a>5.1.2.72. [Required] Property JSON config > modules > modules items > anyOf > item 1 > type</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-05-15 at 14:22:26 +0200