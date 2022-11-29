import {Box, Button, Grid, HStack, Image, Text, useColorModeValue, VStack} from "@chakra-ui/react";
import {FaRegHeart, FaStar} from "react-icons/fa";

export default function Room() {
    const gray = useColorModeValue("gray.600", "gray.300")
    return (
        <VStack alignItems={"flex-start"}>
            <Box position="relative" overflow={"hidden"} mb={3} rounded={"2xl"}>
                <Image
                    minH={"280"}
                    src={"https://a0.muscache.com/im/pictures/miso/Hosting-717134404264905813/original/dfe9fd1e-a010-43c9-b546-0bbc7d59f7f3.jpeg?im_w=720"}>
                </Image>
                <Button
                    variant={"unstyled"}
                    position={"absolute"}
                    top={0}
                    right={0}
                    color={"white"}
                >
                    <FaRegHeart size={"20px"}/>
                </Button>
            </Box>
            <Box>
                <Grid gap={2} templateColumns={"6fr 1fr"}>
                    <Text display={"block"} as={"b"} noOfLines={1} fontSize={"md"}>
                        히든 헤이븐 - 수영장과 바다 전망을 즐길 수 있는 5베드 빌라
                    </Text>
                    <HStack spacing={1} alignItems={"center"}>
                        <FaStar size={12}/>
                        <Text fontSize={"sm"}>5.0</Text>
                    </HStack>
                </Grid>
                <Text fontSize={"sm"} color={"gray"}>
                    케이프타운, 웨스턴케이프 주, 남아프리카
                </Text>
            </Box>
            <Text fontSize={"sm"} color={"gray"}>
                <Text as={"b"}>$72</Text> / night
            </Text>
        </VStack>
)
}