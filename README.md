# Cào Dữ Liệu

### Demo lấy dữ liệu từ 10 trang tại [thuvienphapluat](https://thuvienphapluat.vn/phap-luat/bat-dong-san)


https://github.com/sonnees/CrawlData_thuvienphapluat.vn/assets/110987763/1908dc5c-ab58-40f3-912a-b3932a2d41c5


### Cấu trúc data sau khi đã sàng lọc:
```
{
    "url": link bài báo có trích luật,
    "title": tiêu đề,
    "introduction": đặt vấn đề, giới thiệu chung,
    "content": [
        {
            "sub_title": nội dung chính thứ nhất,
            "sub_content": [
                "Theo quy định tại khoản 2 Điều 4 Nghị định 02/2022/NĐ-CP, nội dung như sau:",
                [
                    trích luật 1
                ],
                [
                    trích luật 2
                ],
                nội dung không phải luật,
                nội dung không phải luật,
                ...,
           ]
        },
        {
            "sub_title": nội dung chính thứ 2,
            "sub_content": []
        }
    ]
}
```

