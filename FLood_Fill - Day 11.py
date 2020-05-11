def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def fill(image, sr, sc, newColor,prevColor):
            if sr<0 or sc<0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc] != prevColor: return

            image[sr][sc] = newColor
            fill(image,sr-1,sc,newColor,prevColor)
            fill(image,sr+1,sc,newColor,prevColor)
            fill(image,sr,sc-1,newColor,prevColor)
            fill(image,sr,sc+1,newColor,prevColor)

        if(image[sr][sc]==newColor): return image
        fill(image, sr, sc, newColor,image[sr][sc])
        return image