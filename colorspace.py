cv2.namedWindow('P-> Previous, N-> Next',cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('SelectBGR',cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('SelectHSV',cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('SelectYCB',cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('SelectLAB',cv2.WINDOW_AUTOSIZE)

    #moving the windows to stack them horizontally
    cv2.moveWindow('P-> Previous, N-> Next',initialX,initialY)
    cv2.moveWindow('SelectBGR',initialX + (rsize + 5),initialY)
    cv2.moveWindow('SelectHSV',initialX + 2*(rsize + 5),initialY)
    cv2.moveWindow('SelectYCB',initialX + 3*(rsize + 5),initialY)
    cv2.moveWindow('SelectLAB',initialX + 4*(rsize + 5),initialY)

    #creating trackbars to get values for YCrCb
    cv2.createTrackbar('CrMin','SelectYCB',0,255,onTrackbarActivity)
    cv2.createTrackbar('CrMax','SelectYCB',0,255,onTrackbarActivity)
    cv2.createTrackbar('CbMin','SelectYCB',0,255,onTrackbarActivity)
    cv2.createTrackbar('CbMax','SelectYCB',0,255,onTrackbarActivity)
    cv2.createTrackbar('YMin','SelectYCB',0,255,onTrackbarActivity)
    cv2.createTrackbar('YMax','SelectYCB',0,255,onTrackbarActivity)

    #creating trackbars to get values for HSV
    cv2.createTrackbar('HMin','SelectHSV',0,180,onTrackbarActivity)
    cv2.createTrackbar('HMax','SelectHSV',0,180,onTrackbarActivity)
    cv2.createTrackbar('SMin','SelectHSV',0,255,onTrackbarActivity)
    cv2.createTrackbar('SMax','SelectHSV',0,255,onTrackbarActivity)
    cv2.createTrackbar('VMin','SelectHSV',0,255,onTrackbarActivity)
    cv2.createTrackbar('VMax','SelectHSV',0,255,onTrackbarActivity)

    #creating trackbars to get values for BGR
    cv2.createTrackbar('BGRBMin','SelectBGR',0,255,onTrackbarActivity)
    cv2.createTrackbar('BGRBMax','SelectBGR',0,255,onTrackbarActivity)
    cv2.createTrackbar('BGRGMin','SelectBGR',0,255,onTrackbarActivity)
    cv2.createTrackbar('BGRGMax','SelectBGR',0,255,onTrackbarActivity)
    cv2.createTrackbar('BGRRMin','SelectBGR',0,255,onTrackbarActivity)
    cv2.createTrackbar('BGRRMax','SelectBGR',0,255,onTrackbarActivity)

    #creating trackbars to get values for LAB
    cv2.createTrackbar('LABLMin','SelectLAB',0,255,onTrackbarActivity)
    cv2.createTrackbar('LABLMax','SelectLAB',0,255,onTrackbarActivity)
    cv2.createTrackbar('LABAMin','SelectLAB',0,255,onTrackbarActivity)
    cv2.createTrackbar('LABAMax','SelectLAB',0,255,onTrackbarActivity)
    cv2.createTrackbar('LABBMin','SelectLAB',0,255,onTrackbarActivity)
    cv2.createTrackbar('LABBMax','SelectLAB',0,255,onTrackbarActivity)

    # show all images initially
    cv2.imshow('SelectHSV',original)
    cv2.imshow('SelectYCB',original)
    cv2.imshow('SelectLAB',original)
    cv2.imshow('SelectBGR',original)