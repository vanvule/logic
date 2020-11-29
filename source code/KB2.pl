dienThoai(mateSeries).
dienThoai(pSeries).
dienThoai(novaSeries).
dienThoai(gSeries).
dienThoai(ySeries).

dongHo(fit).
dongHo(gt).
dongHo(b).

taiNghe(freebud).
taiNghe(freelace).

phanMem(emui).
phanMem(hiSuite).

sanpham(mateSeries,m20).
sanpham(mateSeries,m30).
sanpham(mateSeries,m20pro).

sanpham(pSeries,p40).
sanpham(pSeries,p40pro).
sanpham(pSeries,p40proPlus).
sanpham(pSeries,p30).
sanpham(pSeries,p30lite).
sanpham(pSeries,p30pro).
sanpham(pSeries,p20pro).
sanpham(pSeries,p9).
sanpham(pSeries,p9lite).

sanpham(novaSeries,nova7i).
sanpham(novaSeries,nova5t).
sanpham(novaSeries,nova3i).
sanpham(novaSeries,nova3).
sanpham(novaSeries,nova3e).
sanpham(novaSeries,nova21).

sanpham(gSeries,gr5_2017).
sanpham(gSeries,gr5_2017_pro).
sanpham(gSeries,gr5).

sanpham(ySeries,y9s).
sanpham(ySeries,y6p).
sanpham(ySeries,y9prime).
sanpham(ySeries,y9_2019).
sanpham(ySeries,y7pro_2019).

sanpham(gt,gt2e).
sanpham(gt,gt2).
sanpham(gt,gtBasic).
sanpham(b,b0).
sanpham(b,b2).
sanpham(b,b5).

sanpham(freebud,fbpro).
sanpham(freebud,fb3).
sanpham(freebud,fb3i).
sanpham(freebud,fbstudio).
sanpham(freelace,flpro).

laDienThoai(X):-sanpham(Y,X),dienThoai(Y).
laDienThoaiPhoThong(X):-sanpham(novaSeries,X).
laDienThoaiCaoCap(X):-(sanpham(mateSeries,X));(sanpham(pSeries,X)).
laDongHo(X):-sanpham(Y,X),dongHo(Y).
laDongHoCaoCap(X):-sanpham(gt,X).
laTaiNghe(X):-sanpham(Y,X),taiNghe(Y).
laPhanMem(X):-phanMem(X).
laSP_Huawei(X):-(laDienThoai(X));(laDongHo(X));(laTaiNghe(X));(laPhanMem(X)).
laPhuKienUaChuong(X):-(sanpham(freebud,X));(sanpham(gt,X)).









