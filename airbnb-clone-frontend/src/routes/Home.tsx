import {Box, Grid, HStack, Image, Text, VStack} from "@chakra-ui/react";
import {FaStar} from "react-icons/fa";

export default function Home() {
    return (
        <Grid
            mt={10}
            px={40}
            columnGap={4}
            rowGap={8}
            templateColumns={"repeat(5, 1fr)"}>
            <VStack alignItems={"flex-start"}>
                <Box overflow={"hidden"} mb={3} rounded={"3xl"}>
                    <Image
                        h={"280"}
                        src={"https://a0.muscache.com/im/pictures/miso/Hosting-717134404264905813/original/dfe9fd1e-a010-43c9-b546-0bbc7d59f7f3.jpeg?im_w=720"}></Image>
                </Box>
                <Box>
                    <Grid gap={2} templateColumns={"6fr 1fr"}>
                        <Text display={"block"} as={"b"} noOfLines={1} fontSize={"md"}>
                            히든 헤이븐 - 수영장과 바다 전망을 즐길 수 있는 5베드 빌라
                        </Text>
                        <HStack>
                            <FaStar size={15}/>
                            <Text>5.0</Text>
                        </HStack>
                    </Grid>
                    <Text fontSize={"sm"} color={"gray.600"}>
                        케이프타운, 웨스턴케이프 주, 남아프리카
                    </Text>
                </Box>
                <Text fontSize={"sm"} color={"gray.600"}>
                    <Text as={"b"}>$72</Text> / night
                </Text>
            </VStack>
        </Grid>
    )
}